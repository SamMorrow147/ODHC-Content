import os
import time
import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from pathlib import Path
from markdownify import markdownify as md
from content_mapper import ContentMapper

class ODHCScraper:
    """Main scraper for ODHC website"""
    
    def __init__(self, config_path='config.json'):
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        
        self.base_url = self.config['base_url']
        self.visited_urls = set()
        self.scraped_content = {}
        self.mapper = ContentMapper(config_path)
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': self.config['scraper_settings']['user_agent']
        })
        
        # Create output directories
        self._create_directories()
        
    def _create_directories(self):
        """Create all necessary output directories"""
        for dir_path in self.config['output_dirs'].values():
            Path(dir_path).mkdir(parents=True, exist_ok=True)
        
        # Create additional subdirectories
        Path('scraped_content/about/services').mkdir(parents=True, exist_ok=True)
        Path('scraped_content/about/locations').mkdir(parents=True, exist_ok=True)
        Path('scraped_content/patient-resources').mkdir(parents=True, exist_ok=True)
        Path('scraped_content/footer').mkdir(parents=True, exist_ok=True)
        Path('scraped_content/unmapped').mkdir(parents=True, exist_ok=True)
        
    def is_valid_url(self, url):
        """Check if URL is valid and belongs to the target domain"""
        parsed = urlparse(url)
        base_parsed = urlparse(self.base_url)
        return parsed.netloc == base_parsed.netloc or parsed.netloc == ''
    
    def download_asset(self, url, asset_type='image'):
        """Download image or PDF and return local path"""
        try:
            if not url:
                return None
                
            # Make URL absolute
            url = urljoin(self.base_url, url)
            
            # Skip if already visited
            if url in self.visited_urls:
                return self._get_local_asset_path(url, asset_type)
            
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            # Determine file name
            parsed = urlparse(url)
            filename = os.path.basename(parsed.path)
            if not filename:
                filename = f'asset_{len(self.visited_urls)}'
            
            # Determine output directory
            if asset_type == 'pdf' or filename.endswith('.pdf'):
                output_dir = self.config['output_dirs']['pdfs']
            else:
                output_dir = self.config['output_dirs']['images']
            
            # Save file
            file_path = os.path.join(output_dir, filename)
            with open(file_path, 'wb') as f:
                f.write(response.content)
            
            self.visited_urls.add(url)
            print(f"  Downloaded: {filename}")
            return file_path
            
        except Exception as e:
            print(f"  Error downloading {url}: {e}")
            return None
    
    def _get_local_asset_path(self, url, asset_type):
        """Get local path for an already downloaded asset"""
        parsed = urlparse(url)
        filename = os.path.basename(parsed.path)
        
        if asset_type == 'pdf' or filename.endswith('.pdf'):
            return os.path.join(self.config['output_dirs']['pdfs'], filename)
        else:
            return os.path.join(self.config['output_dirs']['images'], filename)
    
    def clean_html(self, soup):
        """Remove unwanted elements from HTML"""
        # Remove script and style elements
        for element in soup(['script', 'style', 'nav', 'footer', 'header']):
            element.decompose()
        
        # Remove common non-content classes
        for element in soup.find_all(class_=['cookie-notice', 'popup', 'modal', 'advertisement']):
            element.decompose()
            
        return soup
    
    def extract_page_content(self, url):
        """Extract and process content from a single page"""
        try:
            print(f"\nScraping: {url}")
            
            response = self.session.get(url, timeout=15)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'lxml')
            soup = self.clean_html(soup)
            
            # Extract title
            title = soup.find('h1')
            if not title:
                title = soup.find('title')
            title_text = title.get_text(strip=True) if title else 'Untitled'
            
            # Download images and update their src
            for img in soup.find_all('img'):
                src = img.get('src')
                if src:
                    local_path = self.download_asset(src, 'image')
                    if local_path:
                        img['src'] = f'../../{local_path}'
            
            # Download PDFs
            for link in soup.find_all('a', href=True):
                href = link['href']
                if href.endswith('.pdf'):
                    local_path = self.download_asset(href, 'pdf')
                    if local_path:
                        link['href'] = f'../../{local_path}'
            
            # Find main content area
            main_content = (
                soup.find('main') or 
                soup.find('article') or 
                soup.find(class_=['content', 'main-content', 'entry-content']) or
                soup.find('body')
            )
            
            if main_content:
                # Convert to markdown
                markdown_content = md(str(main_content), heading_style='ATX')
                
                return {
                    'url': url,
                    'title': title_text,
                    'content': markdown_content,
                    'links': self._extract_links(soup)
                }
            
            return None
            
        except Exception as e:
            print(f"  Error scraping {url}: {e}")
            return None
    
    def _extract_links(self, soup):
        """Extract all internal links from page"""
        links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(self.base_url, href)
            
            # Only include internal links
            if self.is_valid_url(full_url) and not href.startswith('#'):
                # Remove fragment
                full_url = full_url.split('#')[0]
                links.append(full_url)
        
        return list(set(links))
    
    def scrape_recursive(self, start_url, max_depth=3, current_depth=0):
        """Recursively scrape website starting from given URL"""
        if current_depth >= max_depth:
            return
        
        if start_url in self.visited_urls:
            return
        
        self.visited_urls.add(start_url)
        
        # Extract content
        content = self.extract_page_content(start_url)
        
        if content:
            # Store content with URL as key
            self.scraped_content[start_url] = content
            
            # Add delay to be respectful
            time.sleep(self.config['scraper_settings']['delay_seconds'])
            
            # Recursively scrape linked pages
            for link in content['links']:
                if link not in self.visited_urls:
                    self.scrape_recursive(link, max_depth, current_depth + 1)
    
    def save_to_markdown(self):
        """Save scraped content to organized markdown files"""
        print("\n" + "="*50)
        print("Organizing content into markdown files...")
        print("="*50)
        
        # Group content by target file
        file_contents = {}
        
        for url, content in self.scraped_content.items():
            target_file = self.mapper.get_target_file(url)
            
            if target_file not in file_contents:
                file_contents[target_file] = []
            
            file_contents[target_file].append({
                'url': url,
                'title': content['title'],
                'content': content['content']
            })
        
        # Write to files
        for target_file, contents in file_contents.items():
            full_path = self.mapper.get_full_path(target_file)
            self.mapper.ensure_directory(full_path)
            
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(f"# {target_file.replace('.md', '').replace('/', ' > ').title()}\n\n")
                f.write(f"*Content scraped from ODHC website*\n\n")
                f.write("---\n\n")
                
                for item in contents:
                    f.write(f"## Source: {item['title']}\n")
                    f.write(f"*URL: {item['url']}*\n\n")
                    f.write(item['content'])
                    f.write("\n\n---\n\n")
            
            print(f"Created: {target_file}")
        
        # Generate report
        self._generate_report(file_contents)
    
    def _generate_report(self, file_contents):
        """Generate a content mapping report"""
        with open('content_report.txt', 'w', encoding='utf-8') as f:
            f.write("ODHC Content Scraping Report\n")
            f.write("="*60 + "\n\n")
            f.write(f"Total pages scraped: {len(self.scraped_content)}\n")
            f.write(f"Total markdown files created: {len(file_contents)}\n\n")
            
            f.write("\nContent Organization:\n")
            f.write("-"*60 + "\n")
            for target_file, contents in sorted(file_contents.items()):
                f.write(f"\n{target_file} ({len(contents)} sources)\n")
                for item in contents:
                    f.write(f"  - {item['title']}: {item['url']}\n")
            
            # Report unmapped pages
            unmapped = self.mapper.get_unmapped_report()
            if unmapped:
                f.write("\n\nPages requiring manual review (unmapped):\n")
                f.write("-"*60 + "\n")
                for page in unmapped:
                    f.write(f"  - {page}\n")
        
        print("\nReport generated: content_report.txt")
    
    def run(self):
        """Execute the complete scraping process"""
        print("="*60)
        print("ODHC Website Scraper")
        print("="*60)
        print(f"Target: {self.base_url}")
        print(f"Max depth: {self.config['scraper_settings']['max_depth']}")
        print("="*60)
        
        # Start scraping
        self.scrape_recursive(
            self.base_url,
            max_depth=self.config['scraper_settings']['max_depth']
        )
        
        # Save organized content
        self.save_to_markdown()
        
        print("\n" + "="*60)
        print("Scraping complete!")
        print(f"Pages scraped: {len(self.scraped_content)}")
        print(f"Assets downloaded: Images and PDFs saved to assets/")
        print("="*60)

if __name__ == '__main__':
    scraper = ODHCScraper()
    scraper.run()
    
    # Generate review site
    print("\nGenerating review website...")
    from generate_review_site import generate_review_site
    generate_review_site()
    print("\nDone! Open review_site/index.html to view the organized content.")

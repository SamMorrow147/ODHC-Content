import json
import os
from urllib.parse import urlparse, urljoin
from pathlib import Path

class ContentMapper:
    """Maps scraped content from old URL structure to new page organization"""
    
    def __init__(self, config_path='config.json'):
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        
        self.base_url = self.config['base_url']
        self.page_mappings = self.config['page_mappings']
        self.output_dir = self.config['output_dirs']['scraped_content']
        self.unmapped_pages = []
        
    def normalize_url(self, url):
        """Convert URL to path for mapping lookup"""
        parsed = urlparse(url)
        path = parsed.path.rstrip('/')
        return path if path else '/'
    
    def get_target_file(self, url):
        """Get the target markdown file path for a given URL"""
        normalized = self.normalize_url(url)
        
        # Check exact mapping
        if normalized in self.page_mappings:
            return self.page_mappings[normalized]
        
        # Check if URL contains key terms for intelligent mapping
        url_lower = normalized.lower()
        
        # Service pages
        if 'medical' in url_lower:
            return 'about/services/medical.md'
        elif 'dental' in url_lower:
            return 'about/services/dental.md'
        elif 'behavioral' in url_lower or 'mental' in url_lower:
            return 'about/services/behavioral-health.md'
        elif 'insurance' in url_lower:
            return 'about/services/insurance-enrollment.md'
        elif 'chiropractic' in url_lower:
            return 'about/services/chiropractic-care.md'
        
        # Location pages
        elif 'mankato' in url_lower:
            return 'about/locations/mankato.md'
        elif 'jordan' in url_lower or 'shakopee' in url_lower:
            return 'about/locations/shakopee.md'
        elif 'school' in url_lower and ('location' in url_lower or 'center' in url_lower):
            return 'about/locations/school-based.md'
        
        # About pages
        elif 'mission' in url_lower or 'vision' in url_lower or 'values' in url_lower:
            return 'about/mission-vision-values.md'
        elif 'team' in url_lower or 'staff' in url_lower or 'leadership' in url_lower:
            return 'about/team.md'
        elif 'news' in url_lower or 'event' in url_lower:
            return 'about/news-events.md'
        elif 'career' in url_lower or 'job' in url_lower:
            return 'about/careers.md'
        
        # Patient resources
        elif 'portal' in url_lower:
            return 'patient-resources/portal.md'
        elif 'form' in url_lower:
            return 'patient-resources/forms.md'
        elif 'financial' in url_lower or 'assistance' in url_lower or 'sliding' in url_lower:
            return 'patient-resources/financial-assistance.md'
        elif 'community' in url_lower and 'resource' in url_lower:
            return 'patient-resources/community-resources.md'
        
        # Other pages
        elif 'contact' in url_lower:
            return 'contact.md'
        elif 'donate' in url_lower or 'donation' in url_lower:
            return 'donate.md'
        elif 'privacy' in url_lower:
            return 'footer/privacy-policy.md'
        elif 'faq' in url_lower or 'question' in url_lower:
            return 'footer/faq.md'
        elif 'annual' in url_lower and 'report' in url_lower:
            return 'footer/annual-report.md'
        
        # If no mapping found, flag for review
        self.unmapped_pages.append(normalized)
        return f'unmapped/{normalized.strip("/").replace("/", "-") or "home"}.md'
    
    def get_full_path(self, target_file):
        """Get full file system path for target file"""
        return os.path.join(self.output_dir, target_file)
    
    def ensure_directory(self, file_path):
        """Ensure directory exists for file path"""
        directory = os.path.dirname(file_path)
        if directory:
            Path(directory).mkdir(parents=True, exist_ok=True)
    
    def get_unmapped_report(self):
        """Return list of pages that couldn't be automatically mapped"""
        return self.unmapped_pages

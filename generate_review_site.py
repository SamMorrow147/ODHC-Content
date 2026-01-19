import os
import markdown
from pathlib import Path
import json
import re

def get_all_markdown_files(base_dir='scraped_content'):
    """Get all markdown files organized by directory"""
    md_files = {}
    
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.md'):
                rel_path = os.path.relpath(os.path.join(root, file), base_dir)
                md_files[rel_path] = os.path.join(root, file)
    
    return md_files

def organize_by_new_structure(md_files):
    """Organize files into the new navigation structure"""
    structure = {
        'About': {
            'Mission, Vision, and Values': [],
            'Services': {
                'Overview': [],
                'Medical': [],
                'Dental': [],
                'Behavioral Health': [],
                'Insurance Enrollment': [],
                'Chiropractic Care': []
            },
            'Locations': {
                'Mankato': [],
                'Shakopee': [],
                'School-Based Centers': []
            },
            'Meet the Team': [],
            'News and Events': [],
            'Careers': []
        },
        'Patient Resources': {
            'Patient Portal': [],
            'Forms': [],
            'Financial Assistance': [],
            'Community Resources': []
        },
        'Contact': [],
        'Donate': [],
        'Footer Pages': {
            'Privacy Policy': [],
            'FAQ': [],
            'Annual Report': []
        }
    }
    
    # Map files to structure
    file_mapping = {}
    
    for rel_path, full_path in md_files.items():
        if 'overview.md' in rel_path and 'services' in rel_path:
            file_mapping[full_path] = ('About', 'Services', 'Overview')
        elif 'medical.md' in rel_path:
            file_mapping[full_path] = ('About', 'Services', 'Medical')
        elif 'dental.md' in rel_path:
            file_mapping[full_path] = ('About', 'Services', 'Dental')
        elif 'behavioral-health.md' in rel_path:
            file_mapping[full_path] = ('About', 'Services', 'Behavioral Health')
        elif 'insurance-enrollment.md' in rel_path:
            file_mapping[full_path] = ('About', 'Services', 'Insurance Enrollment')
        elif 'chiropractic-care.md' in rel_path:
            file_mapping[full_path] = ('About', 'Services', 'Chiropractic Care')
        elif 'mankato.md' in rel_path:
            file_mapping[full_path] = ('About', 'Locations', 'Mankato')
        elif 'shakopee.md' in rel_path:
            file_mapping[full_path] = ('About', 'Locations', 'Shakopee')
        elif 'mission' in rel_path or 'vision' in rel_path or 'values' in rel_path:
            file_mapping[full_path] = ('About', 'Mission, Vision, and Values')
        elif 'team.md' in rel_path:
            file_mapping[full_path] = ('About', 'Meet the Team')
        elif 'news' in rel_path or 'events' in rel_path:
            file_mapping[full_path] = ('About', 'News and Events')
        elif 'careers.md' in rel_path:
            file_mapping[full_path] = ('About', 'Careers')
        elif 'portal.md' in rel_path:
            file_mapping[full_path] = ('Patient Resources', 'Patient Portal')
        elif 'forms.md' in rel_path:
            file_mapping[full_path] = ('Patient Resources', 'Forms')
        elif 'financial-assistance.md' in rel_path:
            file_mapping[full_path] = ('Patient Resources', 'Financial Assistance')
        elif 'community-resources.md' in rel_path:
            file_mapping[full_path] = ('Patient Resources', 'Community Resources')
        elif 'contact.md' in rel_path:
            file_mapping[full_path] = ('Contact',)
        elif 'donate.md' in rel_path:
            file_mapping[full_path] = ('Donate',)
        elif 'privacy-policy.md' in rel_path:
            file_mapping[full_path] = ('Footer Pages', 'Privacy Policy')
        elif 'faq.md' in rel_path:
            file_mapping[full_path] = ('Footer Pages', 'FAQ')
        elif 'annual-report.md' in rel_path:
            file_mapping[full_path] = ('Footer Pages', 'Annual Report')
        elif 'overview.md' in rel_path:
            file_mapping[full_path] = ('About', 'Mission, Vision, and Values')
    
    return file_mapping

def extract_source_urls(md_content):
    """Extract source URLs from markdown content"""
    url_matches = re.findall(r'\*URL:\s*(https?://[^\*\n]+)\*', md_content)
    return list(set(url_matches))

def find_images_in_markdown(md_content):
    """Find all images referenced in the markdown content"""
    image_matches = re.findall(r'!\[.*?\]\((.*?)\)', md_content)
    return image_matches

def convert_md_to_html(md_file_path):
    """Convert markdown file to HTML content and extract metadata"""
    try:
        with open(md_file_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Extract URLs and images before converting
        source_urls = extract_source_urls(md_content)
        images = find_images_in_markdown(md_content)
        
        html_content = markdown.markdown(md_content, extensions=['extra', 'tables'])
        
        return html_content, source_urls, images, md_content
    except Exception as e:
        return f"<p>Error loading content: {e}</p>", [], [], ""

def create_wireframe(page_title, content_html):
    """Create a clean structural wireframe based on page type"""
    
    # Determine page type
    is_service = any(keyword in page_title.lower() for keyword in ['service', 'medical', 'dental', 'behavioral', 'chiropractic', 'insurance'])
    is_location = any(keyword in page_title.lower() for keyword in ['location', 'mankato', 'shakopee'])
    is_resource = any(keyword in page_title.lower() for keyword in ['resource', 'portal', 'form', 'financial', 'assistance'])
    is_contact = 'contact' in page_title.lower()
    is_donate = 'donate' in page_title.lower()
    
    # Count content elements
    has_lists = '<ul>' in content_html or '<li>' in content_html
    paragraph_count = content_html.count('<p>')
    heading_count = content_html.count('<h2>') + content_html.count('<h3>')
    
    wireframe = f"""
    <div class="wireframe-container">
        <div class="wireframe-header">
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 15px;">
                <div>
                    <div class="wireframe-logo"></div>
                    <div class="wireframe-label">Logo + Tagline</div>
                </div>
                <div style="display: flex; gap: 10px;">
                    <div class="wireframe-button"></div>
                    <div class="wireframe-button"></div>
                </div>
            </div>
        </div>
        
        <div class="wireframe-nav">
            <div class="wireframe-nav-item"></div>
            <div class="wireframe-nav-item"></div>
            <div class="wireframe-nav-item"></div>
            <div class="wireframe-nav-item"></div>
            <div class="wireframe-nav-item"></div>
        </div>
        
        <div class="wireframe-content">
    """
    
    # Hero section
    wireframe += f"""
            <div class="wireframe-hero">
                <div class="wireframe-section-label">Hero Section</div>
                <div class="wireframe-title"></div>
                <div class="wireframe-subtitle"></div>
                <div class="wireframe-text"></div>
                <div class="wireframe-text medium"></div>
                <div class="wireframe-text short"></div>
    """
    
    # Add CTA buttons for service/location pages
    if is_service or is_location:
        wireframe += """
                <div style="margin-top: 15px;">
                    <div class="wireframe-button"></div>
                    <div class="wireframe-button"></div>
                    <div class="wireframe-label">CTA Buttons</div>
                </div>
        """
    
    wireframe += """
            </div>
    """
    
    # Service page specific layout
    if is_service:
        wireframe += """
            <div class="wireframe-section">
                <div class="wireframe-section-label">Services List</div>
                <div class="wireframe-heading"></div>
                <div class="wireframe-list">
                    <div class="wireframe-list-item">
                        <div class="wireframe-bullet"></div>
                        <div class="wireframe-list-text"></div>
                    </div>
                    <div class="wireframe-list-item">
                        <div class="wireframe-bullet"></div>
                        <div class="wireframe-list-text"></div>
                    </div>
                    <div class="wireframe-list-item">
                        <div class="wireframe-bullet"></div>
                        <div class="wireframe-list-text"></div>
                    </div>
                    <div class="wireframe-list-item">
                        <div class="wireframe-bullet"></div>
                        <div class="wireframe-list-text"></div>
                    </div>
                </div>
            </div>
            
            <div class="wireframe-section">
                <div class="wireframe-section-label">Team Image</div>
                <div class="wireframe-image">Image</div>
            </div>
            
            <div class="wireframe-section" style="background: #fafafa;">
                <div class="wireframe-section-label">2-Column Info Cards</div>
                <div class="wireframe-grid">
                    <div class="wireframe-card">
                        <div class="wireframe-icon">Icon</div>
                        <div class="wireframe-card-title"></div>
                        <div class="wireframe-card-text"></div>
                    </div>
                    <div class="wireframe-card">
                        <div class="wireframe-icon">Icon</div>
                        <div class="wireframe-card-title"></div>
                        <div class="wireframe-card-text"></div>
                    </div>
                </div>
            </div>
        """
    
    # Location page specific layout
    if is_location:
        wireframe += """
            <div class="wireframe-section">
                <div class="wireframe-section-label">2-Column Layout</div>
                <div class="wireframe-grid">
                    <div class="wireframe-card">
                        <div class="wireframe-label">Address & Hours</div>
                        <div class="wireframe-card-title"></div>
                        <div class="wireframe-card-text"></div>
                        <div class="wireframe-card-text"></div>
                        <div class="wireframe-card-text"></div>
                    </div>
                    <div class="wireframe-card">
                        <div class="wireframe-label">Map</div>
                        <div class="wireframe-image" style="height: 200px;">Map</div>
                    </div>
                </div>
            </div>
            
            <div class="wireframe-section" style="background: #fafafa;">
                <div class="wireframe-section-label">5-Column Services Row</div>
                <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 15px;">
                    <div class="wireframe-card">
                        <div class="wireframe-icon" style="margin: 0 auto;">Icon</div>
                        <div style="font-weight: 600; font-size: 0.75rem; text-align: center; margin-top: 8px;">Medical</div>
                    </div>
                    <div class="wireframe-card">
                        <div class="wireframe-icon" style="margin: 0 auto;">Icon</div>
                        <div style="font-weight: 600; font-size: 0.75rem; text-align: center; margin-top: 8px;">Dental</div>
                    </div>
                    <div class="wireframe-card">
                        <div class="wireframe-icon" style="margin: 0 auto;">Icon</div>
                        <div style="font-weight: 600; font-size: 0.75rem; text-align: center; margin-top: 8px;">Behavioral Health</div>
                    </div>
                    <div class="wireframe-card">
                        <div class="wireframe-icon" style="margin: 0 auto;">Icon</div>
                        <div style="font-weight: 600; font-size: 0.75rem; text-align: center; margin-top: 8px;">Insurance Enrollment</div>
                    </div>
                    <div class="wireframe-card">
                        <div class="wireframe-icon" style="margin: 0 auto;">Icon</div>
                        <div style="font-weight: 600; font-size: 0.75rem; text-align: center; margin-top: 8px;">Chiropractic Care</div>
                    </div>
                </div>
            </div>
        """
    
    # Resource page layout
    if is_resource:
        wireframe += """
            <div class="wireframe-section">
                <div class="wireframe-section-label">Content Section</div>
                <div class="wireframe-heading"></div>
                <div class="wireframe-text"></div>
                <div class="wireframe-text"></div>
                <div class="wireframe-text short"></div>
            </div>
            
            <div class="wireframe-section" style="background: #fafafa;">
                <div class="wireframe-section-label">2-Column Cards</div>
                <div class="wireframe-grid">
                    <div class="wireframe-card">
                        <div class="wireframe-card-title"></div>
                        <div class="wireframe-card-text"></div>
                        <div class="wireframe-card-text short"></div>
                        <div class="wireframe-button" style="width: 100px; margin-top: 10px;"></div>
                    </div>
                    <div class="wireframe-card">
                        <div class="wireframe-card-title"></div>
                        <div class="wireframe-card-text"></div>
                        <div class="wireframe-card-text short"></div>
                        <div class="wireframe-button" style="width: 100px; margin-top: 10px;"></div>
                    </div>
                </div>
            </div>
        """
    
    # Contact page layout
    if is_contact:
        wireframe += """
            <div class="wireframe-section">
                <div class="wireframe-section-label">2-Column Layout</div>
                <div class="wireframe-grid">
                    <div class="wireframe-card">
                        <div class="wireframe-label">Contact Form</div>
                        <div class="wireframe-heading" style="margin-bottom: 15px;"></div>
                        <div class="wireframe-text" style="height: 40px; margin: 8px 0; background: #fff; border: 2px solid #999;">Input</div>
                        <div class="wireframe-text" style="height: 40px; margin: 8px 0; background: #fff; border: 2px solid #999;">Input</div>
                        <div class="wireframe-text" style="height: 40px; margin: 8px 0; background: #fff; border: 2px solid #999;">Input</div>
                        <div class="wireframe-text" style="height: 100px; margin: 8px 0; background: #fff; border: 2px solid #999;">Textarea</div>
                        <div class="wireframe-button" style="margin-top: 10px;"></div>
                    </div>
                    
                    <div class="wireframe-card">
                        <div class="wireframe-label">Contact Info</div>
                        <div class="wireframe-heading" style="margin-bottom: 15px;"></div>
                        <div class="wireframe-text"></div>
                        <div class="wireframe-text"></div>
                        <div class="wireframe-text"></div>
                        <div style="display: flex; gap: 10px; margin-top: 20px;">
                            <div class="wireframe-icon">Icon</div>
                            <div class="wireframe-icon">Icon</div>
                        </div>
                    </div>
                </div>
            </div>
        """
    
    # Add general content sections based on heading count
    if heading_count > 0 and not (is_service or is_location or is_resource or is_contact):
        for i in range(min(heading_count, 2)):
            wireframe += f"""
            <div class="wireframe-section">
                <div class="wireframe-section-label">Content Section</div>
                <div class="wireframe-heading"></div>
                <div class="wireframe-text"></div>
                <div class="wireframe-text medium"></div>
                <div class="wireframe-text short"></div>
            </div>
            """
    
    # Footer
    wireframe += """
            <div class="wireframe-section" style="background: #e0e0e0; border-top: 3px solid #999;">
                <div class="wireframe-section-label">4-Column Footer</div>
                <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px;">
                    <div>
                        <div class="wireframe-text" style="height: 14px; background: #999;"></div>
                        <div class="wireframe-text" style="height: 8px; margin: 6px 0;"></div>
                        <div class="wireframe-text short" style="height: 8px;"></div>
                    </div>
                    <div>
                        <div class="wireframe-text" style="height: 14px; background: #999;"></div>
                        <div class="wireframe-text" style="height: 8px; margin: 6px 0;"></div>
                        <div class="wireframe-text" style="height: 8px; margin: 6px 0;"></div>
                    </div>
                    <div>
                        <div class="wireframe-text" style="height: 14px; background: #999;"></div>
                        <div class="wireframe-text" style="height: 8px; margin: 6px 0;"></div>
                        <div class="wireframe-text" style="height: 8px; margin: 6px 0;"></div>
                    </div>
                    <div>
                        <div class="wireframe-text" style="height: 14px; background: #999;"></div>
                        <div class="wireframe-text" style="height: 8px; margin: 6px 0;"></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """
    
    return wireframe

def create_design_preview(content_html, page_title):
    """Create a styled design preview of the page content"""
    # Clean up content for preview (remove source info boxes)
    preview_content = re.sub(r'<h2>Source:.*?</h2>', '', content_html)
    preview_content = re.sub(r'<p><em>URL:.*?</em></p>', '', preview_content)
    
    # Extract first heading as hero title
    hero_match = re.search(r'<h1>(.*?)</h1>', preview_content)
    hero_title = hero_match.group(1) if hero_match else page_title
    
    # Add CTA buttons after first paragraph if it's a service or location page
    if any(keyword in page_title.lower() for keyword in ['service', 'medical', 'dental', 'behavioral', 'location', 'mankato', 'shakopee']):
        preview_content = re.sub(
            r'(</p>)',
            r'\1<a href="#" class="mockup-button">Book Appointment</a><a href="#" class="mockup-button secondary">Contact Us</a>',
            preview_content,
            count=1
        )
    
    # Create wireframe
    wireframe_html = create_wireframe(page_title, content_html)
    
    return f"""
    <div class="design-preview">
        <h2>📐 Wireframe - {page_title}</h2>
        {wireframe_html}
    </div>
    """

def create_redirect_card(source_urls, new_url):
    """Create redirect mapping card for SEO"""
    if not source_urls:
        return ""
    
    redirect_html = """
    <div class="redirect-card">
        <h2>🔀 301 Redirect Mapping (SEO)</h2>
        <p style="margin-bottom: 10px; color: #666; font-size: 0.8rem;">Configure these redirects to preserve search rankings:</p>
    """
    
    for old_url in source_urls:
        # Extract path from old URL
        try:
            from urllib.parse import urlparse
            parsed = urlparse(old_url)
            old_path = parsed.path or '/'
        except:
            old_path = old_url
        
        redirect_html += f"""
        <div class="redirect-mapping">
            <span class="redirect-type">301</span>
            <strong style="font-size: 0.7rem;">From:</strong> <span class="old-url">{old_path}</span>
            <strong style="font-size: 0.7rem; margin-left: 10px;">→</strong>
            <strong style="font-size: 0.7rem;">To:</strong> <span class="new-url">/{new_url}</span>
        </div>
        """
    
    redirect_html += """
        <p style="margin-top: 10px; font-size: 0.7rem; color: #888; padding-top: 8px; border-top: 1px solid #ddd;">
            <strong>Implementation:</strong> Configure in .htaccess, nginx.conf, or hosting platform redirect manager.
        </p>
    </div>
    """
    
    return redirect_html

def create_page_html(title, content, nav_html, is_index=False, design_preview="", homepage_wireframe="", redirect_card=""):
    """Create a complete HTML page"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - ODHC Content Review</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f5f5f5;
        }}
        
        .container {{
            display: flex;
            min-height: 100vh;
        }}
        
        .sidebar {{
            width: 320px;
            background: #2c3e50;
            color: white;
            padding: 20px;
            overflow-y: auto;
            position: fixed;
            height: 100vh;
        }}
        
        .sidebar h1 {{
            font-size: 1.5rem;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #34495e;
        }}
        
        .sidebar h2 {{
            font-size: 1rem;
            margin-top: 20px;
            margin-bottom: 10px;
            color: #ecf0f1;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        .sidebar h3 {{
            font-size: 0.9rem;
            margin-top: 12px;
            margin-left: 10px;
            margin-bottom: 8px;
            color: #bdc3c7;
        }}
        
        .sidebar ul {{
            list-style: none;
        }}
        
        .sidebar li {{
            margin: 5px 0;
        }}
        
        .sidebar a {{
            color: #bdc3c7;
            text-decoration: none;
            display: block;
            padding: 8px 12px;
            border-radius: 4px;
            transition: all 0.3s;
            font-size: 0.9rem;
        }}
        
        .sidebar a:hover {{
            background: #34495e;
            color: white;
            padding-left: 16px;
        }}
        
        .sidebar .subsection {{
            margin-left: 15px;
        }}
        
        .sidebar .missing-page {{
            color: #e74c3c;
            opacity: 0.6;
            cursor: not-allowed;
            padding: 8px 12px;
            font-size: 0.9rem;
            font-style: italic;
        }}
        
        .sidebar .missing-page::after {{
            content: " (no content yet)";
            font-size: 0.75rem;
            color: #c0392b;
        }}
        
        .main-content {{
            flex: 1;
            margin-left: 320px;
            padding: 40px;
        }}
        
        .content-wrapper {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            max-width: 1800px;
            margin-bottom: 30px;
        }}
        
        .content-wrapper.three-col {{
            grid-template-columns: 1fr 1fr 1fr;
            max-width: 2400px;
        }}
        
        .footer-card {{
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            border-left: 5px solid #f39c12;
            max-width: 1800px;
        }}
        
        .redirect-card {{
            background: #f8f9fa;
            padding: 15px 20px;
            border-radius: 6px;
            box-shadow: 0 1px 4px rgba(0,0,0,0.08);
            border-left: 3px solid #16a085;
            max-width: 1800px;
            margin-top: 20px;
        }}
        
        .redirect-card h2 {{
            color: #16a085;
            font-size: 0.9rem;
            margin-bottom: 10px;
            padding-bottom: 6px;
            border-bottom: 1px solid #d0d0d0;
        }}
        
        .redirect-mapping {{
            background: white;
            padding: 10px;
            border-radius: 4px;
            margin: 8px 0;
            font-family: 'Courier New', monospace;
            font-size: 0.75rem;
            line-height: 1.4;
        }}
        
        .redirect-mapping .old-url {{
            color: #e74c3c;
            font-weight: 600;
        }}
        
        .redirect-mapping .new-url {{
            color: #27ae60;
            font-weight: 600;
        }}
        
        .redirect-mapping .redirect-type {{
            background: #16a085;
            color: white;
            padding: 2px 6px;
            border-radius: 3px;
            font-size: 0.7rem;
            font-weight: 600;
            margin-right: 8px;
        }}
        
        .content-box {{
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        .design-preview {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        .design-preview h2 {{
            font-size: 1.3rem;
            color: #2c3e50;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #3498db;
        }}
        
        .mockup-container {{
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 20px rgba(0,0,0,0.15);
        }}
        
        .mockup-header {{
            background: linear-gradient(135deg, #3a8fa8 0%, #2c7a8f 100%);
            padding: 20px;
            color: white;
        }}
        
        .mockup-logo {{
            font-size: 1.5rem;
            font-weight: bold;
            margin-bottom: 5px;
        }}
        
        .mockup-tagline {{
            font-size: 0.9rem;
            opacity: 0.9;
        }}
        
        .mockup-nav {{
            background: #2c5f7c;
            padding: 12px 20px;
            display: flex;
            gap: 20px;
            font-size: 0.85rem;
        }}
        
        .mockup-nav a {{
            color: white;
            text-decoration: none;
            opacity: 0.8;
        }}
        
        .mockup-nav a:hover {{
            opacity: 1;
        }}
        
        .mockup-content {{
            padding: 30px;
            background: linear-gradient(135deg, #f5f9fa 0%, #ffffff 100%);
            max-height: 600px;
            overflow-y: auto;
        }}
        
        .mockup-content h1 {{
            color: #2c5f7c;
            font-size: 1.8rem;
            margin-bottom: 15px;
        }}
        
        .mockup-content h2 {{
            color: #3a8fa8;
            font-size: 1.4rem;
            margin-top: 20px;
            margin-bottom: 10px;
        }}
        
        .mockup-content h3 {{
            color: #2c5f7c;
            font-size: 1.1rem;
            margin-top: 15px;
            margin-bottom: 8px;
        }}
        
        .mockup-content p {{
            color: #555;
            line-height: 1.8;
            margin-bottom: 12px;
        }}
        
        .mockup-content ul {{
            margin: 10px 0;
            padding-left: 20px;
        }}
        
        .mockup-content li {{
            color: #555;
            margin: 8px 0;
        }}
        
        .mockup-content a {{
            color: #3a8fa8;
            text-decoration: none;
            border-bottom: 1px solid #89c8d9;
        }}
        
        .mockup-content a:hover {{
            color: #2c7a8f;
            border-bottom-color: #3a8fa8;
        }}
        
        .mockup-button {{
            display: inline-block;
            background: #a8c954;
            color: white;
            padding: 10px 20px;
            border-radius: 25px;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.9rem;
            margin: 10px 5px;
            border: none;
        }}
        
        .mockup-button.secondary {{
            background: #e88679;
        }}
        
        .mockup-highlight {{
            background: #e8f4f8;
            border-left: 4px solid #3a8fa8;
            padding: 15px;
            margin: 15px 0;
            border-radius: 4px;
        }}
        
        .mockup-stats {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin: 20px 0;
        }}
        
        .mockup-stat {{
            background: linear-gradient(135deg, #3a8fa8 0%, #2c7a8f 100%);
            color: white;
            padding: 15px;
            border-radius: 8px;
            text-align: center;
        }}
        
        .mockup-stat-value {{
            font-size: 1.5rem;
            font-weight: bold;
        }}
        
        .mockup-stat-label {{
            font-size: 0.8rem;
            opacity: 0.9;
        }}
        
        .wireframe-container {{
            background: #ffffff;
            border: 2px solid #ddd;
            border-radius: 8px;
            overflow: hidden;
            margin-top: 20px;
        }}
        
        .wireframe-header {{
            background: #e0e0e0;
            padding: 15px;
            border-bottom: 2px solid #ccc;
        }}
        
        .wireframe-logo {{
            width: 120px;
            height: 30px;
            background: #999;
            margin-bottom: 5px;
        }}
        
        .wireframe-tagline {{
            width: 180px;
            height: 12px;
            background: #bbb;
        }}
        
        .wireframe-nav {{
            background: #f5f5f5;
            padding: 12px 15px;
            display: flex;
            gap: 15px;
            border-bottom: 1px solid #ddd;
        }}
        
        .wireframe-nav-item {{
            width: 60px;
            height: 14px;
            background: #aaa;
            border-radius: 2px;
        }}
        
        .wireframe-content {{
            padding: 20px;
            background: #fafafa;
        }}
        
        .wireframe-hero {{
            border: 2px dashed #999;
            padding: 30px;
            margin-bottom: 20px;
            background: #fff;
        }}
        
        .wireframe-title {{
            width: 70%;
            height: 28px;
            background: #333;
            margin-bottom: 15px;
        }}
        
        .wireframe-subtitle {{
            width: 50%;
            height: 16px;
            background: #666;
            margin-bottom: 10px;
        }}
        
        .wireframe-text {{
            width: 100%;
            height: 10px;
            background: #ccc;
            margin: 8px 0;
        }}
        
        .wireframe-text.short {{
            width: 85%;
        }}
        
        .wireframe-text.medium {{
            width: 92%;
        }}
        
        .wireframe-button {{
            display: inline-block;
            width: 140px;
            height: 38px;
            background: #999;
            border: 2px solid #666;
            margin: 10px 10px 10px 0;
            border-radius: 20px;
        }}
        
        .wireframe-section {{
            border: 1px solid #ddd;
            padding: 20px;
            margin: 15px 0;
            background: #fff;
            text-align: center;
        }}
        
        .wireframe-heading {{
            width: 40%;
            height: 20px;
            background: #555;
            margin-bottom: 12px;
        }}
        
        .wireframe-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin: 15px 0;
        }}
        
        .wireframe-card {{
            border: 2px solid #bbb;
            padding: 15px;
            background: #fff;
            min-height: 80px;
        }}
        
        .wireframe-card-title {{
            width: 70%;
            height: 14px;
            background: #666;
            margin-bottom: 10px;
        }}
        
        .wireframe-card-text {{
            width: 100%;
            height: 8px;
            background: #ddd;
            margin: 5px 0;
        }}
        
        .wireframe-image {{
            width: 100%;
            height: 120px;
            background: #e0e0e0;
            border: 2px dashed #999;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #666;
            font-size: 0.9rem;
            margin: 10px 0;
        }}
        
        .wireframe-list {{
            margin: 10px 0;
        }}
        
        .wireframe-list-item {{
            display: flex;
            align-items: center;
            margin: 8px 0;
        }}
        
        .wireframe-bullet {{
            width: 6px;
            height: 6px;
            background: #666;
            border-radius: 50%;
            margin-right: 10px;
        }}
        
        .wireframe-list-text {{
            width: 80%;
            height: 10px;
            background: #ccc;
        }}
        
        .wireframe-label {{
            font-size: 0.75rem;
            color: #666;
            margin: 5px 0;
            font-family: sans-serif;
            text-align: center;
        }}
        
        .wireframe-section-label {{
            font-size: 0.8rem;
            color: #333;
            font-weight: 600;
            margin: 10px 0 5px 0;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            text-align: center;
        }}
        
        .wireframe-icon {{
            width: 40px;
            height: 40px;
            background: #ddd;
            border-radius: 50%;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            margin: 5px;
        }}
        
        .content-box h1 {{
            color: #2c3e50;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 3px solid #3498db;
        }}
        
        .content-box h2 {{
            color: #34495e;
            margin-top: 30px;
            margin-bottom: 15px;
        }}
        
        .content-box h3 {{
            color: #555;
            margin-top: 20px;
            margin-bottom: 10px;
        }}
        
        .content-box img {{
            max-width: 100%;
            height: auto;
            margin: 20px 0;
            border-radius: 4px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        
        .content-box a {{
            color: #3498db;
            text-decoration: none;
        }}
        
        .content-box a:hover {{
            text-decoration: underline;
        }}
        
        .source-info {{
            background: #e3f2fd;
            padding: 20px;
            margin: 0 0 30px 0;
            border-radius: 6px;
            border-left: 4px solid #2196f3;
        }}
        
        .source-info h3 {{
            margin-top: 0;
            margin-bottom: 12px;
            color: #1976d2;
            font-size: 1.1rem;
        }}
        
        .source-info ul {{
            margin: 0;
            padding-left: 20px;
        }}
        
        .source-info li {{
            margin: 8px 0;
        }}
        
        .source-info a {{
            color: #1976d2;
            word-break: break-all;
            font-size: 0.95rem;
        }}
        
        .footer-card h2 {{
            color: #d68910;
            font-size: 1.3rem;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 2px solid #f39c12;
        }}
        
        .footer-card p {{
            color: #555;
            font-size: 0.95rem;
            line-height: 1.7;
            margin: 12px 0;
        }}
        
        .footer-card .copyright {{
            color: #888;
            font-size: 0.85rem;
            margin-top: 20px;
            padding-top: 15px;
            border-top: 1px solid #eee;
        }}
        
        .image-gallery {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
            gap: 20px;
            margin: 20px 0 0 0;
        }}
        
        .image-item {{
            text-align: center;
        }}
        
        .image-gallery img {{
            width: 100%;
            height: 180px;
            object-fit: cover;
            border-radius: 6px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15);
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
        }}
        
        .image-gallery img:hover {{
            transform: scale(1.05);
            box-shadow: 0 4px 12px rgba(0,0,0,0.25);
        }}
        
        .image-caption {{
            font-size: 0.75rem;
            color: #666;
            margin-top: 8px;
            word-break: break-word;
        }}
        
        .alert {{
            padding: 15px;
            margin: 20px 0;
            border-radius: 4px;
            background: #fff3cd;
            border-left: 4px solid #ffc107;
        }}
        
        @media (max-width: 768px) {{
            .sidebar {{
                width: 100%;
                position: relative;
                height: auto;
            }}
            
            .main-content {{
                margin-left: 0;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <nav class="sidebar">
            <h1>ODHC Content Review</h1>
            {nav_html}
        </nav>
        <main class="main-content">
            <div class="content-wrapper">
                <div class="content-box">
                    {content}
                </div>
                {design_preview}
            </div>
            <div class="footer-card">
                <h2>📄 Footer Content</h2>
                <p>Open Door Health Center is a Federally Qualified Health Center (FQHC). Open Door Health Center receives HHS funding and is a Health Center Program grantee under 42 U.S.C 254b, and is deemed a Public Health Service employer under 42 U.S.C. 233 (g)-(n)</p>
                <p class="copyright">© Copyright - Open Door Health Center - powered by Enfold WordPress Theme</p>
            </div>
            {redirect_card}
        </main>
    </div>
</body>
</html>"""

def create_navigation_html(file_mapping):
    """Create navigation HTML from organized structure"""
    nav_html = '<a href="index.html" style="background: #34495e; margin-bottom: 20px;">🏠 Home</a>'
    
    # Define the structure order
    nav_structure = [
        ('About', [
            'Mission, Vision, and Values',
            'Services',
            ('Locations', ['Mankato', 'Shakopee', 'School-Based Centers']),
            'Meet the Team',
            'News and Events',
            'Careers'
        ]),
        ('Patient Resources', [
            'Patient Portal',
            'Forms',
            'Financial Assistance',
            'Community Resources'
        ]),
        'Contact',
        'Donate',
        ('Footer pages Utility', [
            'Privacy Policy',
            'FAQ',
            'Annual Report'
        ])
    ]
    
    # Create reverse lookup
    file_to_html = {}
    for full_path, location in file_mapping.items():
        html_name = '-'.join([s.lower().replace(' ', '-').replace(',', '') for s in location]) + '.html'
        file_to_html[location] = (html_name, full_path)
    
    def render_nav_item(item, level=0, parent_path=()):
        html = ''
        if isinstance(item, tuple):
            section_name, subsections = item
            html += f'<h{"2" if level == 0 else "3"}>{section_name}</h{"2" if level == 0 else "3"}>'
            html += '<ul class="subsection">' if level > 0 else '<ul>'
            current_path = parent_path + (section_name,)
            for sub in subsections:
                html += render_nav_item(sub, level + 1, current_path)
            html += '</ul>'
        else:
            # It's a page name - check if we have content for it
            found = False
            
            # Special case: "Services" should link to the services overview page
            if item == "Services":
                for location, (html_name, _) in file_to_html.items():
                    if location[-1] == "Overview" and len(location) > 1 and location[-2] == "Services":
                        html += f'<li><a href="{html_name}">{item}</a></li>'
                        found = True
                        break
            else:
                for location, (html_name, _) in file_to_html.items():
                    if location[-1] == item or (len(location) == 1 and location[0] == item):
                        html += f'<li><a href="{html_name}">{item}</a></li>'
                        found = True
                        break
            
            # If not found, show as missing
            if not found:
                html += f'<li><span class="missing-page">{item}</span></li>'
        
        return html
    
    for item in nav_structure:
        nav_html += render_nav_item(item, parent_path=())
    
    return nav_html

def create_homepage_wireframe():
    """Create homepage wireframe based on content strategy"""
    wireframe = """
    <div class="design-preview">
        <h2>📐 Homepage Wireframe</h2>
        <div class="wireframe-container">
            <div class="wireframe-header">
                <div style="display: flex; justify-content: space-between; align-items: center; padding: 15px;">
                    <div>
                        <div class="wireframe-logo"></div>
                        <div class="wireframe-label">Logo + Tagline</div>
                    </div>
                    <div style="display: flex; gap: 10px;">
                        <div class="wireframe-button"></div>
                        <div class="wireframe-button"></div>
                    </div>
                </div>
            </div>
            
            <div class="wireframe-nav">
                <div class="wireframe-nav-item"></div>
                <div class="wireframe-nav-item"></div>
                <div class="wireframe-nav-item"></div>
                <div class="wireframe-nav-item"></div>
                <div class="wireframe-nav-item"></div>
            </div>
            
            <div class="wireframe-content">
                <div class="wireframe-hero">
                    <div class="wireframe-section-label">1. Hero Section</div>
                    <div style="font-size: 1.1rem; font-weight: 700; margin: 10px 0; text-align: center;">Quality Healthcare for Everyone</div>
                    <div style="font-size: 0.9rem; font-weight: 500; margin: 8px 0; text-align: center; color: #666;">Affordable medical, dental, and behavioral health care for all Southern Minnesota families</div>
                    <div style="font-size: 0.75rem; margin: 10px 0; text-align: center; line-height: 1.4;">Independent nonprofit community health center. We accept most insurance and offer sliding fee discounts for those who qualify.</div>
                    <div style="margin-top: 15px; display: flex; gap: 10px; justify-content: center;">
                        <div class="wireframe-button" style="padding: 8px 15px;">Book Appointment</div>
                        <div class="wireframe-button" style="padding: 8px 15px;">Contact Us</div>
                    </div>
                    <div style="font-size: 0.85rem; margin-top: 10px; text-align: center; font-weight: 600;">(507) 388-2120</div>
                </div>
                
                <div class="wireframe-section" style="background: #fafafa;">
                    <div class="wireframe-section-label">2. Locations (2-Column)</div>
                    <div class="wireframe-grid">
                        <div class="wireframe-card">
                            <div style="font-weight: 700; font-size: 0.9rem;">Mankato</div>
                        </div>
                        <div class="wireframe-card">
                            <div style="font-weight: 700; font-size: 0.9rem;">Shakopee</div>
                        </div>
                    </div>
                </div>
                
                <div class="wireframe-section">
                    <div class="wireframe-section-label">3. Services (3-Column)</div>
                    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px;">
                        <div class="wireframe-card">
                            <div style="font-weight: 700; font-size: 0.9rem;">Medical</div>
                        </div>
                        <div class="wireframe-card">
                            <div style="font-weight: 700; font-size: 0.9rem;">Dental</div>
                        </div>
                        <div class="wireframe-card">
                            <div style="font-weight: 700; font-size: 0.9rem;">Behavioral Health</div>
                        </div>
                    </div>
                </div>
                
                <div class="wireframe-section" style="background: #fafafa;">
                    <div class="wireframe-section-label">4. Trust Indicators (4-Column)</div>
                    <div class="wireframe-grid" style="grid-template-columns: repeat(4, 1fr);">
                        <div class="wireframe-card">
                            <div style="font-weight: 700; font-size: 0.85rem; margin-bottom: 5px;">Insurance Accepted</div>
                            <div style="font-size: 0.65rem; line-height: 1.3;">Many private plans, Minnesota Care & MA</div>
                        </div>
                        <div class="wireframe-card">
                            <div style="font-weight: 700; font-size: 0.85rem; margin-bottom: 5px;">Sliding Fee Program</div>
                            <div style="font-size: 0.65rem; line-height: 1.3;">Discounts based on income & household size</div>
                        </div>
                        <div class="wireframe-card">
                            <div style="font-weight: 700; font-size: 0.85rem; margin-bottom: 5px;">No One Turned Away</div>
                            <div style="font-size: 0.65rem; line-height: 1.3;">Regardless of ability to pay</div>
                        </div>
                        <div class="wireframe-card">
                            <div style="font-weight: 700; font-size: 0.85rem; margin-bottom: 5px;">Language Services</div>
                            <div style="font-size: 0.65rem; line-height: 1.3;">Available free of charge</div>
                        </div>
                    </div>
                </div>
                
                <div class="wireframe-section">
                    <div class="wireframe-section-label">5. Additional Services (2-Column)</div>
                    <div class="wireframe-grid">
                        <div class="wireframe-card">
                            <div style="font-weight: 700; font-size: 0.9rem;">Insurance Enrollment</div>
                        </div>
                        <div class="wireframe-card">
                            <div style="font-weight: 700; font-size: 0.9rem;">Chiropractic Care</div>
                        </div>
                    </div>
                </div>
                
                <div class="wireframe-section" style="background: #fafafa;">
                    <div class="wireframe-section-label">6. Why Choose Open Door? (4-Column)</div>
                    <div class="wireframe-grid" style="grid-template-columns: repeat(4, 1fr);">
                        <div class="wireframe-card">
                            <div style="font-weight: 700; font-size: 0.85rem; margin-bottom: 5px;">Affordable Care</div>
                            <div style="font-size: 0.65rem; line-height: 1.3;">Quality healthcare at prices you can afford</div>
                        </div>
                        <div class="wireframe-card">
                            <div style="font-weight: 700; font-size: 0.85rem; margin-bottom: 5px;">Comprehensive Services</div>
                            <div style="font-size: 0.65rem; line-height: 1.3;">Medical, dental, and behavioral health all in one place</div>
                        </div>
                        <div class="wireframe-card">
                            <div style="font-weight: 700; font-size: 0.85rem; margin-bottom: 5px;">Community-Focused</div>
                            <div style="font-size: 0.65rem; line-height: 1.3;">Independent nonprofit. We serve families—not shareholders.</div>
                        </div>
                        <div class="wireframe-card">
                            <div style="font-weight: 700; font-size: 0.85rem; margin-bottom: 5px;">Telehealth Available</div>
                            <div style="font-size: 0.65rem; line-height: 1.3;">Virtual appointments when you need them</div>
                        </div>
                    </div>
                </div>
                
                <div class="wireframe-section">
                    <div class="wireframe-section-label">7. Patient Resources (4-Column)</div>
                    <div class="wireframe-grid" style="grid-template-columns: repeat(4, 1fr);">
                        <div class="wireframe-card">
                            <div style="font-weight: 600; font-size: 0.85rem;">Portal</div>
                        </div>
                        <div class="wireframe-card">
                            <div style="font-weight: 600; font-size: 0.85rem;">Forms</div>
                        </div>
                        <div class="wireframe-card">
                            <div style="font-weight: 600; font-size: 0.85rem;">Financial</div>
                        </div>
                        <div class="wireframe-card">
                            <div style="font-weight: 600; font-size: 0.85rem;">Community</div>
                        </div>
                    </div>
                </div>
                
                <div class="wireframe-section" style="background: #e0e0e0; border-top: 3px solid #999;">
                    <div class="wireframe-section-label">8. Footer (4-Column)</div>
                    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px;">
                        <div>
                            <div class="wireframe-text" style="height: 14px; background: #999;"></div>
                        </div>
                        <div>
                            <div class="wireframe-text" style="height: 14px; background: #999;"></div>
                        </div>
                        <div>
                            <div class="wireframe-text" style="height: 14px; background: #999;"></div>
                        </div>
                        <div>
                            <div class="wireframe-text" style="height: 14px; background: #999;"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """
    return wireframe

def create_index_page(file_mapping, nav_html):
    """Create index/home page with overview"""
    content = """
    <h1>ODHC Website Content Review</h1>
    <div class="alert">
        <strong>About This Site:</strong> This is a review site showing all scraped content from odhc.org organized into your new website structure.
        Use the navigation on the left to browse through different sections. Each page shows the original source URLs and any images extracted from those pages.
    </div>
    
    <h2>New Site Structure</h2>
    <p>Content has been organized into the following sections:</p>
    
    <h3>📘 About</h3>
    <ul>
        <li>Mission, Vision, and Values</li>
        <li>Services (Medical, Dental, Behavioral Health, Insurance, Chiropractic)</li>
        <li>Locations (Mankato, Shakopee, School-Based Centers)</li>
        <li>Meet the Team</li>
        <li>News and Events</li>
        <li>Careers</li>
    </ul>
    
    <h3>📋 Patient Resources</h3>
    <ul>
        <li>Patient Portal</li>
        <li>Forms</li>
        <li>Financial Assistance</li>
        <li>Community Resources</li>
    </ul>
    
    <h3>📞 Contact & Donate</h3>
    
    <h3>📄 Footer Pages</h3>
    <ul>
        <li>Privacy Policy</li>
        <li>FAQ</li>
        <li>Annual Report</li>
    </ul>
    
    <h2 style="margin-top: 40px;">🎨 Design System</h2>
    <div style="background: linear-gradient(135deg, #f5f9fa 0%, #e8f4f8 100%); padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        <h3 style="color: #2c5f7c; margin-top: 0;">Community Wellness Hub Aesthetic</h3>
        
        <p style="color: #2c5f7c; font-size: 0.95rem; margin: 15px 0;">
            <strong>Color Palette:</strong>
        </p>
        <div style="display: flex; gap: 10px; margin: 20px 0;">
            <div style="width: 50px; height: 50px; border-radius: 50%; background: #3a8fa8;" title="Primary Teal"></div>
            <div style="width: 50px; height: 50px; border-radius: 50%; background: #a8c954;" title="Accent Green"></div>
            <div style="width: 50px; height: 50px; border-radius: 50%; background: #e88679;" title="Coral"></div>
            <div style="width: 50px; height: 50px; border-radius: 50%; background: #89c8d9;" title="Light Blue"></div>
        </div>
        <ul style="color: #2c5f7c; font-size: 0.9rem;">
            <li>Primary Teal: #3a8fa8</li>
            <li>Accent Green: #a8c954</li>
            <li>Coral: #e88679</li>
            <li>Light Blue: #89c8d9</li>
        </ul>
        
        <p style="font-size: 0.9rem; color: #666; margin-top: 20px;">
            <em>Warm, welcoming colors with a modern, clean interface focused on accessibility and family-friendly appeal.</em>
        </p>
    </div>
    
    <h2 style="margin-top: 40px;">📋 Content Strategy</h2>
    <div style="background: #f8f9fa; padding: 20px; border-radius: 8px; border: 2px solid #3498db;">
        <h3 style="margin-top: 0; color: #2c3e50;">Strategic Approach</h3>
        <p style="font-size: 0.9rem; line-height: 1.6;">
            <strong>Primary Goal:</strong> Get visitors to book appointment or call (507) 388-2120
        </p>
        <p style="font-size: 0.9rem; line-height: 1.6;">
            <strong>Key Message:</strong> Affordable, comprehensive healthcare for all Southern Minnesota families
        </p>
        <p style="font-size: 0.9rem; line-height: 1.6;">
            <strong>Differentiator:</strong> FQHC with sliding fee program + all services under one roof
        </p>
        <p style="font-size: 0.85rem; color: #666; margin-top: 15px; padding-top: 15px; border-top: 1px solid #ddd;">
            See full content strategy document: <strong>HOMEPAGE-CONTENT-STRATEGY.md</strong>
        </p>
    </div>
    """
    
    # Create homepage wireframe
    homepage_wireframe = create_homepage_wireframe()
    
    return create_page_html('Home', content, nav_html, is_index=True, design_preview=homepage_wireframe, redirect_card="")

def generate_review_site():
    """Generate the complete review website"""
    print("\nGenerating review website...")
    
    # Create output directory
    output_dir = 'review_site'
    Path(output_dir).mkdir(exist_ok=True)
    
    # Get all markdown files
    md_files = get_all_markdown_files()
    
    if not md_files:
        print("No markdown files found. Run the scraper first.")
        return
    
    # Organize files by new structure
    file_mapping = organize_by_new_structure(md_files)
    
    # Create navigation
    nav_html = create_navigation_html(file_mapping)
    
    # Create index page
    index_html = create_index_page(file_mapping, nav_html)
    with open(os.path.join(output_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(index_html)
    print(f"  ✓ Created: index.html")
    
    # Create individual pages
    for full_path, location in file_mapping.items():
        # Convert markdown to HTML
        content_html, source_urls, images, md_content = convert_md_to_html(full_path)
        
        # Add source info and images at the top
        extra_content = ""
        
        if source_urls:
            extra_content += '<div class="source-info">'
            extra_content += '<h3>📄 Original Source Page(s):</h3>'
            extra_content += '<ul>'
            for url in source_urls:
                extra_content += f'<li><a href="{url}" target="_blank" rel="noopener">{url}</a></li>'
            extra_content += '</ul>'
            extra_content += '</div>'
        
        if images:
            extra_content += '<div class="source-info">'
            extra_content += f'<h3>🖼️ Images Extracted ({len(images)} total):</h3>'
            extra_content += '<div class="image-gallery">'
            for img in images:
                # Get just the filename for caption
                img_name = os.path.basename(img)
                extra_content += f'<div class="image-item"><a href="{img}" target="_blank"><img src="{img}" alt="{img_name}" title="Click to view full size"></a><div class="image-caption">{img_name}</div></div>'
            extra_content += '</div>'
            extra_content += '</div>'
        
        # Combine extra content with main content
        full_content = extra_content + content_html
        
        # Create page title
        page_title = ' > '.join(location)
        
        # Create design preview
        design_preview = create_design_preview(content_html, page_title)
        
        # Save HTML file
        html_filename = '-'.join([s.lower().replace(' ', '-').replace(',', '') for s in location]) + '.html'
        
        # Create redirect card
        redirect_card = create_redirect_card(source_urls, html_filename)
        
        # Create full page HTML
        page_html = create_page_html(page_title, full_content, nav_html, design_preview=design_preview, redirect_card=redirect_card)
        output_path = os.path.join(output_dir, html_filename)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(page_html)
        
        print(f"  ✓ Created: {html_filename}")
    
    print(f"\n✅ Review site generated successfully!")
    print(f"📂 Open {output_dir}/index.html in your browser to view.")

if __name__ == '__main__':
    generate_review_site()

# ODHC Website Content Scraper

This tool scrapes content from https://odhc.org and organizes it into a new site structure for redesign planning.

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Run the complete scraping process:
```bash
python scraper.py
```

This will:
1. Scrape all content from odhc.org
2. Download all images and PDFs
3. Organize content into markdown files based on the new site structure
4. Generate a simple HTML review website

### View the results:
1. Open `review_site/index.html` in your web browser
2. Navigate through the organized content
3. Review the content mapping report at `content_report.txt`

## Output Structure

```
scraped_content/          # Organized markdown files
├── about/
│   ├── mission-vision-values.md
│   ├── services/
│   ├── locations/
│   └── team.md
├── patient-resources/
├── contact.md
└── donate.md

assets/                   # Downloaded media
├── images/
└── pdfs/

review_site/             # HTML preview site
└── index.html
```

## Configuration

Edit `config.json` to:
- Modify page mappings
- Adjust scraper settings
- Change output directories

## Deploying to Vercel

The `review_site/` folder is set up for static deployment on Vercel.

1. Push this repo to GitHub and [import the project in Vercel](https://vercel.com/new).
2. In **Project Settings → General → Root Directory**, set **Root Directory** to `review_site` and save.
3. Deploy. The site will be served with clean URLs (e.g. `/about-overview` instead of `/about-overview.html`).

The `review_site` directory includes a copy of `assets/` (images and PDFs) and a `vercel.json` that enables `cleanUrls`.

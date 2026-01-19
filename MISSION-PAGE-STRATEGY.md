# Strategic Wireframe Plan: Mission, Vision, and Values Page

## Overview
This document outlines the strategy and task list for creating a strategized content wireframe for the "Mission, Vision, and Values" page, based on the successful approach used for the homepage.

---

## What We Did for the Homepage (Process Summary)

### 1. **Layout Transformation**
- **From:** 2-column layout (Scraped Content | Wireframe)
- **To:** 3-column layout (Scraped Content | Wireframe | Strategized Content)
- **Grid:** `grid-template-columns: 1fr 1fr 1.8fr` (strategized content wider to accommodate more text)

### 2. **CSS Styling Approach**
- Created `.strategized-content` class with **black & white wireframe aesthetic**
  - White background, gray borders (`border: 2px solid #ddd`)
  - No shadows, gradients, or brand colors
  - Simple, clean typography
- Added wireframe-specific styles:
  - `.bw-header`, `.bw-nav`, `.bw-logo`, `.bw-icon` (header/nav mock)
  - `.bw-slideshow`, `.bw-arrow`, `.bw-dot` (slideshow frame)
  - `.bw-box`, `.bw-pill` (content containers)
  - `.service-card`, `.cta-button` (gray, minimal styling)

### 3. **Content Strategy**
- **Referenced:** `HOMEPAGE-CONTENT-STRATEGY.md` for voice, tone, and messaging principles
- **Source Material:** Scraped content markdown files (`scraped_content/`) for factual information
- **Approach:**
  - Rewrote scraped content to be **patient-focused** and **benefit-driven**
  - Used clear, concise language (avoid jargon)
  - Added CTAs where appropriate
  - Structured content for **scannability** (short paragraphs, bullet points, headings)
  - Filled gaps where scraped content was missing

### 4. **Homepage Structure Created**
The strategized content card included:
1. **Header/Nav Mock** (B/W wireframe style with logo, phone icon)
2. **Hero/Slideshow Section** (Shakopee announcement, CTAs, slideshow frame)
3. **Locations** (2-column grid: Mankato, Shakopee)
4. **Services** (3-column grid: Medical, Dental, Behavioral Health)
5. **Trust Indicators** (4-column grid: Insurance, Sliding Fee, No One Turned Away, Language Services)
6. **Additional Services** (2-column grid: Insurance Enrollment, Chiropractic Care)
7. **Why Choose Open Door?** (4-column grid: Affordable, Comprehensive, Community-Focused, Telehealth)
8. **Patient Resources** (Single box with inline links: Portal, Forms, Financial, Community)
9. **Donate** (Single box with CTA)
10. **Footer** (Single box with 4-column grid: About, Locations, Patient Resources, Contact & More)

### 5. **Technical Implementation**
- Updated `<style>` section with new CSS classes
- Inserted `<div class="strategized-content">...</div>` as third column
- Used semantic HTML (`h2`, `h3`, `h4`, `p`, `ul`, `li`, `a`)
- Applied inline styles sparingly for fine-tuning spacing/layout

---

## Mission, Vision, and Values Page: Content Strategy

### Page Purpose
This page should:
- Communicate ODHC's **core values** and **organizational mission**
- Build **trust and credibility** by showing commitment to community
- Inspire **confidence** in prospective patients that ODHC aligns with their values
- Provide **clear next steps** (CTAs to book appointment, learn about services, or contact)

### Key Messaging Pillars
1. **Mission:** Provide accessible, affordable, quality healthcare to all
2. **Vision:** A healthier Southern Minnesota where healthcare is a right, not a privilege
3. **Values:** Community, compassion, equity, excellence, integrity
4. **Patient-Centered:** Everything we do is for the well-being of our patients

### Target Audience
- Prospective patients researching ODHC before first visit
- Community members evaluating whether ODHC aligns with their values
- Potential partners, donors, or employees

---

## Proposed Strategized Content Structure for Mission/Vision/Values Page

### Section 1: Header/Nav Mock
- **Same as homepage:** B/W wireframe header with logo box, phone icon, and nav pills

### Section 2: Hero Section - "Who We Are"
- **Headline:** "Healthcare Rooted in Community"
- **Subheadline:** "Open Door Health Center exists to serve Southern Minnesota families with accessible, affordable, quality care—no matter your circumstances."
- **CTA Buttons:**
  - "Book Appointment"
  - "Learn About Our Services"
- **Frame/Box:** Place in a subtle gray box to mimic hero section

### Section 3: Mission Statement
- **Headline:** "Our Mission"
- **Content:** (Rewritten from scraped content)
  - "We provide comprehensive, patient-centered healthcare—medical, dental, and behavioral health—to all people in Southern Minnesota, regardless of ability to pay."
- **Visual:** Single box/card with left border accent

### Section 4: Vision Statement
- **Headline:** "Our Vision"
- **Content:** (Rewritten)
  - "A healthier Southern Minnesota where everyone has access to quality healthcare and can live their best life."
- **Visual:** Single box/card with left border accent

### Section 5: Core Values (Grid)
- **Headline:** "Our Values"
- **Layout:** 3-column or 4-column grid of value cards
- **Values to Include:**
  1. **Community-Focused** - "We serve families, not shareholders."
  2. **Compassionate Care** - "Every patient is treated with dignity and respect."
  3. **Equity & Access** - "Healthcare is a right. We never turn anyone away."
  4. **Excellence** - "Quality care you can trust."
  5. **Integrity** - "Transparent, honest, and accountable."
  6. **(Optional) Collaboration** - "We partner with the community to improve health."

### Section 6: What This Means for You
- **Headline:** "What This Means for You"
- **Content:** (Benefit-focused translation of values into patient experience)
  - "No matter your income, insurance status, or background, you'll receive the same high-quality care. We accept most insurance, offer sliding fee discounts, and provide language assistance services at no charge."
- **CTA:** "Learn About Financial Assistance"

### Section 7: Our Commitment
- **Headline:** "Our Commitment to Southern Minnesota"
- **Content:** (Quick facts/stats)
  - "As an independent nonprofit community health center, we reinvest every dollar back into care for our patients."
  - "We're a Federally Qualified Health Center (FQHC), meeting rigorous federal standards for quality and access."
  - "We serve patients in Mankato, Shakopee, and school-based centers across the region."
- **Visual:** 2-column grid or single box with bullet points

### Section 8: Footer (Same as Homepage)
- **Single box with 4-column grid:** About, Locations, Patient Resources, Contact & More

---

## Task List for Implementation

### Phase 1: CSS Setup
- [ ] **Task 1.1:** Update `.content-wrapper` grid to `1fr 1fr 1.8fr` (3-column layout)
- [ ] **Task 1.2:** Copy `.strategized-content` CSS class and all related B/W wireframe styles from `index.html` to `about-mission-vision-and-values.html`
- [ ] **Task 1.3:** Ensure all utility classes are present (`.service-card`, `.service-grid`, `.cta-button`, `.bw-header`, `.bw-nav`, `.bw-box`, `.bw-slideshow`, etc.)

### Phase 2: Content Research & Analysis
- [ ] **Task 2.1:** Read scraped content from `about-mission-vision-and-values.html` left column (lines 702-724)
- [ ] **Task 2.2:** Extract key facts, mission/vision statements, values, and messaging
- [ ] **Task 2.3:** Identify gaps where content needs to be written from scratch
- [ ] **Task 2.4:** Review `HOMEPAGE-CONTENT-STRATEGY.md` for tone, voice, and messaging guidelines

### Phase 3: Content Writing
- [ ] **Task 3.1:** Write Hero Section copy ("Who We Are")
- [ ] **Task 3.2:** Rewrite Mission Statement (patient-focused, benefit-driven)
- [ ] **Task 3.3:** Rewrite Vision Statement (aspirational, community-focused)
- [ ] **Task 3.4:** Draft Core Values section (3-4 values with short descriptions)
- [ ] **Task 3.5:** Write "What This Means for You" section (translate values into patient benefits)
- [ ] **Task 3.6:** Write "Our Commitment" section (trust-building facts/stats)
- [ ] **Task 3.7:** Adapt footer content from homepage (update links if needed)

### Phase 4: HTML Structure
- [ ] **Task 4.1:** Insert `<div class="strategized-content">` as third column in `.content-wrapper`
- [ ] **Task 4.2:** Add section heading: `<h2>Strategized Content <span class="optimized-badge">Optimized</span></h2>`
- [ ] **Task 4.3:** Copy header/nav mock from homepage (`.bw-header`, `.bw-nav`)
- [ ] **Task 4.4:** Build Hero Section with headline, subheadline, CTAs (in `.bw-box` or similar)
- [ ] **Task 4.5:** Build Mission Statement section (single card with `<h3>`, `<p>`)
- [ ] **Task 4.6:** Build Vision Statement section (single card with `<h3>`, `<p>`)
- [ ] **Task 4.7:** Build Core Values grid (`.service-grid` with 3-4 `.service-card` elements)
- [ ] **Task 4.8:** Build "What This Means for You" section (single card with CTA)
- [ ] **Task 4.9:** Build "Our Commitment" section (2-column grid or single box with bullets)
- [ ] **Task 4.10:** Copy Footer section from homepage (single box, 4-column grid)

### Phase 5: Refinement & QA
- [ ] **Task 5.1:** Review all content for tone consistency (warm, welcoming, patient-focused)
- [ ] **Task 5.2:** Check for clear CTAs in appropriate sections
- [ ] **Task 5.3:** Verify all links in footer are correct and active
- [ ] **Task 5.4:** Ensure B/W wireframe styling is consistent (no brand colors/gradients)
- [ ] **Task 5.5:** Test layout responsiveness (if applicable)
- [ ] **Task 5.6:** Run linter check for HTML/CSS errors
- [ ] **Task 5.7:** Update sidebar navigation if needed (confirm "Mission, Vision, and Values" link is correct)

### Phase 6: Documentation
- [ ] **Task 6.1:** Add notes in this document about what worked well and what to adjust for future pages
- [ ] **Task 6.2:** Create a reusable template or style guide based on homepage + mission page patterns

---

## Key Considerations

### Content Writing Guidelines
- **Voice:** Professional yet approachable, warm, welcoming
- **Tone:** Confident, compassionate, patient-focused
- **Length:** Short paragraphs (2-3 sentences max), scannable
- **Language:** Plain language, avoid medical jargon
- **CTAs:** Clear, action-oriented ("Book Appointment", "Learn More", "Contact Us")
- **Focus:** Benefits to the patient, not organizational features

### Visual Design Guidelines
- **Color Palette:** Black, white, grays (no brand colors in wireframe card)
- **Borders:** 2px solid gray (`#ddd` or similar)
- **Buttons:** Gray background, gray border, no hover effects (static wireframe look)
- **Typography:**
  - `h2`: Section title (larger, centered, letter-spacing)
  - `h3`: Subsection headings (centered, larger font)
  - `h4`: Card titles
  - `p`: Body text (readable line-height)
- **Spacing:** Consistent margins/padding (use `margin: 18px 0`, `padding: 25px`, etc.)
- **Grid Layouts:** Use `.service-grid` with `grid-template-columns` for multi-column sections

### Reusability
- This process can be replicated for **all other pages** in the site:
  - Service pages (Medical, Dental, Behavioral Health, etc.)
  - Location pages (Mankato, Shakopee, School-Based Centers)
  - Patient Resources pages (Portal, Forms, Financial Assistance, etc.)
  - Contact, Donate, Careers, etc.
- Create a **master CSS file** or **template** to streamline future implementations

---

## Success Metrics

### Content Quality
- ✓ Mission/vision statements are clear and compelling
- ✓ Values are translated into patient benefits
- ✓ CTAs are prominent and action-oriented
- ✓ Tone is warm, welcoming, and patient-focused

### Visual Quality
- ✓ B/W wireframe aesthetic is consistent with homepage
- ✓ Layout is clean, scannable, and well-organized
- ✓ Typography hierarchy is clear (h2 > h3 > h4 > p)
- ✓ No linter errors or broken links

### User Experience
- ✓ Page clearly answers "What does ODHC stand for?"
- ✓ Prospective patients feel confident in ODHC's values and commitment
- ✓ Next steps (booking, learning, contacting) are obvious and easy

---

## Next Steps

1. **Review this plan** with the team to confirm structure and messaging approach
2. **Execute Phase 1-5 tasks** systematically
3. **Document lessons learned** for future page implementations
4. **Scale to other pages** using this template as a guide

---

## Notes & Observations

*(To be filled in during/after implementation)*

- What worked well:
- What to adjust:
- Time estimate for similar pages:
- Reusable components identified:

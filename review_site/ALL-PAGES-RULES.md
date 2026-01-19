# ALL PAGES RULES - MUST FOLLOW EVERY TIME

## Rule 1: THREE-COLUMN LAYOUT STRUCTURE

**EVERY page MUST use this exact HTML structure:**

```html
<main class="main-content">
    <div class="content-wrapper">
        
        <!-- COLUMN 1: Original Content -->
        <div class="content-box">
            <!-- Original scraped content here -->
        </div>
        
        <!-- COLUMN 2: Design Preview/Wireframe -->
        <div class="design-preview">
            <!-- Wireframe mockup here -->
        </div>
        
        <!-- COLUMN 3: Strategized Content -->
        <div class="strategized-content">
            <!-- SEE RULE 3 FOR REQUIRED CONTENT -->
        </div>
        
    </div> <!-- CLOSES AFTER ALL 3 COLUMNS! -->
    
    <!-- Footer Card - OUTSIDE wrapper, full width -->
    <div class="footer-card">
        <h2>📄 Footer Content</h2>
        <p>Open Door Health Center is a Federally Qualified Health Center...</p>
        <p class="copyright">© Copyright - Open Door Health Center...</p>
    </div>
    
</main>
```

## Rule 2: CSS GRID CONFIGURATION

```css
.content-wrapper {
    display: grid;
    grid-template-columns: 1fr 1fr 1.8fr;  /* NOT 1fr 1fr 1fr! */
    gap: 30px;
    max-width: 2400px;
    margin-bottom: 30px;
}
```

## Rule 3: STRATEGIZED CONTENT MUST INCLUDE B/W HEADER & FOOTER

**EVERY strategized-content section MUST start with:**

1. **B/W Header Wireframe** (bw-header)
2. **B/W Navigation Wireframe** (bw-nav)  
3. **B/W Slideshow/Hero Section** (bw-slideshow)
4. **Page-specific content sections**
5. **Footer Wireframe** (4-column grid inside service-card)

### REQUIRED STRUCTURE:

```html
<div class="strategized-content">
    <h2>
        Strategized Content
                    <!-- (No "Optimized" badge) -->
    </h2>

    <!-- REQUIRED: B/W Header -->
    <div class="bw-header" style="margin: 18px 0;">
        <div class="bw-header-row" aria-hidden="true">
            <div class="bw-logo">LOGO</div>
            <div class="bw-box" style="min-width: 220px;">OPEN DOOR HEALTH CENTER</div>
            <div class="bw-icon" title="Phone" aria-label="Phone">☎</div>
            <div style="flex: 1;"></div>
            <div class="bw-pill">Portal Login</div>
            <div class="bw-pill alt">Pay My Bill</div>
        </div>
    </div>

    <!-- REQUIRED: B/W Navigation -->
    <div class="bw-nav" style="margin: 0 0 22px 0;">
        <div class="bw-nav-shell" aria-hidden="true">
            <div class="bw-nav-item">About</div>
            <div class="bw-nav-item">Locations</div>
            <div class="bw-nav-item">Patient Resources</div>
            <div class="bw-nav-item">Contact</div>
            <div class="bw-nav-item">Donate</div>
            <div class="bw-nav-search">
                <div class="bw-search">Search…</div>
            </div>
        </div>
    </div>
    
    <!-- REQUIRED: Hero/Slideshow Section -->
    <div class="bw-slideshow">
        <h3 style="margin-top: 0;">[Page-specific headline]</h3>
        <p><strong>[Page-specific intro]</strong></p>
        <p>[Page-specific description]</p>
        
        <div style="text-align: center; margin: 18px 0 6px 0;">
            <a href="#" class="cta-button">Schedule Appointment</a>
            <a href="#" class="cta-button secondary">Contact Us</a>
        </div>

        <div class="bw-slideshow-controls" aria-hidden="true">
            <div class="bw-arrow">‹</div>
            <div class="bw-dots">
                <div class="bw-dot active"></div>
                <div class="bw-dot"></div>
                <div class="bw-dot"></div>
            </div>
            <div class="bw-arrow">›</div>
        </div>
    </div>
    
    <!-- Page-specific content sections go here -->
    
    <!-- REQUIRED: Footer -->
    <h3>Footer</h3>
    <div class="service-card" style="padding: 25px;">
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px;">
            <div>
                <h4>About</h4>
                <div style="text-align: left; font-size: 0.85rem; line-height: 1.6;">
                    <a href="about-mission-vision-and-values.html">Mission, Vision, and Values</a><br>
                    <a href="about-services-overview.html">Services</a><br>
                    <a href="about-meet-the-team.html">Meet the Team</a><br>
                    <a href="about-news-and-events.html">News and Events</a><br>
                </div>
            </div>
            <div>
                <h4>Locations</h4>
                <div style="text-align: left; font-size: 0.85rem; line-height: 1.6;">
                    <a href="about-locations-mankato.html">Mankato</a><br>
                    <a href="about-locations-shakopee.html">Shakopee</a><br>
                    <a href="about-locations-school-based-centers.html">School-Based Centers</a>
                </div>
            </div>
            <div>
                <h4>Patient Resources</h4>
                <div style="text-align: left; font-size: 0.85rem; line-height: 1.6;">
                    <a href="patient-resources-patient-portal.html">Patient Portal</a><br>
                    <a href="patient-resources-forms.html">Forms</a><br>
                    <a href="patient-resources-financial-assistance.html">Financial Assistance</a><br>
                    <a href="patient-resources-community-resources.html">Community Resources</a>
                </div>
            </div>
            <div>
                <h4>Contact &amp; More</h4>
                <div style="text-align: left; font-size: 0.85rem; line-height: 1.6;">
                    <a href="contact.html">Contact</a><br>
                    <a href="donate.html">Donate</a><br>
                    <a href="about-careers.html">Careers</a><br>
                    <a href="footer-pages-privacy-policy.html">Privacy Policy</a><br>
                    <a href="footer-pages-faq.html">FAQ</a><br>
                    <a href="footer-pages-annual-report.html">Annual Report</a>
                </div>
            </div>
        </div>
    </div>
</div>
```

## Rule 4: BLACK AND WHITE WIREFRAME STYLING

**NO COLORS ALLOWED! Everything must be black, white, and gray.**

### CSS Requirements:

```css
.strategized-content {
    background: #ffffff;           /* White - NOT gradients */
    border: 2px solid #ddd;        /* Gray border */
    box-shadow: none;              /* NO shadows */
}

.strategized-content h2 {
    color: #333;                   /* Dark gray */
    border-bottom: 2px solid #ccc; /* Gray border */
}

.strategized-content h3 {
    color: #333;                   /* Dark gray */
    text-align: center;            /* Centered */
}

.strategized-content h4 {
    color: #333;                   /* Dark gray */
}

.cta-button {
    background: #999;              /* Gray */
    color: white;
    border: 2px solid #666;
    box-shadow: none;
    transition: none;
}

.cta-button:hover {
    background: #999;              /* NO color change */
    box-shadow: none;
    transform: none;
}

.phone-highlight {
    color: #333;                   /* Dark gray */
    background: #f5f5f5;           /* Light gray */
    border: 1px solid #ddd;
}

.trust-badge {
    background: #f5f5f5;
    border-left: 4px solid #999;   /* Gray */
}

.optimized-badge {
    background: #999;              /* Gray */
    color: white;
}

.service-card {
    background: white;
    border: 2px solid #bbb;        /* Gray */
    transition: none;
}

.service-card:hover {
    border-color: #bbb;            /* NO change */
    box-shadow: none;
}

.strategized-content li:before {
    content: "•";                  /* Bullet - NOT checkmark */
    color: #666;                   /* Gray - NOT green */
}
```

## Rule 5: REQUIRED CSS CLASSES FOR B/W WIREFRAMES

**All pages MUST include these CSS classes:**

```css
/* B/W Header Wireframe */
.bw-header { }
.bw-header-row { }
.bw-logo { }
.bw-box { }
.bw-icon { }
.bw-pill { }

/* B/W Navigation */
.bw-nav { }
.bw-nav-shell { }
.bw-nav-item { }
.bw-nav-search { }
.bw-search { }

/* B/W Slideshow */
.bw-slideshow { }
.bw-slideshow-controls { }
.bw-arrow { }
.bw-dots { }
.bw-dot { }

/* Service Cards */
.service-grid { }
.service-card { }
```

## Rule 6: REFERENCE FILES

**ALWAYS use these as templates:**
- ✅ `index.html` (homepage)
- ✅ `about-services-overview.html` (services page)

**When in doubt, copy from these files!**

---

## COMMON MISTAKES TO AVOID

❌ Closing content-wrapper before strategized-content
❌ Using colored styling (green, blue, teal)
❌ Using gradients or shadows
❌ Missing B/W header wireframe
❌ Missing B/W navigation wireframe  
❌ Missing footer with 4-column links
❌ Wrong grid columns (1fr 1fr 1fr instead of 1fr 1fr 1.8fr)
❌ Using checkmarks (✓) instead of bullets (•)
❌ Using animations or transitions

---

**Created: January 15, 2026**  
**Last Updated: January 15, 2026**

# LAYOUT STRUCTURE REFERENCE - CRITICAL

## ⚠️ IMPORTANT: Three-Column Layout Structure

**All review site pages MUST follow this exact structure.**

### CORRECT Structure (3 columns in one row):

```html
<main class="main-content">
    <div class="content-wrapper">
        
        <!-- COLUMN 1: Original Content -->
        <div class="content-box">
            <!-- Page content here -->
        </div>
        
        <!-- COLUMN 2: Design Preview/Wireframe -->
        <div class="design-preview">
            <!-- Wireframe content here -->
        </div>
        
        <!-- COLUMN 3: Strategized Content -->
        <div class="strategized-content">
            <!-- Strategized content here -->
        </div>
        
    </div> <!-- content-wrapper CLOSES HERE after all 3 columns -->
    
    <!-- Footer Card - OUTSIDE content-wrapper, full width -->
    <div class="footer-card">
        <!-- Footer content -->
    </div>
    
</main>
```

### ❌ WRONG Structure (strategized-content full width on bottom):

```html
<main class="main-content">
    <div class="content-wrapper">
        <div class="content-box">...</div>
        <div class="design-preview">...</div>
    </div> <!-- DON'T CLOSE content-wrapper HERE! -->
    
    <div class="strategized-content">...</div> <!-- This will be full width! -->
</main>
```

## CSS Grid Configuration

The `.content-wrapper` uses this grid:
```css
.content-wrapper {
    display: grid;
    grid-template-columns: 1fr 1fr 1.8fr;
    gap: 30px;
}
```

This creates three columns where:
- Column 1 (content-box): 1 fraction
- Column 2 (design-preview): 1 fraction  
- Column 3 (strategized-content): 1.8 fractions (wider)

## Key Points

1. **All three sections MUST be inside `content-wrapper`**
2. **The closing `</div>` for `content-wrapper` comes AFTER `strategized-content`**
3. **Only the `footer-card` is outside and full width**
4. **The indentation pattern matches the homepage (index.html)**

## BLACK AND WHITE WIREFRAME STYLING - CRITICAL

**ALL pages must use BLACK AND WHITE wireframe styling - NO COLORS!**

### ✅ CORRECT Styling (Black & White):

```css
.strategized-content {
    background: #ffffff;           /* White background */
    box-shadow: none;              /* NO shadow */
    border: 2px solid #ddd;        /* Gray border */
}

.strategized-content h2 {
    color: #333;                   /* Dark gray */
    border-bottom: 2px solid #ccc; /* Gray border */
}

.strategized-content h3 {
    color: #333;                   /* Dark gray */
}

.cta-button {
    background: #999;              /* Gray background */
    color: white;
    border: 2px solid #666;        /* Gray border */
    box-shadow: none;              /* NO shadow */
    transition: none;              /* NO animations */
}

.phone-highlight {
    color: #333;                   /* Dark gray */
    background: #f5f5f5;           /* Light gray */
    border: 1px solid #ddd;        /* Gray border */
}

.trust-badge {
    background: #f5f5f5;           /* Light gray */
    border-left: 4px solid #999;   /* Gray border */
}

.optimized-badge {
    background: #999;              /* Gray background */
}

.strategized-content li:before {
    content: "•";                  /* Bullet, not checkmark */
    color: #666;                   /* Gray, not green */
}
```

### ❌ WRONG Styling (Colored):

```css
/* DON'T USE THESE! */
background: linear-gradient(135deg, #f5f9fa 0%, #ffffff 100%); /* ❌ No gradients */
border-left: 5px solid #a8c954;  /* ❌ No green */
color: #2c5f7c;                  /* ❌ No teal */
color: #3a8fa8;                  /* ❌ No blue */
box-shadow: 0 2px 10px rgba(...);/* ❌ No shadows */
content: "✓";                    /* ❌ No checkmarks */
color: #a8c954;                  /* ❌ No green */
```

## Reference Files

- ✅ **Correct Example**: `index.html` (homepage)
- ✅ **Correct Example**: `about-services-overview.html` (after fix on Jan 15, 2026)

---

**Created: January 15, 2026**  
**Reason: Repeated issue with strategized-content being placed outside content-wrapper**

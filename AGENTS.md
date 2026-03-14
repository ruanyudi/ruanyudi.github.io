# AGENTS.md - Project Guide for AI Coding Agents

> This file contains essential information about the project structure, technology stack, and development conventions for AI coding agents.

## Project Overview

This is **Yudi Ruan's Personal Academic Homepage** (阮宇迪的个人学术主页), a static portfolio website showcasing research, projects, experience, and awards in AI, Vision-Language Models (VLM), Embodied AI, and RAG systems.

The website is hosted on **GitHub Pages** with automated deployment to an **Aliyun (Alibaba Cloud)** server.

### Key URLs
- Live Site: https://ruanyudi.github.io (or custom domain via Aliyun)
- Repository: GitHub repository with GitHub Pages enabled

## Technology Stack

### Frontend
- **HTML5** - Semantic markup with sections for different content areas
- **CSS3** - Responsive styling with media queries
  - Lato font family from Google Fonts
  - CSS variables for theming (`--accent`, `--text-main`, etc.)
  - Flexbox layouts
- **JavaScript (Vanilla)** - No frameworks, native browser APIs only
  - Network Information API for adaptive loading
  - LocalStorage for user preferences
  - Performance API for bandwidth testing
  - CSS animations for photo wall scrolling

### Backend/Utilities (Python)
- **Python 3.10+** for utility scripts
- **Playwright** (`>=1.40.0`) - Browser automation for PDF export
- **WeasyPrint** (`>=60.0`) - Alternative HTML-to-PDF conversion
- **PIL (Pillow)** - Image compression utilities
- **socket** - TCP client for deployment signaling

### Deployment & CI/CD
- **GitHub Actions** - Automated deployment workflow
- **GitHub Pages** - Static site hosting
- **Aliyun Server** - Production deployment target

## Project Structure

```
ruanyudi.github.io/
├── index.html                    # Entry point with network detection
├── main.html                     # Main content page (~2650 lines)
├── README.md                     # (Currently empty)
├── requirements.txt              # Python dependencies
│
├── css/
│   ├── desktop.css               # Styles for screen width > 600px
│   └── mobile.css                # Styles for screen width <= 600px
│
├── src/
│   ├── images/                   # Image assets
│   │   ├── highlights/           # Photo wall images
│   │   ├── profile.jpg           # Profile photo
│   │   ├── cqjtu_logo.webp       # University logos
│   │   ├── cortex_logo.png       # Company logos
│   │   ├── *.gif                 # Project demo GIFs
│   │   └── *.png                 # Project screenshots
│   ├── matrix-wall.web.mp4       # Background video
│   └── ryd_cv.pdf                # CV PDF
│
├── .github/
│   └── workflows/
│       └── aliyun-deploy.yml     # GitHub Actions deployment workflow
│
├── deploy_aliyun.py              # TCP client to trigger remote deployment
├── export_to_pdf.py              # PDF export using Playwright
├── export_to_pdf_weasyprint.py   # PDF export using WeasyPrint
└── jpg_comp.py                   # Image compression utility
```

## Main Content Sections (main.html)

The main page contains the following sections (in order):

1. **Top** (`#Top`) - Header with profile info and social links
2. **RealtimeAvatar** (`#RealtimeAvatar`) - Digital human demo section
3. **PhotoWall** (`#PhotoWall`) - Auto-scrolling image gallery
4. **Awards** (`#Awards`) - Awards and honors timeline
5. **ResearchExperience** (`#ResearchExperience`) - Work experience timeline
6. **Research** (`#Research`) - Research interests with filter buttons
7. **Paper** (`#paper`) - Publications with filtering by category
8. **Projects** (`#Projects`) - Project showcases with GIF demos
9. **Friends** (`#Friends`) - Links to collaborators/friends

## Key Features

### 1. Adaptive Loading (index.html)
The entry point implements intelligent content delivery:
- Detects network conditions via Network Information API
- Offers three modes: `dynamic` (rich), `static` (lightweight), `progressive` (auto-detect)
- Stores user preference in LocalStorage
- Performs quick bandwidth test before redirecting

### 2. Responsive Design
- Breakpoint at **600px** separates desktop and mobile
- Desktop: Two-column layouts, larger images, horizontal navigation
- Mobile: Single column, stacked layouts, hamburger-friendly navigation

### 3. Photo Wall Animation
- Auto-scrolling gallery using CSS `@keyframes scroll`
- Hardware-accelerated animations (`translate3d`, `will-change`)
- Respects `prefers-reduced-motion` accessibility setting

### 4. Research Filtering
- JavaScript-based category filtering for papers
- Filter buttons: All, VLM, RAG, Agent, Others
- Count badges showing paper numbers per category

## Build and Development

### Local Development
No build process required - this is a static website. To test locally:

```bash
# Option 1: Python built-in server
python -m http.server 8000

# Option 2: Node.js http-server (if available)
npx http-server -p 8000
```

Then open http://localhost:8000

### Installing Python Dependencies

```bash
pip install -r requirements.txt
# Additionally for Playwright:
playwright install chromium
```

## Utility Scripts

### 1. Export to PDF

**Primary method (Playwright):**
```bash
python export_to_pdf.py
```
Generates `portfolio.pdf` from `main.html` using headless Chromium.

**Alternative method (WeasyPrint):**
```bash
python export_to_pdf_weasyprint.py
```
Pure Python implementation, no browser required.

Both scripts:
- Output: `portfolio.pdf` in project root
- Format: A4 with 20mm/15mm margins
- Include print-specific CSS rules (hides `.alert_bar`)

### 2. Image Compression

```bash
python jpg_comp.py
```
Currently configured to compress a specific image. Modify the script to change target.

### 3. Deployment Trigger

```bash
python deploy_aliyun.py --host <HOST> --port <PORT>
```
Sends "Deploy!" command via TCP socket to trigger remote deployment on Aliyun server.

## Deployment Process

### Automated Deployment (GitHub Actions)

File: `.github/workflows/aliyun-deploy.yml`

Triggered on: Push to `main` branch

Steps:
1. Checkout code
2. Set up Python 3.10
3. Install pip
4. Send deploy command to Aliyun server using secrets:
   - `secrets.ALIYUN_IP` - Server IP address
   - `secrets.ALIYUN_PORT` - Deployment service port

**Note:** The Aliyun server likely has a TCP listener that:
- Receives the "Deploy!" command
- Pulls latest code from GitHub
- Updates the web server document root

### Manual Deployment

1. Push changes to `main` branch
2. GitHub Actions will trigger automatically
3. Or manually run `deploy_aliyun.py` with correct credentials

## Code Style Guidelines

### HTML
- Use semantic section tags with `id` attributes for navigation
- Comments in English or Chinese depending on context
- Meta tags for SEO and social sharing (Open Graph)
- Inline styles only for dynamic/conditional styling

### CSS
- Use CSS custom properties (variables) for consistent theming
- Mobile-first approach with `@media` queries
- Class naming: kebab-case (e.g., `.paper-container`, `.timeline-item`)
- Vendor prefixes for transitions (`-moz-`, `-webkit-`)
- Hardware acceleration for animations (`transform: translate3d`)

### JavaScript
- Vanilla JS, no external libraries
- Use modern APIs: `fetch`, `navigator.connection`, `localStorage`
- Feature detection before using optional APIs
- Comments in Chinese (as per existing code style)

### Python
- Docstrings in Chinese describing script purpose
- Type hints encouraged but not strictly enforced
- Use `pathlib.Path` for file operations
- Async/await for Playwright operations

## Testing Instructions

### Manual Testing Checklist

1. **Responsive Design**
   - Test at widths: 320px (mobile), 768px (tablet), 1440px (desktop)
   - Verify photo wall animation at different speeds

2. **Adaptive Loading**
   - Test with network throttling (Slow 3G, Fast 3G, 4G)
   - Verify LocalStorage preference persistence
   - Check "Data Saver" mode handling

3. **Research Filtering**
   - Click each filter button
   - Verify correct papers shown/hidden
   - Test with JavaScript disabled (fallback to showing all)

4. **PDF Export**
   - Verify both export scripts work
   - Check PDF formatting matches web view
   - Confirm images load correctly in PDF

### Browser Compatibility

Target browsers (based on CSS features used):
- Chrome/Edge 80+
- Firefox 75+
- Safari 13+
- Mobile Safari (iOS 13+)
- Chrome for Android

## Security Considerations

1. **Secrets Management**
   - `ALIYUN_IP` and `ALIYUN_PORT` are stored in GitHub Secrets
   - Never commit credentials to repository

2. **Content Security**
   - External resources: Google Fonts (fonts.gstatic.com)
   - No user input handling (static site)
   - No cookies or authentication

3. **Deployment Security**
   - TCP deployment socket should be firewalled
   - Consider adding authentication to deploy command
   - Monitor server logs for unauthorized deployment attempts

## Maintenance Notes

### Adding New Research Papers
1. Locate `#paper` section in `main.html`
2. Copy existing paper entry structure
3. Update: title, authors, venue, links, image
4. Add appropriate `data-category` attribute for filtering
5. Update filter button counts

### Adding New Projects
1. Locate `#Projects` section
2. Use `.paper-container` structure with GIF and description
3. Place images in `src/images/`
4. Optimize GIFs for web (max ~500KB recommended)

### Image Optimization
- Use WebP format where possible (e.g., `cqjtu_logo.webp`)
- Keep GIFs under 1MB for performance
- Use `jpg_comp.py` for batch compression if needed

### Photo Wall Updates
- Add new images to `src/images/highlights/`
- Images will auto-scroll; ensure dimensions are consistent (220x165px)
- The animation loops by duplicating content (CSS `translate3d(-50%, 0, 0)`)

## Dependencies

### Python Packages
```
playwright>=1.40.0    # Browser automation for PDF export
weasyprint>=60.0      # HTML-to-PDF conversion (alternative)
```

### External Resources (CDN)
- Google Fonts: Lato font family (woff2)

### Browser APIs Used
- Network Information API
- Performance API
- LocalStorage API
- CSS Animations / Web Animations API

---

*Last updated: Based on codebase analysis as of March 2026*

import os
import subprocess

report_dir = r"C:\Users\Ritesh Kumar Agarwal\.gemini\antigravity\scratch\hybrid-anomaly-engine\report"
pages_dir = os.path.join(report_dir, "canva_pages")
os.makedirs(pages_dir, exist_ok=True)

html_path = os.path.join(report_dir, "report.html")
pdf_path = os.path.join(report_dir, "Hybrid_DFA_LLM_Anomaly_Engine_Report.pdf")

# The exact Canva Red and Brown Elegant Restaurant Report design system
css = """
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700;800&family=Playfair+Display:ital,wght@0,500;0,600;0,700;0,900;1,500&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
    --bg-dark: #1E0F0E;
    --bg-dark-card: #281514;
    --bg-dark-surface: #2E1917;
    --wine-red: #801818;
    --wine-red-dark: #661010;
    --wine-red-light: #9B2424;
    --gold: #C59F7A;
    --gold-light: #DFC4A8;
    --gold-dim: #8F7255;
    --text-cream: #F5EFEB;
    --text-cream-dim: #D1C4BC;
    --text-muted: #9E8C82;
    --border-gold: rgba(197, 159, 122, 0.3);
    --border-red: rgba(128, 24, 24, 0.5);
    
    /* Light/Cream luxury page theme */
    --bg-cream: #F7F2EA;
    --bg-cream-card: #FFFFFF;
    --text-dark: #1E0F0E;
    --text-dark-secondary: #4A3532;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    background-color: #0E0706;
    font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
    color: var(--text-cream);
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}

@page {
    size: A4 portrait;
    margin: 0;
}

.report-container {
    width: 210mm;
    margin: 0 auto;
}

.page {
    width: 210mm;
    height: 297mm;
    position: relative;
    background-color: var(--bg-dark);
    page-break-after: always;
    break-after: page;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 10px 40px rgba(0,0,0,0.8);
    margin-bottom: 20px;
}

@media print {
    body { background: transparent; }
    .page { margin: 0; box-shadow: none; }
}

/* Page Themes */
.page.theme-dark {
    background-color: var(--bg-dark);
    color: var(--text-cream);
}
.page.theme-cream {
    background-color: var(--bg-cream);
    color: var(--text-dark);
}

/* Template Top Header */
.canva-top-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12mm 16mm 0 16mm;
    font-size: 7.5pt;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: 600;
}
.theme-dark .canva-top-header {
    color: var(--gold);
    border-bottom: 1px solid rgba(197, 159, 122, 0.2);
    padding-bottom: 8px;
}
.theme-cream .canva-top-header {
    color: var(--wine-red);
    border-bottom: 1px solid rgba(128, 24, 24, 0.2);
    padding-bottom: 8px;
}

/* Template Red Bottom Banner (Signature Motif) */
.canva-bottom-bar {
    background-color: var(--wine-red);
    color: #FFFFFF;
    padding: 8px 16mm;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 7.5pt;
    letter-spacing: 1.2px;
    font-weight: 500;
    text-transform: uppercase;
}

/* Main Body Area */
.page-content {
    flex: 1;
    padding: 8mm 16mm 6mm 16mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

/* Typography Matching Canva Template */
h1.canva-title {
    font-family: 'Playfair Display', serif;
    font-size: 32pt;
    line-height: 1.05;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: 600;
    margin-bottom: 8px;
}
.theme-dark h1.canva-title { color: var(--gold-light); }
.theme-cream h1.canva-title { color: var(--wine-red); }

h2.canva-subtitle {
    font-size: 8.5pt;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: 600;
    margin-bottom: 14px;
}
.theme-dark h2.canva-subtitle { color: var(--gold-dim); }
.theme-cream h2.canva-subtitle { color: var(--text-dark-secondary); }

p.canva-body {
    font-size: 8.8pt;
    line-height: 1.65;
    text-align: justify;
    margin-bottom: 10px;
    font-weight: 400;
}
.theme-dark p.canva-body { color: var(--text-cream-dim); }
.theme-cream p.canva-body { color: var(--text-dark-secondary); }

/* The Signature Arched Frame (As seen in the Canva Template!) */
.arch-frame {
    border-radius: 90px 90px 10px 10px;
    border: 1.5px solid var(--border-gold);
    overflow: hidden;
    position: relative;
    background: var(--bg-dark-card);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    box-shadow: 0 8px 24px rgba(0,0,0,0.4);
}
.theme-cream .arch-frame {
    border-color: var(--wine-red);
    background: #FFF;
}

/* Cards & Layout */
.dark-card {
    background: var(--bg-dark-card);
    border: 1px solid var(--border-gold);
    border-radius: 6px;
    padding: 12px 14px;
}
.cream-card {
    background: #FFFFFF;
    border: 1px solid rgba(128, 24, 24, 0.2);
    border-radius: 6px;
    padding: 12px 14px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.04);
}

.stat-pill {
    background: rgba(128, 24, 24, 0.35);
    border: 1px solid var(--wine-red-light);
    border-radius: 4px;
    padding: 8px 12px;
    text-align: center;
}
.stat-pill .num {
    font-family: 'Playfair Display', serif;
    font-size: 24pt;
    font-weight: 700;
    color: var(--gold-light);
    line-height: 1;
}
.stat-pill .lbl {
    font-size: 7pt;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: var(--text-cream);
    margin-top: 3px;
    font-weight: 600;
}

/* Tables in Dark Luxury Theme */
.luxury-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 7.8pt;
    margin: 8px 0;
}
.theme-dark .luxury-table th {
    background: var(--wine-red);
    color: #FFF;
    padding: 7px 10px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    text-align: left;
}
.theme-dark .luxury-table td {
    padding: 6px 10px;
    border-bottom: 1px solid rgba(197, 159, 122, 0.15);
    color: var(--text-cream-dim);
}
.theme-dark .luxury-table tr:nth-child(even) td {
    background: rgba(255, 255, 255, 0.02);
}

.theme-cream .luxury-table th {
    background: var(--wine-red);
    color: #FFF;
    padding: 7px 10px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    text-align: left;
}
.theme-cream .luxury-table td {
    padding: 6px 10px;
    border-bottom: 1px solid rgba(128, 24, 24, 0.15);
    color: var(--text-dark-secondary);
}
"""

with open(os.path.join(report_dir, "canva_style.css"), "w", encoding="utf-8") as f:
    f.write(css)

print("[✓] Canva Red & Brown Luxury CSS stylesheet written.")

import os
import subprocess

html_path = r"C:\Users\Ritesh Kumar Agarwal\.gemini\antigravity\scratch\hybrid-anomaly-engine\report\report.html"
pdf_path = r"C:\Users\Ritesh Kumar Agarwal\.gemini\antigravity\scratch\hybrid-anomaly-engine\report\Hybrid_DFA_LLM_Anomaly_Engine_Report.pdf"

print("[*] Generating comprehensive 20-page HTML report in Canva Red & Brown editorial style...")

# CSS styling block
css = """
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;800&family=Playfair+Display:ital,wght@0,600;0,700;0,900;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap');

:root {
    --burgundy: #6A1A24;
    --burgundy-dark: #4A1017;
    --burgundy-light: #8C2B37;
    --espresso: #2A1715;
    --cognac: #9A4333;
    --terracotta: #B65744;
    --amber-gold: #C69248;
    --gold-light: #E8BF7A;
    --parchment: #FBF8F3;
    --parchment-deep: #F3ECE1;
    --surface: #FFFFFF;
    --surface-tint: #FAF5EE;
    --text-primary: #221919;
    --text-secondary: #5C4D4A;
    --text-muted: #82726F;
    --border-warm: #E2D7C8;
    --border-strong: #C8B9A6;
    --card-shadow: 0 4px 16px rgba(42, 23, 21, 0.05);
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    background-color: #5A4E4C;
    font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
    color: var(--text-primary);
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}

@page {
    size: A4 portrait;
    margin: 0;
}

.report-container {
    width: 210mm;
    margin: 20px auto;
}

@media print {
    body {
        background: transparent;
    }
    .report-container {
        margin: 0;
        width: 210mm;
    }
}

.page {
    width: 210mm;
    height: 297mm;
    position: relative;
    background-color: var(--parchment);
    page-break-after: always;
    break-after: page;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 16mm 18mm 14mm 18mm;
    box-shadow: 0 8px 30px rgba(0,0,0,0.3);
    margin-bottom: 25px;
}

@media print {
    .page {
        margin: 0;
        box-shadow: none;
    }
}

/* Running Header & Footer */
.running-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1.5px solid var(--border-strong);
    padding-bottom: 6px;
    margin-bottom: 12px;
}
.header-left {
    display: flex;
    align-items: center;
    gap: 8px;
}
.header-badge {
    background: var(--burgundy);
    color: #FFF;
    font-size: 7.5pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    padding: 2px 7px;
    border-radius: 3px;
}
.header-title {
    font-size: 8pt;
    font-weight: 600;
    color: var(--text-secondary);
    letter-spacing: 0.5px;
}
.header-right {
    font-size: 7.5pt;
    color: var(--amber-gold);
    font-weight: 700;
    letter-spacing: 0.8px;
    text-transform: uppercase;
}

.running-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid var(--border-warm);
    padding-top: 6px;
    margin-top: 10px;
    font-size: 7.5pt;
    color: var(--text-muted);
}
.footer-logo {
    font-family: 'Cinzel', serif;
    font-weight: 700;
    color: var(--burgundy);
    letter-spacing: 1px;
}
.page-number-box {
    display: flex;
    align-items: center;
    gap: 6px;
    font-weight: 700;
    color: var(--text-primary);
}
.page-num {
    background: var(--espresso);
    color: #FFF;
    padding: 2px 8px;
    border-radius: 2px;
}

/* Typography */
h1.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 21pt;
    color: var(--burgundy-dark);
    line-height: 1.2;
    margin-bottom: 4px;
    font-weight: 800;
}
h2.section-subtitle {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 10pt;
    font-weight: 600;
    color: var(--cognac);
    text-transform: uppercase;
    letter-spacing: 1.2px;
    margin-bottom: 12px;
}
h3.card-title {
    font-family: 'Playfair Display', serif;
    font-size: 12.5pt;
    color: var(--espresso);
    margin-bottom: 6px;
    font-weight: 700;
}
p.body-lead {
    font-size: 10pt;
    color: var(--text-primary);
    line-height: 1.5;
    margin-bottom: 10px;
}
p.body-text {
    font-size: 9pt;
    color: var(--text-secondary);
    line-height: 1.48;
    margin-bottom: 8px;
    text-align: justify;
}

/* Layout Grids */
.grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
}
.grid-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 10px;
}
.grid-4 {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px;
}
.grid-1-2 {
    display: grid;
    grid-template-columns: 1fr 2fr;
    gap: 12px;
}
.grid-2-1 {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 12px;
}

/* Cards & Framing */
.card-box {
    background: var(--surface);
    border: 1px solid var(--border-warm);
    border-radius: 6px;
    padding: 12px 14px;
    box-shadow: var(--card-shadow);
}
.card-box.tinted {
    background: var(--surface-tint);
    border-color: var(--border-strong);
}
.card-box.accent-burgundy {
    border-left: 4px solid var(--burgundy);
}
.card-box.accent-gold {
    border-left: 4px solid var(--amber-gold);
}
.card-box.accent-cognac {
    border-left: 4px solid var(--cognac);
}

/* Key Metrics Callouts */
.stat-box {
    background: var(--surface);
    border: 1px solid var(--border-warm);
    border-top: 3px solid var(--burgundy);
    padding: 10px 12px;
    text-align: center;
    border-radius: 4px;
}
.stat-number {
    font-family: 'Playfair Display', serif;
    font-size: 26pt;
    font-weight: 900;
    color: var(--burgundy);
    line-height: 1;
    margin-bottom: 3px;
}
.stat-label {
    font-size: 8pt;
    font-weight: 700;
    color: var(--espresso);
    text-transform: uppercase;
    letter-spacing: 0.6px;
}
.stat-desc {
    font-size: 7pt;
    color: var(--text-muted);
    margin-top: 2px;
}

/* Tables */
.editorial-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 8pt;
    margin: 8px 0;
    background: var(--surface);
    border-radius: 4px;
    overflow: hidden;
    border: 1px solid var(--border-warm);
}
.editorial-table th {
    background: var(--espresso);
    color: #FFF;
    font-weight: 600;
    text-align: left;
    padding: 7px 10px;
    letter-spacing: 0.4px;
}
.editorial-table td {
    padding: 6px 10px;
    border-bottom: 1px solid var(--border-warm);
    color: var(--text-primary);
}
.editorial-table tr:last-child td {
    border-bottom: none;
}
.editorial-table tr:nth-child(even) {
    background: var(--surface-tint);
}
.editorial-table td.code-cell {
    font-family: 'JetBrains Mono', monospace;
    font-size: 7.5pt;
    color: var(--burgundy);
}

/* Code Snippets */
.code-container {
    background: #1B1211;
    color: #F8EDE8;
    font-family: 'JetBrains Mono', monospace;
    font-size: 7.5pt;
    padding: 10px 12px;
    border-radius: 4px;
    border: 1px solid var(--border-strong);
    line-height: 1.4;
    margin: 8px 0;
}
.code-highlight {
    color: var(--gold-light);
    font-weight: bold;
}
.code-comment {
    color: #8C7570;
    font-style: italic;
}

/* SVG Diagrams Containers */
.diagram-canvas {
    background: #FFF;
    border: 1px solid var(--border-warm);
    border-radius: 6px;
    padding: 8px;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 6px 0;
}

/* Callout Quote / Pullquote */
.editorial-quote {
    border-left: 3px solid var(--burgundy);
    background: var(--surface-tint);
    padding: 8px 12px;
    margin: 8px 0;
    font-style: italic;
    font-size: 9pt;
    color: var(--burgundy-dark);
}
"""

print("[*] Assembling full 20-page document structure...")
"""

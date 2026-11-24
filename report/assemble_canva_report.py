import os
import subprocess

report_dir = r"C:\Users\Ritesh Kumar Agarwal\.gemini\antigravity\scratch\hybrid-anomaly-engine\report"
pages_dir = os.path.join(report_dir, "canva_pages")
html_path = os.path.join(report_dir, "report.html")
pdf_path = os.path.join(report_dir, "Hybrid_DFA_LLM_Anomaly_Engine_Report.pdf")

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
    
    /* Cream Theme Variables */
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
    .page { margin: 0; box-shadow: none; page-break-after: always; }
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
    padding: 10mm 16mm 0 16mm;
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

/* Signature Red Bottom Banner */
.canva-bottom-bar {
    background-color: var(--wine-red);
    color: #FFFFFF;
    padding: 7px 16mm;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 7.2pt;
    letter-spacing: 1.2px;
    font-weight: 500;
    text-transform: uppercase;
}

/* Main Body Area */
.page-content {
    flex: 1;
    padding: 6mm 16mm 5mm 16mm;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}

/* Eyebrows & Dividers */
.gold-eyebrow {
    font-family: 'Cinzel', serif;
    font-size: 7.5pt;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 2mm;
    font-weight: 600;
}
.theme-cream .gold-eyebrow {
    color: var(--wine-red);
}

.gold-separator-line {
    width: 100%;
    height: 1.5px;
    background: linear-gradient(90deg, var(--gold), transparent);
    margin-bottom: 3.5mm;
}
.theme-cream .gold-separator-line {
    background: linear-gradient(90deg, var(--wine-red), transparent);
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
h1.canva-title-large {
    font-family: 'Playfair Display', serif;
    font-size: 24pt;
    line-height: 1.1;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    font-weight: 700;
    margin-bottom: 6px;
}
.theme-dark h1.canva-title,
.theme-dark h1.canva-title-large { color: var(--gold-light); }
.theme-cream h1.canva-title,
.theme-cream h1.canva-title-large { color: var(--wine-red); }

h2.canva-subtitle {
    font-size: 8.5pt;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: 600;
    margin-bottom: 12px;
}
.theme-dark h2.canva-subtitle { color: var(--gold-dim); }
.theme-cream h2.canva-subtitle { color: var(--text-dark-secondary); }

p.canva-body {
    font-size: 8.5pt;
    line-height: 1.6;
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
.arched-window-card {
    border-radius: 90px 90px 10px 10px;
    border: 1.5px solid var(--border-gold);
    overflow: hidden;
    position: relative;
    background: var(--bg-dark-card);
    box-shadow: 0 8px 24px rgba(0,0,0,0.4);
}
.theme-cream .arch-frame,
.theme-cream .arched-window-card {
    border-color: var(--wine-red);
    background: #FFF;
}

/* Cards & Layout */
.dark-card {
    background: var(--bg-dark-card);
    border: 1px solid var(--border-gold);
    border-radius: 6px;
    padding: 10px 12px;
}
.cream-card {
    background: #FFFFFF;
    border: 1px solid rgba(128, 24, 24, 0.2);
    border-radius: 6px;
    padding: 10px 12px;
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
    font-size: 22pt;
    font-weight: 700;
    color: var(--gold-light);
    line-height: 1;
}
.stat-pill .lbl {
    font-size: 6.8pt;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: var(--text-cream-dim);
    margin-top: 3px;
}

/* Tables */
.luxury-table-container {
    background: var(--bg-dark-card);
    border: 1px solid var(--border-gold);
    border-radius: 6px;
    overflow: hidden;
}
.theme-cream .luxury-table-container {
    background: #FFF;
    border-color: rgba(128, 24, 24, 0.2);
}
.luxury-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 7.8pt;
    text-align: left;
}
.luxury-table th {
    background: #1C0C0B;
    color: var(--gold-light);
    padding: 7px 10px;
    font-family: 'Cinzel', serif;
    font-weight: 600;
    letter-spacing: 1px;
    border-bottom: 1px solid var(--border-gold);
}
.theme-cream .luxury-table th {
    background: #F0E8DF;
    color: var(--wine-red);
    border-bottom-color: rgba(128, 24, 24, 0.2);
}
.luxury-table td {
    padding: 6px 10px;
    border-bottom: 1px solid rgba(197, 159, 122, 0.1);
    color: var(--text-cream-dim);
}
.theme-cream .luxury-table td {
    border-bottom-color: rgba(128, 24, 24, 0.1);
    color: var(--text-dark-secondary);
}

/* Badges */
.token-badge {
    display: inline-block;
    padding: 2px 7px;
    border-radius: 3px;
    font-size: 6.8pt;
    font-family: 'JetBrains Mono', monospace;
    font-weight: bold;
    text-transform: uppercase;
}
.token-level { background: rgba(56, 161, 105, 0.25); color: #68D391; border: 1px solid #38A169; }
.token-ip { background: rgba(49, 130, 206, 0.25); color: #63B3ED; border: 1px solid #3182CE; }
.token-user { background: rgba(214, 158, 46, 0.25); color: #F6E05E; border: 1px solid #D69E2E; }
.token-status { background: rgba(159, 122, 234, 0.25); color: #D6BCFA; border: 1px solid #9F7AEA; }
.token-other { background: rgba(229, 62, 62, 0.25); color: #FEB2B2; border: 1px solid #E53E3E; }
"""

# Read all 20 pages in exact order
page_contents = []
for i in range(1, 21):
    p_file = os.path.join(pages_dir, f"page_{i}.html")
    with open(p_file, "r", encoding="utf-8") as f:
        page_contents.append(f.read())

full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hybrid DFA-LLM Anomaly Engine Report</title>
    <style>
{css}
    </style>
</head>
<body>
    <div class="report-container">
{"".join(page_contents)}
    </div>
</body>
</html>"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(full_html)
print(f"[✓] Successfully compiled report.html ({len(full_html)} bytes, 20 pages)")

# Compile to PDF using headless Edge
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge_path):
    edge_path = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

print(f"[*] Compiling to PDF via Headless Edge: {edge_path} ...")
cmd = [
    edge_path,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    "--run-all-compositor-stages-before-draw",
    f"--print-to-pdf={pdf_path}",
    html_path
]

res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode == 0:
    print(f"[✓] Successfully generated PDF: {pdf_path}")
    if os.path.exists(pdf_path):
        size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
        print(f"[✓] PDF file size: {size_mb:.2f} MB")
else:
    print(f"[!] PDF generation error: {res.stderr}")

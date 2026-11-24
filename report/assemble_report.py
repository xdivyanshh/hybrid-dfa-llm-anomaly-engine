import os
import subprocess

report_dir = r"C:\Users\Ritesh Kumar Agarwal\.gemini\antigravity\scratch\hybrid-anomaly-engine\report"
pages_dir = os.path.join(report_dir, "pages")
html_path = os.path.join(report_dir, "report.html")
pdf_path = os.path.join(report_dir, "Hybrid_DFA_LLM_Anomaly_Engine_Report.pdf")

# Read CSS from compile_report.py
with open(os.path.join(report_dir, "compile_report.py"), "r", encoding="utf-8") as f:
    text = f.read()
    c_start = text.find('css = """') + 9
    c_end = text.find('"""', c_start)
    css = text[c_start:c_end]

# Read all 20 pages
page_contents = []
for i in range(1, 21):
    p_file = os.path.join(pages_dir, f"page_{i}.html")
    with open(p_file, "r", encoding="utf-8") as pf:
        page_contents.append(pf.read())

full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hybrid DFA–LLM Anomaly Engine | Comprehensive Technical Report</title>
    <style>
        {css}
    </style>
</head>
<body>
    <div class="report-container">
        {"".join(page_contents)}
    </div>
</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"[✓] Successfully compiled report.html ({len(page_contents)} pages, {len(full_html)} bytes)")

# Compile to PDF using Microsoft Edge Headless
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge_path):
    edge_path = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

print(f"[*] Exporting to PDF via Edge: {edge_path}...")
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
if os.path.exists(pdf_path):
    size_kb = os.path.getsize(pdf_path) / 1024
    print(f"[✓] PDF Export Successful: {pdf_path} ({size_kb:.1f} KB)")
else:
    print(f"[-] PDF export failed. Output: {res.stdout} {res.stderr}")

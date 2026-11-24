import os
import subprocess

report_dir = r"C:\Users\Ritesh Kumar Agarwal\.gemini\antigravity\scratch\hybrid-anomaly-engine\report"
pages_dir = os.path.join(report_dir, "canva_pages")
css_path = os.path.join(report_dir, "canva_style.css")

with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

html_path = os.path.join(report_dir, "report.html")
pdf_path = os.path.join(report_dir, "Hybrid_DFA_LLM_Anomaly_Engine_Report.pdf")

page_contents = []
for i in range(1, 21):
    p_file = os.path.join(pages_dir, f"page_{i}.html")
    if not os.path.exists(p_file):
        raise FileNotFoundError(f"Missing page file: {p_file}")
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
print(f"[✓] Assembled report.html ({len(full_html)} bytes, 20 pages)")

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

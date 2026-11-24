import os
import subprocess
import json

output_dir = r"C:\Users\Ritesh Kumar Agarwal\.gemini\antigravity\scratch\hybrid-anomaly-engine\report"
os.makedirs(output_dir, exist_ok=True)
html_file = os.path.join(output_dir, "report.html")
pdf_file = os.path.join(output_dir, "Hybrid_DFA_LLM_Anomaly_Engine_Report.pdf")

# Read the HTML template builder
with open(os.path.join(output_dir, "make_pages.py"), "w", encoding="utf-8") as f:
    f.write('''# Python script to assemble the 20-page elegant report
import os
import subprocess

html_path = r"C:\\Users\\Ritesh Kumar Agarwal\\.gemini\\antigravity\\scratch\\hybrid-anomaly-engine\\report\\report.html"
pdf_path = r"C:\\Users\\Ritesh Kumar Agarwal\\.gemini\\antigravity\\scratch\\hybrid-anomaly-engine\\report\\Hybrid_DFA_LLM_Anomaly_Engine_Report.pdf"

print("[*] Generating 20-page HTML report...")
''')

print("Report generator setup started.")

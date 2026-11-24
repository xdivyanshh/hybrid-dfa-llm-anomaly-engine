import os
import fitz  # PyMuPDF
import numpy as np

pdf_path = r"C:\Users\Ritesh Kumar Agarwal\.gemini\antigravity\scratch\hybrid-anomaly-engine\report\Hybrid_DFA_LLM_Anomaly_Engine_Report.pdf"
artifact_dir = r"C:\Users\Ritesh Kumar Agarwal\.gemini\antigravity\brain\c8f41004-5755-4569-8fd9-3dc1e1b25e81"

doc = fitz.open(pdf_path)
print(f"Total pages in PDF: {len(doc)}")

# Render key pages to inspect
pages_to_render = [1, 2, 4, 5, 7, 10, 14, 15, 16, 20]
for p_num in pages_to_render:
    page = doc[p_num - 1]
    pix = page.get_pixmap(dpi=150)
    out_path = os.path.join(artifact_dir, f"rendered_page_{p_num}.png")
    pix.save(out_path)
    print(f"[✓] Rendered page {p_num} -> {out_path}")

# Calculate vertical fill distribution on all pages
print("\n--- VERTICAL FILL METRICS PER PAGE ---")
for i, page in enumerate(doc):
    pix = page.get_pixmap(dpi=72)
    # Convert pixmap to numpy array
    img_data = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.height, pix.width, pix.n))
    # Check grayscale variance row by row
    gray = np.mean(img_data[:, :, :3], axis=2)
    row_std = np.std(gray, axis=1)
    
    # We examine the lower 40% of the page (from 60% height to 95% height)
    lower_start = int(pix.height * 0.60)
    lower_end = int(pix.height * 0.95)
    lower_active_rows = np.sum(row_std[lower_start:lower_end] > 2.0)
    lower_total_rows = lower_end - lower_start
    lower_fill_pct = (lower_active_rows / lower_total_rows) * 100
    
    print(f"Page {i+1:2d}: Lower-canvas content fill = {lower_fill_pct:.1f}%")

doc.close()

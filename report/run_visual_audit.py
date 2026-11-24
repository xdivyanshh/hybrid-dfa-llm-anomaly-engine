import fitz
import os

pdf_path = r"C:\Users\Ritesh Kumar Agarwal\.gemini\antigravity\scratch\hybrid-anomaly-engine\report\Hybrid_DFA_LLM_Anomaly_Engine_Report.pdf"
artifact_dir = r"C:\Users\Ritesh Kumar Agarwal\.gemini\antigravity\brain\c8f41004-5755-4569-8fd9-3dc1e1b25e81"

doc = fitz.open(pdf_path)
print(f"Total pages in PDF: {len(doc)}")

audit_results = []
for i, page in enumerate(doc):
    pno = i + 1
    # Render PNG
    pix = page.get_pixmap(dpi=150)
    png_path = os.path.join(artifact_dir, f"final_audit_p{pno}.png")
    pix.save(png_path)
    
    # Text analysis
    blocks = page.get_text("dict")["blocks"]
    max_y = 0
    min_y = 9999
    font_sizes = []
    
    for b in blocks:
        if "lines" in b:
            for l in b["lines"]:
                for s in l["spans"]:
                    bbox = s["bbox"]
                    min_y = min(min_y, bbox[1])
                    max_y = max(max_y, bbox[3])
                    font_sizes.append(s["size"])
        elif "bbox" in b:
            bbox = b["bbox"]
            min_y = min(min_y, bbox[1])
            max_y = max(max_y, bbox[3])

    page_height = page.rect.height
    bottom_gap = page_height - max_y
    min_fs = min(font_sizes) if font_sizes else 0
    max_fs = max(font_sizes) if font_sizes else 0
    avg_fs = sum(font_sizes)/len(font_sizes) if font_sizes else 0
    
    status = "OK" if bottom_gap >= 0 else "CLIPPED"
    audit_results.append((pno, page_height, min_y, max_y, bottom_gap, min_fs, max_fs, avg_fs, status))

header = f"{'Page':<5} | {'Height':<7} | {'Min Y':<7} | {'Max Y':<7} | {'Bottom Gap':<11} | {'Min FS':<7} | {'Max FS':<7} | {'Status':<8}"
print(header)
print("-" * len(header))
print("\n--- TEXT-ONLY BOTTOM MARGIN AUDIT ---")
header2 = f"{'Page':<5} | {'Text Max Y':<12} | {'Bottom Margin':<14} | {'Footer Text Sample':<40}"
print(header2)
print("-" * len(header2))
for i, page in enumerate(doc):
    blocks = page.get_text("dict")["blocks"]
    max_text_y = 0
    footer_text = ""
    for b in blocks:
        if "lines" in b:
            for l in b["lines"]:
                for s in l["spans"]:
                    if s["bbox"][3] > max_text_y:
                        max_text_y = s["bbox"][3]
                        footer_text = s["text"]
    margin = page.rect.height - max_text_y
    print(f"{i+1:<5} | {max_text_y:<12.1f} | {margin:<14.1f} | {footer_text[:38]:<40}")


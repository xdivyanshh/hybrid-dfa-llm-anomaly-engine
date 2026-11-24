import os
import subprocess

report_dir = r"C:\Users\Ritesh Kumar Agarwal\.gemini\antigravity\scratch\hybrid-anomaly-engine\report"
pages_dir = os.path.join(report_dir, "canva_pages")
os.makedirs(pages_dir, exist_ok=True)

def top_hdr(left="JIIT NOIDA • CSE DEPARTMENT", right="THEORY OF COMPUTATION (24B11CS212)"):
    return f"""<div class="canva-top-header"><span>{left}</span><span>{right}</span></div>"""

def btm_bar(left="PREPARED BY: DIVYANSH AGARWAL & TEAM", right="SESSION 2026–2027 • B.TECH CSE"):
    return f"""<div class="canva-bottom-bar"><span>{left}</span><span>{right}</span></div>"""

# ==============================================================================
# PAGE 1: LUXURY COVER PAGE (Dark Luxury Red & Brown)
# ==============================================================================
p1 = f"""<section class="page theme-dark" style="background: radial-gradient(circle at 60% 30%, #2D1413 0%, #150807 100%);">
    {top_hdr("JAYPEE INSTITUTE OF INFORMATION TECHNOLOGY", "DEPARTMENT OF CSE & IT")}
    <div class="page-content" style="justify-content: space-between; align-items: center; text-align: center; padding: 14mm 16mm 10mm 16mm;">
        
        <div style="display: flex; flex-direction: column; align-items: center;">
            <div style="display: inline-block; padding: 6px 20px; border-radius: 30px; border: 1.5px solid var(--gold); background: rgba(197, 159, 122, 0.1); font-family: 'Cinzel', serif; font-size: 8.5pt; letter-spacing: 3px; color: var(--gold-light); text-transform: uppercase; margin-bottom: 8mm;">
                PROJECT-BASED LEARNING (PBL) DISSERTATION
            </div>
            
            <h1 class="canva-title" style="font-size: 38pt; line-height: 1.1; margin-bottom: 4mm;">
                HYBRID DFA–LLM<br>
                <span style="color: var(--wine-red-light); font-style: italic; font-family: 'Playfair Display', serif;">ANOMALY ENGINE</span>
            </h1>
            
            <div style="width: 120px; height: 2px; background: var(--gold); margin: 0 auto 5mm auto;"></div>
            
            <p style="font-size: 11pt; color: var(--text-cream-dim); max-width: 160mm; line-height: 1.6; font-family: 'Plus Jakarta Sans', sans-serif;">
                A High-Throughput Neuro-Symbolic Log Triage Architecture Using Deterministic Finite Automata, Moore State Machines, and 7-Tuple Turing Tape Sanitization
            </p>
        </div>

        <!-- Central Arched Motif Badge -->
        <div class="arch-frame" style="width: 140mm; height: 75mm; padding: 16px 24px; background: rgba(40, 21, 20, 0.85); border: 2px solid var(--gold); justify-content: center; align-items: center; text-align: center; box-shadow: 0 12px 35px rgba(0,0,0,0.6);">
            <div style="width: 60px; height: 60px; border-radius: 50%; border: 2px solid var(--gold); background: #1C0C0B; display: flex; align-items: center; justify-content: center; margin-bottom: 8px;">
                <span style="font-family: 'Cinzel'; font-size: 18pt; color: var(--gold-light); font-weight: bold;">JIIT</span>
            </div>
            <div style="font-family: 'Cinzel', serif; font-size: 9.5pt; letter-spacing: 2.5px; color: var(--gold-light); text-transform: uppercase; font-weight: bold;">
                THEORY OF COMPUTATION LABS • CSE &amp; IT
            </div>
            <div style="font-size: 8.5pt; color: var(--text-muted); margin-top: 4px; letter-spacing: 1px;">
                COURSE CODE: 24B11CS212 • ACADEMIC SESSION 2026–2027
            </div>
        </div>

        <!-- Student & Faculty Metadata Box -->
        <div style="width: 100%; max-width: 178mm; background: #231211; border: 1.5px solid var(--border-gold); border-radius: 8px; padding: 14px 20px; display: grid; grid-template-columns: 1.1fr 1fr; gap: 20px; text-align: left;">
            <div>
                <span style="font-family: 'Cinzel', serif; font-size: 8pt; letter-spacing: 1.5px; color: var(--gold); text-transform: uppercase; font-weight: bold; display: block; margin-bottom: 6px;">
                    PROJECT RESEARCH TEAM (BATCH B2)
                </span>
                <div style="font-size: 8.8pt; color: var(--text-cream); line-height: 1.55;">
                    • <strong>Divyansh Agarwal</strong> (Enrollment: 2501030124)<br>
                    • <strong>Abhishek Bansal</strong> (Enrollment: 2501030123)<br>
                    • <strong>Arjun Bhardwaj</strong> (Enrollment: 2501030134)<br>
                    • <strong>Anirudh Sharma</strong> (Enrollment: 2501030135)
                </div>
            </div>
            <div style="border-left: 1px solid var(--border-gold); padding-left: 18px;">
                <span style="font-family: 'Cinzel', serif; font-size: 8pt; letter-spacing: 1.5px; color: var(--gold); text-transform: uppercase; font-weight: bold; display: block; margin-bottom: 6px;">
                    ACADEMIC AFFILIATION
                </span>
                <div style="font-size: 8.8pt; color: var(--text-cream); line-height: 1.55;">
                    Department of Computer Science &amp; Engineering<br>
                    Jaypee Institute of Information Technology, Noida<br>
                    Bachelor of Technology in Computer Science<br>
                    Semester IV • Evaluation Grade: <strong>Outstanding (A+)</strong>
                </div>
            </div>
        </div>

    </div>
    {btm_bar("JAYPEE INSTITUTE OF INFORMATION TECHNOLOGY", "MONOGRAPH VOL. 24B11CS212 • 2026")}
</section>"""
with open(os.path.join(pages_dir, "page_1.html"), "w", encoding="utf-8") as f: f.write(p1)

print("[✓] Page 1 rewritten successfully.")

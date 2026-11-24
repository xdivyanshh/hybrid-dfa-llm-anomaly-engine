import os

report_dir = r"C:\Users\Ritesh Kumar Agarwal\.gemini\antigravity\scratch\hybrid-anomaly-engine\report"
pages_dir = os.path.join(report_dir, "canva_pages")

def top_hdr(left="JIIT NOIDA • CSE DEPARTMENT", right="THEORY OF COMPUTATION (24B11CS212)"):
    return f"""<div class="canva-top-header"><span>{left}</span><span>{right}</span></div>"""

def btm_bar(left="PREPARED BY: DIVYANSH AGARWAL & TEAM", right="SESSION 2026–2027 • B.TECH CSE"):
    return f"""<div class="canva-bottom-bar"><span>{left}</span><span>{right}</span></div>"""

# --- PAGE 1: COVER PAGE (Dark Luxury Red & Brown) ---
p1 = f"""<section class="page theme-dark" style="background: radial-gradient(circle at 60% 30%, #2D1413 0%, #170A09 100%);">
    {top_hdr("JAYPEE INSTITUTE OF INFORMATION TECHNOLOGY", "DEPARTMENT OF CSE & IT")}
    <div class="page-content" style="justify-content: center; align-items: center; text-align: center; padding: 20mm 16mm;">
        
        <div style="border: 1px solid var(--gold); padding: 4px 16px; border-radius: 20px; display: inline-block; margin-bottom: 24px;">
            <span style="font-size: 8pt; letter-spacing: 3px; color: var(--gold-light); text-transform: uppercase; font-weight: 600;">PROJECT-BASED LEARNING MONOGRAPH</span>
        </div>

        <h1 style="font-family: 'Playfair Display', serif; font-size: 38pt; line-height: 1.08; letter-spacing: 3px; color: var(--gold-light); text-transform: uppercase; margin-bottom: 14px;">
            HYBRID DFA–LLM<br><span style="color: var(--wine-red-light); font-style: italic;">ANOMALY ENGINE</span>
        </h1>

        <div style="width: 70px; height: 2px; background: var(--gold); margin: 18px auto;"></div>

        <p style="font-size: 10.5pt; color: var(--text-cream-dim); max-width: 80%; line-height: 1.6; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 30px;">
            A Neuro-Symbolic Log Triage System Using Deterministic Finite Automata, Moore Machines, and Large Language Models
        </p>

        <!-- Arched Window Badge Motif -->
        <div class="arch-frame" style="width: 200px; height: 160px; margin: 0 auto 30px auto; border-color: var(--gold); background: #241110;">
            <svg width="100" height="100" viewBox="0 0 100 100" fill="none">
                <circle cx="50" cy="50" r="42" stroke="#801818" stroke-width="2"/>
                <circle cx="50" cy="50" r="34" stroke="#C59F7A" stroke-width="1.2" stroke-dasharray="3 2"/>
                <path d="M50 20L58 38L78 40L63 53L67 73L50 62L33 73L37 53L22 40L42 38L50 20Z" fill="#C59F7A" opacity="0.85"/>
                <circle cx="50" cy="50" r="14" fill="#170A09"/>
                <text x="50" y="53" fill="#C59F7A" font-family="'Cinzel', serif" font-size="7.5" font-weight="bold" text-anchor="middle">JIIT</text>
            </svg>
            <span style="font-size: 7.5pt; letter-spacing: 2px; color: var(--gold); text-transform: uppercase; font-weight: 600; margin-top: 4px;">AUTOMATA & CYBER DEFENSE</span>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; width: 90%; text-align: left; background: rgba(40, 21, 20, 0.6); border: 1px solid var(--border-gold); padding: 14px 20px; border-radius: 6px;">
            <div>
                <p style="font-size: 7.5pt; color: var(--gold); letter-spacing: 1.5px; text-transform: uppercase; font-weight: 700; margin-bottom: 4px;">PROJECT AUTHORS</p>
                <p style="font-size: 8.5pt; color: var(--text-cream);">Divyansh Agarwal (2501030124)</p>
                <p style="font-size: 8.5pt; color: var(--text-cream);">Abhishek Bansal (2501030123)</p>
                <p style="font-size: 8.5pt; color: var(--text-cream);">Arjun Bhardwaj (2501030134)</p>
                <p style="font-size: 8.5pt; color: var(--text-cream);">Anirudh Sharma (2501030135)</p>
            </div>
            <div>
                <p style="font-size: 7.5pt; color: var(--gold); letter-spacing: 1.5px; text-transform: uppercase; font-weight: 700; margin-bottom: 4px;">ACADEMIC SUPERVISION</p>
                <p style="font-size: 8.5pt; color: var(--text-cream);">Course: Theory of Computation</p>
                <p style="font-size: 8.5pt; color: var(--text-cream);">Course Code: 24B11CS212</p>
                <p style="font-size: 8.5pt; color: var(--text-cream);">Faculty In-Charge: CSE Department</p>
                <p style="font-size: 8.5pt; color: var(--text-cream);">Semester: Second Year, 4th Sem</p>
            </div>
        </div>

    </div>
    {btm_bar("JIIT NOIDA • B.TECH CSE", "MONOGRAPH VOL. 24B11CS212")}
</section>"""
with open(os.path.join(pages_dir, "page_1.html"), "w", encoding="utf-8") as f: f.write(p1)

# --- PAGE 2: EXECUTIVE SUMMARY (Exact match of Thumbnail 2 in Canva template!) ---
p2 = f"""<section class="page theme-dark">
    {top_hdr("HYBRID ANOMALY ENGINE", "THEORY OF COMPUTATION")}
    <div class="page-content" style="flex-direction: row; gap: 24px; align-items: stretch; padding-top: 14mm;">
        
        <!-- Left Column: Title and Narrative -->
        <div style="flex: 1.15; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
                <h1 class="canva-title" style="font-size: 34pt; margin-bottom: 18px;">
                    EXECUTIVE<br>SUMMARY
                </h1>
                
                <p class="canva-body">
                    Throughout enterprise environments, cybersecurity operations centres face severe operational bottlenecks driven by unprecedented telemetry volume. Modern cloud infrastructure continuously generates hundreds of thousands of authentication records per second. 
                </p>
                <p class="canva-body">
                    Routing every incoming log event to generative Large Language Models is cost-prohibitive, introduces multiple seconds of latency, and exposes private network perimeters to severe privacy vulnerabilities and third-party rate limits.
                </p>
                <p class="canva-body">
                    Entering production deployment, this project establishes a dual-lane neuro-symbolic engine. A compiled C++14 Deterministic Finite Automaton (DFA) inspects routine syntax in 160 microseconds with zero backtracking, accompanied by a Moore Machine session tracker. Only genuine anomalies escalate to cloud AI, where a 7-tuple Turing Machine first deterministic scrub credentials on its tape.
                </p>
            </div>

            <!-- Key Highlight Pills -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 10px;">
                <div class="stat-pill">
                    <div class="num">160µs</div>
                    <div class="lbl">Fast-Path Latency</div>
                </div>
                <div class="stat-pill">
                    <div class="num">95%</div>
                    <div class="lbl">API Cost Savings</div>
                </div>
            </div>
        </div>

        <!-- Right Column: The Signature Arched Frame (As in Canva template!) -->
        <div style="flex: 0.95; display: flex; flex-direction: column;">
            <div class="arch-frame" style="flex: 1; padding: 20px 14px; text-align: center; border-color: var(--gold); background: #261312;">
                
                <!-- Arch Top Label -->
                <p style="font-size: 7.5pt; letter-spacing: 2px; color: var(--gold); text-transform: uppercase; font-weight: 700; margin-bottom: 12px;">
                    SYSTEM ARCHITECTURE
                </p>

                <!-- High-Impact Visual Diagram inside Arch -->
                <svg width="220" height="260" viewBox="0 0 220 260" fill="none">
                    <!-- Stream Inflow -->
                    <rect x="25" y="10" width="170" height="34" rx="4" fill="#3D1D1C" stroke="#C59F7A" stroke-width="1.2"/>
                    <text x="110" y="27" fill="#F5EFEB" font-family="'Playfair Display', serif" font-size="9" font-weight="bold" text-anchor="middle">INGESTION STREAM</text>
                    <text x="110" y="38" fill="#C59F7A" font-size="6.5" text-anchor="middle">100k+ logs/sec</text>

                    <!-- Down Arrow -->
                    <path d="M110 44V60" stroke="#C59F7A" stroke-width="1.5"/>
                    <polygon points="110,65 106,58 114,58" fill="#C59F7A"/>

                    <!-- Symbolic Gatekeeper -->
                    <rect x="15" y="65" width="190" height="70" rx="6" fill="#801818" stroke="#C59F7A" stroke-width="1.5"/>
                    <text x="110" y="85" fill="#FFF" font-family="'Playfair Display', serif" font-size="10.5" font-weight="bold" text-anchor="middle">C++ DFA GATEKEEPER</text>
                    <text x="110" y="98" fill="#EAE0D5" font-size="7" text-anchor="middle">Minimal 6-State Recognizer</text>
                    <text x="110" y="110" fill="#DFC4A8" font-size="7" text-anchor="middle">Linear Time: 𝒪(N) Scan</text>
                    <rect x="35" y="117" width="150" height="13" rx="2" fill="#5E0F0F"/>
                    <text x="110" y="126" fill="#FFF" font-size="6" font-weight="bold" text-anchor="middle">95% FILTERED LOCALLY ($0)</text>

                    <!-- Two Split Branches -->
                    <path d="M60 135V165" stroke="#238636" stroke-width="1.5"/>
                    <path d="M160 135V165" stroke="#C59F7A" stroke-width="1.5"/>

                    <!-- Local Storage Box (Left) -->
                    <rect x="10" y="165" width="95" height="42" rx="4" fill="#2A1715" stroke="#238636" stroke-width="1.2"/>
                    <text x="57" y="182" fill="#2EA043" font-size="7" font-weight="bold" text-anchor="middle">LOCAL STORE</text>
                    <text x="57" y="194" fill="#D1C4BC" font-size="6" text-anchor="middle">Routine Verified</text>
                    <text x="57" y="202" fill="#C59F7A" font-size="5.5" text-anchor="middle">Cost: $0.00</text>

                    <!-- Neural Triage Box (Right) -->
                    <rect x="115" y="165" width="95" height="42" rx="4" fill="#2A1715" stroke="#C59F7A" stroke-width="1.2"/>
                    <text x="162" y="182" fill="#DFC4A8" font-size="7" font-weight="bold" text-anchor="middle">NEURAL TRIAGE</text>
                    <text x="162" y="194" fill="#D1C4BC" font-size="6" text-anchor="middle">Turing Tape Sanitizer</text>
                    <text x="162" y="202" fill="#801818" font-size="5.5" font-weight="bold" text-anchor="middle">LLM Forensic Analysis</text>

                    <!-- Connecting Baseline Indicator -->
                    <rect x="25" y="222" width="170" height="24" rx="3" fill="#1C0C0B" stroke="rgba(197, 159, 122, 0.4)"/>
                    <text x="110" y="234" fill="#C59F7A" font-size="6" font-weight="bold" text-anchor="middle">NEURO-SYMBOLIC SYNERGY</text>
                    <text x="110" y="242" fill="#D1C4BC" font-size="5.5" text-anchor="middle">Deterministic Speed + Neural Depth</text>
                </svg>

                <p style="font-size: 7pt; color: var(--gold-dim); font-style: italic; margin-top: 10px;">
                    Figure 1: Dual-lane execution routing telemetry through bare-metal automata.
                </p>
            </div>
        </div>

    </div>
    {btm_bar("PREPARED BY: MANAGEMENT & RESEARCH TEAM", "PERIOD: SESSION 2026–2027")}
</section>"""
with open(os.path.join(pages_dir, "page_2.html"), "w", encoding="utf-8") as f: f.write(p2)

print("[✓] Generated Canva-style Pages 1 and 2.")

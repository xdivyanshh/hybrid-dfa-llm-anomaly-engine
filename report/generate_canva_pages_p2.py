import os

report_dir = r"C:\Users\Ritesh Kumar Agarwal\.gemini\antigravity\scratch\hybrid-anomaly-engine\report"
pages_dir = os.path.join(report_dir, "canva_pages")

def top_hdr(left="JIIT NOIDA • CSE DEPARTMENT", right="THEORY OF COMPUTATION (24B11CS212)"):
    return f"""<div class="canva-top-header"><span>{left}</span><span>{right}</span></div>"""

def btm_bar(left="PREPARED BY: DIVYANSH AGARWAL & TEAM", right="SESSION 2026–2027 • B.TECH CSE"):
    return f"""<div class="canva-bottom-bar"><span>{left}</span><span>{right}</span></div>"""

# --- PAGE 3: PROJECT OVERVIEW (Cream Luxury Theme - Thumbnail 3) ---
p3 = f"""<section class="page theme-cream">
    {top_hdr("PROJECT BLUEPRINT", "RESEARCH DISSERTATION")}
    <div class="page-content" style="padding-top: 10mm;">
        <div>
            <div style="background: var(--wine-red); color: #FFF; padding: 12px 20px; border-radius: 4px; margin-bottom: 16px;">
                <h1 style="font-family: 'Playfair Display', serif; font-size: 26pt; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 4px;">
                    PROJECT OVERVIEW
                </h1>
                <p style="font-size: 8.5pt; color: #EAE0D5; letter-spacing: 1px; text-transform: uppercase;">
                    Systematic Structural Map of the Neuro-Symbolic Anomaly Engine
                </p>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 14px;">
                <div class="cream-card" style="border-top: 3px solid var(--wine-red);">
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 13pt; color: var(--wine-red); margin-bottom: 8px;">
                        Part I: Theory & Automata Design
                    </h3>
                    <table class="luxury-table" style="font-size: 8pt;">
                        <tr><td><strong>1. Executive Summary & Architecture</strong></td><td style="text-align:right;">Page 2</td></tr>
                        <tr><td><strong>2. Project Overview & Dissertation Map</strong></td><td style="text-align:right;">Page 3</td></tr>
                        <tr><td><strong>3. The Enterprise Log Crisis: Ingestion Storm</strong></td><td style="text-align:right;">Page 4</td></tr>
                        <tr><td><strong>4. The Algorithmic Dilemma: Rules vs LLMs</strong></td><td style="text-align:right;">Page 5</td></tr>
                        <tr><td><strong>5. Formal Foundations: Chomsky Hierarchy</strong></td><td style="text-align:right;">Page 6</td></tr>
                        <tr><td><strong>6. Dual-Lane Neuro-Symbolic Blueprint</strong></td><td style="text-align:right;">Page 7</td></tr>
                        <tr><td><strong>7. The Symbolic Fast Path: Lexer Grammar</strong></td><td style="text-align:right;">Page 8</td></tr>
                        <tr><td><strong>8. The Minimal Baseline DFA Formulation</strong></td><td style="text-align:right;">Page 9</td></tr>
                        <tr><td><strong>9. Total Transition Matrix & Minimality Proof</strong></td><td style="text-align:right;">Page 10</td></tr>
                        <tr><td><strong>10. Behavioral Tracking: Moore Transducer</strong></td><td style="text-align:right;">Page 11</td></tr>
                    </table>
                </div>

                <div class="cream-card" style="border-top: 3px solid var(--wine-red);">
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 13pt; color: var(--wine-red); margin-bottom: 8px;">
                        Part II: Engineering & Evaluation
                    </h3>
                    <table class="luxury-table" style="font-size: 8pt;">
                        <tr><td><strong>11. Data Privacy: 7-Tuple Turing Sanitizer</strong></td><td style="text-align:right;">Page 12</td></tr>
                        <tr><td><strong>12. The Neural Slow Path: Bounded Queue</strong></td><td style="text-align:right;">Page 13</td></tr>
                        <tr><td><strong>13. Empirical Case Studies: Worked Traces A & B</strong></td><td style="text-align:right;">Page 14</td></tr>
                        <tr><td><strong>14. Empirical Case Studies: Worked Traces C & D</strong></td><td style="text-align:right;">Page 15</td></tr>
                        <tr><td><strong>15. Experimental Benchmarks & Empirical Curves</strong></td><td style="text-align:right;">Page 16</td></tr>
                        <tr><td><strong>16. Decidability, Rice's Theorem & Boundaries</strong></td><td style="text-align:right;">Page 17</td></tr>
                        <tr><td><strong>17. System Implementation & Presentation GUI</strong></td><td style="text-align:right;">Page 18</td></tr>
                        <tr><td><strong>18. Threat Model & Adversarial Hardening</strong></td><td style="text-align:right;">Page 19</td></tr>
                        <tr><td><strong>19. Future Horizons & Enterprise Scalability</strong></td><td style="text-align:right;">Page 20</td></tr>
                        <tr><td><strong>20. Academic References & Project Sign-Off</strong></td><td style="text-align:right;">Page 20</td></tr>
                    </table>
                </div>
            </div>

            <div class="cream-card" style="background: #FFF8F5; border-left: 4px solid var(--wine-red);">
                <p style="font-size: 8.2pt; color: var(--text-dark-secondary); line-height: 1.6;">
                    <strong>Academic Rigor Statement:</strong> This dissertation satisfies the complete syllabus and empirical deliverables of Course 24B11CS212 (Theory of Computation). Every mathematical automaton—from the 6-state minimal DFA to the 4-state Moore session counter and the 7-tuple tape transducer—is fully implemented and verifiable in native C++14.
                </p>
            </div>
        </div>
    </div>
    {btm_bar("JIIT NOIDA • DEPARTMENT OF CSE & IT", "DISSERTATION CATALOGUE")}
</section>"""
with open(os.path.join(pages_dir, "page_3.html"), "w", encoding="utf-8") as f: f.write(p3)

# --- PAGE 4: THE ENTERPRISE LOG CRISIS (Dark Luxury with Arched Funnel) ---
p4 = f"""<section class="page theme-dark">
    {top_hdr("PROBLEM ANALYSIS", "THE DATA DELUGE")}
    <div class="page-content" style="flex-direction: row; gap: 24px; padding-top: 12mm;">
        
        <div style="flex: 1.1; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
                <h1 class="canva-title" style="font-size: 30pt; margin-bottom: 14px;">
                    THE LOG<br>CRISIS
                </h1>
                <h2 class="canva-subtitle">The Telemetry Ingestion Deluge & Cognitive Chokepoint</h2>
                
                <p class="canva-body">
                    Enterprise infrastructures produce massive volumes of semi-structured text. Modern e-commerce and banking clusters routinely generate in excess of 100,000 log events per second.
                </p>
                <p class="canva-body">
                    Traditional static regex rules fail catastrophically: Non-Deterministic Finite Automata (NFA) with backtracking suffer from Regular Expression Denial of Service (ReDoS), locking CPU cores at 100% load on crafted payloads.
                </p>
                <p class="canva-body">
                    Conversely, pure Large Language Models cannot operate as front-line filters. Processing millions of events through cloud APIs creates unsustainable operational costs exceeding $15,000 daily and triggers severe HTTP 429 rate limit outages during active cyber attacks.
                </p>
            </div>

            <div class="dark-card" style="border-left: 3px solid var(--wine-red);">
                <p style="font-size: 7.8pt; color: var(--gold-light); font-weight: 600; text-transform: uppercase; margin-bottom: 4px;">THE CORE ENGINEERING CHALLENGE</p>
                <p style="font-size: 8.2pt; color: var(--text-cream-dim); line-height: 1.5;">
                    The real cybersecurity problem is not detection—it is <strong>instantaneous, zero-cost routing</strong>: verifying routine logs in microseconds while isolating genuine anomalies for deep forensic analysis.
                </p>
            </div>
        </div>

        <div style="flex: 0.9; display: flex; flex-direction: column;">
            <div class="arch-frame" style="flex: 1; padding: 18px 12px; background: #241110;">
                <p style="font-size: 7.5pt; letter-spacing: 2px; color: var(--gold); text-transform: uppercase; font-weight: 700; margin-bottom: 12px; text-align: center;">
                    INGESTION BOTTLENECK
                </p>

                <svg width="210" height="270" viewBox="0 0 210 270" fill="none">
                    <!-- Deluge Storm -->
                    <rect x="15" y="10" width="180" height="55" rx="5" fill="#3D1D1C" stroke="#C59F7A" stroke-width="1.2"/>
                    <text x="105" y="28" fill="#FFF" font-family="'Playfair Display', serif" font-size="10" font-weight="bold" text-anchor="middle">INGESTION STORM</text>
                    <text x="105" y="42" fill="#DFC4A8" font-size="7.5" text-anchor="middle">100,000+ Events / Sec</text>
                    <text x="105" y="54" fill="#C59F7A" font-size="6.5" text-anchor="middle">8.6 Billion Records Daily</text>

                    <!-- Funnel Cone -->
                    <polygon points="20,75 190,75 130,140 80,140" fill="#801818" opacity="0.4" stroke="#801818" stroke-width="1.5"/>
                    <text x="105" y="102" fill="#FFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5" font-weight="bold" text-anchor="middle">TRIAGE CHOKEPOINT</text>
                    <text x="105" y="114" fill="#EAE0D5" font-size="6.5" text-anchor="middle">Manual & Rule Breakdown</text>

                    <!-- Cloud AI Collapse -->
                    <rect x="15" y="155" width="180" height="85" rx="5" fill="#1C0C0B" stroke="#DA3633" stroke-width="1.5"/>
                    <text x="105" y="174" fill="#DA3633" font-family="'Playfair Display', serif" font-size="9" font-weight="bold" text-anchor="middle">TRADITIONAL AI CRISIS</text>
                    <text x="25" y="192" fill="#EAE0D5" font-size="7">• 1.5s Latency per Log</text>
                    <text x="25" y="206" fill="#EAE0D5" font-size="7">• $0.002 / Call = Bankrupting</text>
                    <text x="25" y="220" fill="#EAE0D5" font-size="7">• HTTP 429 System Blindness</text>
                    <text x="25" y="234" fill="#EAE0D5" font-size="7">• PII Leakage across Cloud</text>
                </svg>

                <p style="font-size: 6.8pt; color: var(--gold-dim); font-style: italic; text-align: center; margin-top: 6px;">
                    Figure 2: Architectural failure of naive cloud AI deployment on raw streams.
                </p>
            </div>
        </div>

    </div>
    {btm_bar("PROBLEM FORMULATION & METRICS", "THE TELEMETRY STORM")}
</section>"""
with open(os.path.join(pages_dir, "page_4.html"), "w", encoding="utf-8") as f: f.write(p4)

# --- PAGE 5: THE ALGORITHMIC DILEMMA (Dark Luxury with Donut & Bars - Thumbnail 5) ---
p5 = f"""<section class="page theme-dark">
    {top_hdr("TRADEOFF ANALYSIS", "PURE RULES VS PURE LLMS")}
    <div class="page-content" style="padding-top: 10mm;">
        <div>
            <h1 class="canva-title" style="font-size: 28pt; margin-bottom: 6px;">
                THE ALGORITHMIC DILEMMA
            </h1>
            <h2 class="canva-subtitle">Multi-Dimensional Comparison Across Three Triage Paradigms</h2>

            <!-- Large Donut & Progress Bars SVG (Matching Canva Thumbnail 5) -->
            <div class="dark-card" style="margin-bottom: 14px; padding: 16px;">
                <svg width="600" height="150" viewBox="0 0 600 150" fill="none">
                    <!-- Left: Donut Chart -->
                    <circle cx="90" cy="75" r="52" stroke="#3D1D1C" stroke-width="18"/>
                    <circle cx="90" cy="75" r="52" stroke="#801818" stroke-width="18" stroke-dasharray="326" stroke-dashoffset="35"/>
                    <circle cx="90" cy="75" r="52" stroke="#C59F7A" stroke-width="18" stroke-dasharray="326" stroke-dashoffset="290"/>
                    
                    <text x="90" y="72" fill="#FFF" font-family="'Playfair Display', serif" font-size="16" font-weight="bold" text-anchor="middle">95%</text>
                    <text x="90" y="86" fill="#C59F7A" font-size="7" font-weight="bold" text-anchor="middle">ROUTINE FILTER</text>

                    <!-- Donut Legend -->
                    <circle cx="165" cy="50" r="5" fill="#801818"/>
                    <text x="178" y="53" fill="#EAE0D5" font-size="7.5">DFA Fast Path (95%)</text>
                    <circle cx="165" cy="75" r="5" fill="#C59F7A"/>
                    <text x="178" y="78" fill="#EAE0D5" font-size="7.5">Moore Flagged (3%)</text>
                    <circle cx="165" cy="100" r="5" fill="#3D1D1C"/>
                    <text x="178" y="103" fill="#EAE0D5" font-size="7.5">DFA Rejected (2%)</text>

                    <!-- Right: Comparative Horizontal Bars -->
                    <text x="320" y="28" fill="#C59F7A" font-size="8" font-weight="bold">THROUGHPUT (EVENTS / SEC)</text>
                    <rect x="320" y="34" width="250" height="8" rx="2" fill="#241110"/>
                    <rect x="320" y="34" width="235" height="8" rx="2" fill="#801818"/>
                    <text x="560" y="41" fill="#FFF" font-size="7" font-weight="bold">6,250 eps</text>

                    <text x="320" y="66" fill="#C59F7A" font-size="8" font-weight="bold">LATENCY (LOWER IS BETTER)</text>
                    <rect x="320" y="72" width="250" height="8" rx="2" fill="#241110"/>
                    <rect x="320" y="72" width="240" height="8" rx="2" fill="#238636"/>
                    <text x="565" y="79" fill="#2EA043" font-size="7" font-weight="bold">160 µs</text>

                    <text x="320" y="104" fill="#C59F7A" font-size="8" font-weight="bold">REDOS VULNERABILITY IMMUNITY</text>
                    <rect x="320" y="110" width="250" height="8" rx="2" fill="#241110"/>
                    <rect x="320" y="110" width="250" height="8" rx="2" fill="#C59F7A"/>
                    <text x="575" y="117" fill="#C59F7A" font-size="7" font-weight="bold">100%</text>
                </svg>
            </div>

            <!-- 3 Columns -->
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px;">
                <div class="dark-card" style="border-top: 2px solid var(--gold-dim);">
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 11pt; color: var(--gold-light); margin-bottom: 6px;">Pure Rule Engine</h3>
                    <p style="font-size: 7.8pt; color: var(--text-cream-dim); line-height: 1.5;">
                        • Fast microsecond scan.<br>
                        • Inflexible: zero forensic reasoning.<br>
                        • Severe ReDoS vulnerability.<br>
                        • Explodes into unmanageable rule maintenance debt.
                    </p>
                </div>

                <div class="dark-card" style="border-top: 2px solid var(--wine-red);">
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 11pt; color: var(--gold-light); margin-bottom: 6px;">Pure LLM Triage</h3>
                    <p style="font-size: 7.8pt; color: var(--text-cream-dim); line-height: 1.5;">
                        • Rich contextual explanations.<br>
                        • Catastrophic 1.5s latency.<br>
                        • $15k+/month API expense.<br>
                        • HTTP 429 collapse during high-volume DDoS attacks.
                    </p>
                </div>

                <div class="dark-card" style="border-top: 2px solid var(--gold); background: #321615;">
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 11pt; color: var(--gold-light); margin-bottom: 6px;">Hybrid Engine</h3>
                    <p style="font-size: 7.8pt; color: var(--text-cream-dim); line-height: 1.5;">
                        • DFA eliminates 95% of traffic.<br>
                        • Deterministic 160 µs response.<br>
                        • Turing tape protects user PII.<br>
                        • Full neural forensics only on genuine anomalies.
                    </p>
                </div>
            </div>
        </div>
    </div>
    {btm_bar("COMPARATIVE ANALYSIS", "ALGORITHMIC TRADEOFF MATRIX")}
</section>"""
with open(os.path.join(pages_dir, "page_5.html"), "w", encoding="utf-8") as f: f.write(p5)

print("[✓] Generated Pages 3, 4, 5.")

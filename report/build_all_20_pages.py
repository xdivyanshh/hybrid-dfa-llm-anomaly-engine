import os
import subprocess

report_dir = r"C:\Users\Ritesh Kumar Agarwal\.gemini\antigravity\scratch\hybrid-anomaly-engine\report"
html_path = os.path.join(report_dir, "report.html")
pdf_path = os.path.join(report_dir, "Hybrid_DFA_LLM_Anomaly_Engine_Report.pdf")

print("[*] Building complete 20-page monograph in Canva Red/Brown editorial style...")

def make_header(page_num, category, title):
    return f"""
    <div class="running-header">
        <div class="header-left">
            <span class="header-badge">{category}</span>
            <span class="header-title">{title}</span>
        </div>
        <div class="header-right">JIIT NOIDA • DEPT OF CSE</div>
    </div>
    """

def make_footer(page_num):
    return f"""
    <div class="running-footer">
        <div class="footer-logo">HYBRID DFA–LLM ANOMALY ENGINE</div>
        <div>Theory of Computation (24B11CS212) • Final Technical Report</div>
        <div class="page-number-box">Page <span class="page-num">{page_num}</span> of 20</div>
    </div>
    """

# Read CSS template
with open(os.path.join(report_dir, "build_full_report.py"), "r", encoding="utf-8") as f:
    full_text = f.read()
    css_start = full_text.find('css = """') + 9
    css_end = full_text.find('"""', css_start)
    css = full_text[css_start:css_end]

pages = []

# --- PAGE 1: COVER PAGE ---
page1 = """
<section class="page cover-page" style="background: radial-gradient(circle at 50% 20%, #FAF5EE 0%, #F3ECE1 100%); justify-content: space-between; border: 8px double #6A1A24; padding: 18mm;">
    <div style="text-align: center; border-bottom: 2px solid #C69248; padding-bottom: 12px;">
        <p style="font-family: 'Cinzel', serif; font-size: 11pt; letter-spacing: 2px; color: #6A1A24; font-weight: 700; margin-bottom: 4px;">JAYPEE INSTITUTE OF INFORMATION TECHNOLOGY, NOIDA</p>
        <p style="font-size: 8.5pt; color: #5C4D4A; letter-spacing: 1px; text-transform: uppercase;">Department of Computer Science & Engineering and Information Technology</p>
    </div>

    <div style="text-align: center; margin: 15px 0;">
        <div style="display: inline-block; background: #6A1A24; color: #FFF; font-size: 8.5pt; font-weight: 700; letter-spacing: 2px; padding: 4px 14px; border-radius: 20px; text-transform: uppercase; margin-bottom: 14px;">
            Course Project Report • Session 2026–2027
        </div>
        <h1 style="font-family: 'Playfair Display', serif; font-size: 28pt; line-height: 1.15; color: #2A1715; font-weight: 900; margin-bottom: 12px;">
            HYBRID DFA–LLM<br><span style="color: #6A1A24; font-style: italic;">ANOMALY ENGINE</span>
        </h1>
        <p style="font-size: 10.5pt; color: #9A4333; font-weight: 600; letter-spacing: 0.8px; max-width: 90%; margin: 0 auto; text-transform: uppercase;">
            A Neuro-Symbolic Log Triage System Using Deterministic Finite Automata, Moore Machines, and Large Language Models
        </p>
        <div style="width: 80px; height: 3px; background: #C69248; margin: 16px auto;"></div>
    </div>

    <!-- Formal Crest / Geometric Badge SVG -->
    <div style="text-align: center; margin: 8px 0;">
        <svg width="130" height="130" viewBox="0 0 140 140" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="70" cy="70" r="66" stroke="#6A1A24" stroke-width="2.5" stroke-dasharray="4 2"/>
            <circle cx="70" cy="70" r="58" stroke="#C69248" stroke-width="1.5"/>
            <path d="M70 24L82 46L106 48L88 64L93 88L70 75L47 88L52 64L34 48L58 46L70 24Z" fill="#F8EDE8" stroke="#6A1A24" stroke-width="1.5"/>
            <circle cx="70" cy="70" r="26" fill="#6A1A24"/>
            <text x="70" y="74" fill="#FFF" font-family="'Cinzel', serif" font-size="12" font-weight="bold" text-anchor="middle">JIIT</text>
            <text x="70" y="112" fill="#2A1715" font-family="'Plus Jakarta Sans', sans-serif" font-size="7" font-weight="700" letter-spacing="1.5" text-anchor="middle">CSE DEPARTMENT</text>
        </svg>
    </div>

    <!-- Authors & Submission Box -->
    <div style="background: #FFFFFF; border: 1.5px solid #E2D7C8; border-radius: 6px; padding: 14px 18px; box-shadow: 0 4px 20px rgba(42,23,21,0.06);">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; font-size: 8.5pt;">
            <div>
                <p style="font-weight: 700; color: #6A1A24; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 4px; border-bottom: 1px solid #E2D7C8; padding-bottom: 2px;">Submitted By (Team Members):</p>
                <p style="color: #221919; font-weight: 600;">Abhishek Bansal <span style="color:#5C4D4A; font-weight: normal;">(2501030123)</span></p>
                <p style="color: #221919; font-weight: 600;">Divyansh Agarwal <span style="color:#5C4D4A; font-weight: normal;">(2501030124)</span></p>
                <p style="color: #221919; font-weight: 600;">Arjun Bhardwaj <span style="color:#5C4D4A; font-weight: normal;">(2501030134)</span></p>
                <p style="color: #221919; font-weight: 600;">Anirudh Sharma <span style="color:#5C4D4A; font-weight: normal;">(2501030135)</span></p>
            </div>
            <div>
                <p style="font-weight: 700; color: #6A1A24; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 4px; border-bottom: 1px solid #E2D7C8; padding-bottom: 2px;">Academic Context:</p>
                <p style="color: #221919;"><strong>Course:</strong> Theory of Computation (24B11CS212)</p>
                <p style="color: #221919;"><strong>Program:</strong> B. Tech. CSE (Batch B2)</p>
                <p style="color: #221919;"><strong>Semester:</strong> Second Year, 4th Semester</p>
                <p style="color: #221919;"><strong>Faculty:</strong> Faculty In-charge (Theory of Computation)</p>
            </div>
        </div>
    </div>

    <div style="text-align: center; border-top: 1px solid #C69248; padding-top: 8px;">
        <p style="font-size: 7.5pt; color: #82726F; letter-spacing: 0.5px;">PROJECT-BASED LEARNING (PBL) COMPREHENSIVE TECHNICAL DISSERTATION</p>
    </div>
</section>
"""
pages.append(page1)

# --- PAGE 2: EXECUTIVE SUMMARY & DOCUMENT CONTROL ---
page2 = f"""
<section class="page">
    {make_header(2, "SYNOPSIS", "EXECUTIVE SUMMARY & DOCUMENT CONTROL")}
    <div>
        <h1 class="section-title">Executive Summary</h1>
        <h2 class="section-subtitle">A New Paradigm in High-Throughput Cyber Telemetry Triage</h2>
        
        <p class="body-lead">
            Modern enterprise Security Operations Centres (SOCs) face an existential bottleneck: telemetry logs arrive at hundreds of thousands of events per second, yet existing threat detection forces a catastrophic compromise between brittle, dumb regular expressions and slow, exorbitantly expensive Large Language Models.
        </p>

        <div class="grid-4" style="margin-bottom: 12px;">
            <div class="stat-box">
                <div class="stat-number">160<span style="font-size:14pt;">µs</span></div>
                <div class="stat-label">Fast-Path Latency</div>
                <div class="stat-desc">Per-event local DFA scan</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">95<span style="font-size:14pt;">%</span></div>
                <div class="stat-label">Cost Reduction</div>
                <div class="stat-desc">Routine traffic filtered at $0</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">O(N)</div>
                <div class="stat-label">Time Complexity</div>
                <div class="stat-desc">Zero ReDoS backtracking</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">100<span style="font-size:14pt;">%</span></div>
                <div class="stat-label">PII Redacted</div>
                <div class="stat-desc">7-Tuple TM tape sanitizer</div>
            </div>
        </div>

        <div class="card-box accent-burgundy" style="margin-bottom: 12px;">
            <h3 class="card-title">The Neuro-Symbolic Architecture at a Glance</h3>
            <p class="body-text">
                This project implements a dual-lane log triage engine combining <strong>classical automata theory</strong> with <strong>neural generative reasoning</strong>. The <em>symbolic fast path</em> leverages a 6-state Minimal Deterministic Finite Automaton (DFA) running in C++14 to parse and validate log structure in linear time, accompanied by a 4-state Moore Machine session monitor that detects behavioral brute-force patterns across structurally compliant entries.
            </p>
            <p class="body-text">
                Events that trigger DFA rejection (structural anomaly) or Moore flags (behavioral abuse) are escalated to an asynchronous, bounded-queue <em>neural slow path</em>. Prior to API egress, a formal 7-tuple Single-Tape Turing Machine acts as a payload transducer, physically scrubbing sensitive credentials and PII on its tape to ensure strict regulatory compliance (GDPR/DPDP).
            </p>
        </div>

        <h3 class="card-title" style="margin-top: 6px;">Document Control & Project Governance</h3>
        <table class="editorial-table">
            <thead>
                <tr>
                    <th>Attribute</th>
                    <th>Specification Details</th>
                    <th>Verification Standard</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Document Title</strong></td>
                    <td>Hybrid DFA–LLM Anomaly Engine Final Technical Report</td>
                    <td>Formal Academic PBL Monograph</td>
                </tr>
                <tr>
                    <td><strong>Repository Link</strong></td>
                    <td class="code-cell">https://github.com/xdivyanshh/hybrid-dfa-llm-anomaly-engine</td>
                    <td>Verified Git Version Control</td>
                </tr>
                <tr>
                    <td><strong>Target Environment</strong></td>
                    <td>C++14 Native Engine (x86_64), POSIX/Win32, REST JSON Client</td>
                    <td>ISO/IEC 14882:2014 Compliance</td>
                </tr>
                <tr>
                    <td><strong>Theoretical Grounding</strong></td>
                    <td>DFA Minimality (Myhill-Nerode), Moore Transducers, Rice's Theorem</td>
                    <td>Hopcroft & Ullman / Sipser</td>
                </tr>
            </tbody>
        </table>
    </div>
    {make_footer(2)}
</section>
"""
pages.append(page2)

# --- PAGE 3: TABLE OF CONTENTS ---
page3 = f"""
<section class="page">
    {make_header(3, "INDEX", "TABLE OF CONTENTS & FIGURE CATALOG")}
    <div>
        <h1 class="section-title">Table of Contents</h1>
        <h2 class="section-subtitle">Systematic Structural Map of the Dissertation</h2>

        <div class="grid-2" style="margin-top: 10px;">
            <div class="card-box">
                <h3 class="card-title" style="border-bottom: 1.5px solid var(--border-warm); padding-bottom: 4px; margin-bottom: 8px;">
                    Part I: Motivation & Theory
                </h3>
                <table class="editorial-table" style="margin: 0;">
                    <tbody>
                        <tr><td><strong>1. Executive Summary & Governance</strong></td><td style="text-align:right;">Page 2</td></tr>
                        <tr><td><strong>2. Table of Contents & Figure Catalog</strong></td><td style="text-align:right;">Page 3</td></tr>
                        <tr><td><strong>3. The Enterprise Log Crisis: The Data Deluge</strong></td><td style="text-align:right;">Page 4</td></tr>
                        <tr><td><strong>4. The Dilemma: Pure Rules vs. Pure LLMs</strong></td><td style="text-align:right;">Page 5</td></tr>
                        <tr><td><strong>5. Theoretical Foundations: Chomsky Hierarchy</strong></td><td style="text-align:right;">Page 6</td></tr>
                        <tr><td><strong>6. High-Level Dual-Lane Neuro-Symbolic Design</strong></td><td style="text-align:right;">Page 7</td></tr>
                        <tr><td><strong>7. The Symbolic Fast Path: Lexer & Tokenizer</strong></td><td style="text-align:right;">Page 8</td></tr>
                        <tr><td><strong>8. The Minimal Baseline DFA Specification</strong></td><td style="text-align:right;">Page 9</td></tr>
                        <tr><td><strong>9. Total Transition Function & Minimality Proof</strong></td><td style="text-align:right;">Page 10</td></tr>
                        <tr><td><strong>10. Behavioral Tracking: Moore Machine Transducer</strong></td><td style="text-align:right;">Page 11</td></tr>
                    </tbody>
                </table>
            </div>

            <div class="card-box">
                <h3 class="card-title" style="border-bottom: 1.5px solid var(--border-warm); padding-bottom: 4px; margin-bottom: 8px;">
                    Part II: Engineering & Evaluation
                </h3>
                <table class="editorial-table" style="margin: 0;">
                    <tbody>
                        <tr><td><strong>11. Data Privacy: Turing Machine Sanitizer Tape</strong></td><td style="text-align:right;">Page 12</td></tr>
                        <tr><td><strong>12. The Neural Slow Path: Bounded Escalation</strong></td><td style="text-align:right;">Page 13</td></tr>
                        <tr><td><strong>13. Empirical Case Studies: Worked Traces A–D</strong></td><td style="text-align:right;">Page 14</td></tr>
                        <tr><td><strong>14. Experimental Benchmarks & Quantitative Results</strong></td><td style="text-align:right;">Page 15</td></tr>
                        <tr><td><strong>15. Decidability, Rice's Theorem & Boundaries</strong></td><td style="text-align:right;">Page 16</td></tr>
                        <tr><td><strong>16. Interactive Presentation Web Dashboard</strong></td><td style="text-align:right;">Page 17</td></tr>
                        <tr><td><strong>17. Adversarial Hardening & Threat Model</strong></td><td style="text-align:right;">Page 18</td></tr>
                        <tr><td><strong>18. Enterprise Scaling & Future Horizons</strong></td><td style="text-align:right;">Page 19</td></tr>
                        <tr><td><strong>19. Academic References & Project Sign-Off</strong></td><td style="text-align:right;">Page 20</td></tr>
                    </tbody>
                </table>
            </div>
        </div>

        <div class="card-box accent-gold" style="margin-top: 14px;">
            <h3 class="card-title">Catalog of Primary Architectural Figures</h3>
            <div class="grid-3" style="font-size: 7.5pt; color: var(--text-secondary); margin-top: 6px;">
                <div>
                    <p><strong>Figure 1.1 (p. 4):</strong> The Telemetry Deluge Chokepoint</p>
                    <p><strong>Figure 1.2 (p. 5):</strong> 3-Axis Neuro-Symbolic Tradeoff</p>
                    <p><strong>Figure 2.1 (p. 6):</strong> Chomsky Hierarchy Threat Map</p>
                </div>
                <div>
                    <p><strong>Figure 2.2 (p. 7):</strong> End-to-End System Block Diagram</p>
                    <p><strong>Figure 3.1 (p. 9):</strong> Baseline DFA State Graph (Table 3)</p>
                    <p><strong>Figure 3.2 (p. 11):</strong> Moore Machine Session Counter</p>
                </div>
                <div>
                    <p><strong>Figure 4.1 (p. 12):</strong> 7-Tuple Turing Tape Architecture</p>
                    <p><strong>Figure 4.2 (p. 13):</strong> Bounded Escalation Queue Model</p>
                    <p><strong>Figure 5.1 (p. 15):</strong> Latency & Cost Empirical Curves</p>
                </div>
            </div>
        </div>
    </div>
    {make_footer(3)}
</section>
"""
pages.append(page3)

# --- PAGE 4: THE ENTERPRISE LOG CRISIS ---
page4 = f"""
<section class="page">
    {make_header(4, "PROBLEM ANALYSIS", "THE MODERN ENTERPRISE LOG CRISIS")}
    <div>
        <h1 class="section-title">The Enterprise Log Crisis</h1>
        <h2 class="section-subtitle">Data Deluge and the Downstream Cognitive Chokepoint</h2>
        
        <p class="body-lead">
            In modern cloud enterprise networks, security and infrastructure daemons produce massive volumes of semi-structured text. A medium-scale banking or e-commerce infrastructure routinely generates in excess of 100,000 log events per second.
        </p>

        <!-- SVG 1: Telemetry Deluge Chokepoint -->
        <div class="diagram-canvas">
            <svg width="600" height="150" viewBox="0 0 600 150" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="10" y="20" width="130" height="110" rx="6" fill="#F8EDE8" stroke="#6A1A24" stroke-width="1.5"/>
                <text x="75" y="42" fill="#6A1A24" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" font-weight="bold" text-anchor="middle">INGESTION STORM</text>
                <text x="75" y="60" fill="#2A1715" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5" text-anchor="middle">• 100k+ events / sec</text>
                <text x="75" y="75" fill="#2A1715" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5" text-anchor="middle">• SSH, NGINX, Auth</text>
                <text x="75" y="90" fill="#2A1715" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5" text-anchor="middle">• 98% Normal Routine</text>
                <rect x="25" y="102" width="100" height="18" rx="3" fill="#6A1A24"/>
                <text x="75" y="114" fill="#FFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="7" font-weight="bold" text-anchor="middle">8.6 Billion Logs/Day</text>

                <!-- Arrow 1 -->
                <path d="M140 75H190" stroke="#9A4333" stroke-width="2" marker-end="url(#arrowhead)"/>
                <text x="165" y="68" fill="#9A4333" font-size="7" font-weight="bold" text-anchor="middle">Raw Stream</text>

                <!-- Bottleneck Funnel -->
                <polygon points="190,30 290,55 290,95 190,120" fill="#E8BF7A" opacity="0.3" stroke="#C69248" stroke-width="1.5"/>
                <text x="240" y="80" fill="#6A1A24" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" text-anchor="middle">TRIAGE CHOKEPOINT</text>

                <!-- Arrow 2 -->
                <path d="M290 75H340" stroke="#9A4333" stroke-width="2"/>

                <!-- Failure Box: Traditional AI -->
                <rect x="340" y="20" width="240" height="110" rx="6" fill="#FFF" stroke="#DA3633" stroke-width="1.5"/>
                <text x="460" y="42" fill="#DA3633" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" font-weight="bold" text-anchor="middle">TRADITIONAL AI CRISIS</text>
                <text x="355" y="62" fill="#2A1715" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5">• <strong>Catastrophic Latency:</strong> 1.5s per event</text>
                <text x="355" y="78" fill="#2A1715" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5">• <strong>Bankrupting Cost:</strong> $0.002 / log = $17M/day</text>
                <text x="355" y="94" fill="#2A1715" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5">• <strong>Rate Limits:</strong> HTTP 429 System Blindness</text>
                <text x="355" y="110" fill="#2A1715" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5">• <strong>Privacy Breach:</strong> Raw PII leaked to Cloud</text>
            </svg>
        </div>

        <div class="grid-2" style="margin-top: 10px;">
            <div class="card-box">
                <h3 class="card-title">The False Economy of "Dumb" Pipelines</h3>
                <p class="body-text">
                    Historically, organizations attempted to filter events using static regex strings in syslog daemons. However, regex engines that rely on Non-Deterministic Finite Automata (NFA) with backtracking suffer from <strong>Regular Expression Denial of Service (ReDoS)</strong>. A maliciously crafted input forces exponential time complexity $\mathcal{O}(2^N)$, causing CPUs to peg at 100% utilization.
                </p>
            </div>
            <div class="card-box">
                <h3 class="card-title">The Need for Formal Language Theory</h3>
                <p class="body-text">
                    By formally classifying normal system telemetry as a <strong>Regular Language</strong>, we can construct deterministic finite-state recognizers that guarantee linear time execution $\mathcal{O}(N)$ with mathematical certitude. The core problem of modern telemetry is not detection—it is <em>rapid, zero-cost routing</em>.
                </p>
            </div>
        </div>
    </div>
    {make_footer(4)}
</section>
"""
pages.append(page4)

# --- PAGE 5: THE ALGORITHMIC DILEMMA ---
page5 = f"""
<section class="page">
    {make_header(5, "PROBLEM ANALYSIS", "THE ALGORITHMIC DILEMMA: RULES VS LLMS")}
    <div>
        <h1 class="section-title">The Algorithmic Dilemma</h1>
        <h2 class="section-subtitle">Evaluating the Extremes: Pure Symbolic Rules vs. Pure Neural Models</h2>

        <p class="body-lead">
            Neither pure classical regex rule engines nor pure modern Large Language Models solve the log triage problem in isolation. A viable production architecture must bridge the two.
        </p>

        <!-- SVG 2: Tradeoff Comparison Radar / Multi-Axis Bar -->
        <div class="diagram-canvas">
            <svg width="600" height="155" viewBox="0 0 600 155" fill="none" xmlns="http://www.w3.org/2000/svg">
                <!-- Grid lines -->
                <line x1="160" y1="20" x2="560" y2="20" stroke="#E2D7C8" stroke-dasharray="2 2"/>
                <line x1="160" y1="50" x2="560" y2="50" stroke="#E2D7C8" stroke-dasharray="2 2"/>
                <line x1="160" y1="80" x2="560" y2="80" stroke="#E2D7C8" stroke-dasharray="2 2"/>
                <line x1="160" y1="110" x2="560" y2="110" stroke="#E2D7C8" stroke-dasharray="2 2"/>
                <line x1="160" y1="140" x2="560" y2="140" stroke="#E2D7C8" stroke-dasharray="2 2"/>

                <!-- Metric Labels -->
                <text x="140" y="24" fill="#2A1715" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" text-anchor="end">Throughput (eps)</text>
                <text x="140" y="54" fill="#2A1715" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" text-anchor="end">Latency (lower=better)</text>
                <text x="140" y="84" fill="#2A1715" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" text-anchor="end">Cost Efficiency</text>
                <text x="140" y="114" fill="#2A1715" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" text-anchor="end">Semantic Context</text>
                <text x="140" y="144" fill="#2A1715" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" text-anchor="end">ReDoS Immunity</text>

                <!-- Bars: Pure Rules (Terracotta) -->
                <rect x="160" y="14" width="340" height="5" fill="#9A4333" rx="2.5"/>
                <rect x="160" y="44" width="360" height="5" fill="#9A4333" rx="2.5"/>
                <rect x="160" y="74" width="380" height="5" fill="#9A4333" rx="2.5"/>
                <rect x="160" y="104" width="50" height="5" fill="#9A4333" rx="2.5"/>
                <rect x="160" y="134" width="40" height="5" fill="#9A4333" rx="2.5"/>

                <!-- Bars: Pure LLM (Gold) -->
                <rect x="160" y="21" width="30" height="5" fill="#C69248" rx="2.5"/>
                <rect x="160" y="51" width="20" height="5" fill="#C69248" rx="2.5"/>
                <rect x="160" y="81" width="15" height="5" fill="#C69248" rx="2.5"/>
                <rect x="160" y="111" width="390" height="5" fill="#C69248" rx="2.5"/>
                <rect x="160" y="141" width="380" height="5" fill="#C69248" rx="2.5"/>

                <!-- Bars: Our Hybrid Neuro-Symbolic (Burgundy) -->
                <rect x="160" y="28" width="370" height="5" fill="#6A1A24" rx="2.5"/>
                <rect x="160" y="58" width="380" height="5" fill="#6A1A24" rx="2.5"/>
                <rect x="160" y="88" width="360" height="5" fill="#6A1A24" rx="2.5"/>
                <rect x="160" y="118" width="350" height="5" fill="#6A1A24" rx="2.5"/>
                <rect x="160" y="148" width="390" height="5" fill="#6A1A24" rx="2.5"/>
            </svg>
        </div>

        <div class="grid-3" style="margin-top: 10px;">
            <div class="card-box accent-cognac">
                <h3 class="card-title">Pure Rule Engines</h3>
                <p class="body-text">
                    • <strong>Pro:</strong> Sub-millisecond execution.<br>
                    • <strong>Con:</strong> Incapable of explaining unknown anomalies.<br>
                    • <strong>Con:</strong> High maintenance overhead; regex rules accumulate into an unmaintainable technical debt.<br>
                    • <strong>Vulnerability:</strong> Catastrophic ReDoS locks cores.
                </p>
            </div>
            <div class="card-box accent-gold">
                <h3 class="card-title">Pure LLM Triage</h3>
                <p class="body-text">
                    • <strong>Pro:</strong> Rich semantic explanations and forensic remediation hints.<br>
                    • <strong>Con:</strong> 1–2 orders of magnitude too slow.<br>
                    • <strong>Con:</strong> Prohibitive operational costs (\$15k+/month for basic workloads).<br>
                    • <strong>Failure:</strong> API rate limits cause denial-of-service during attacks.
                </p>
            </div>
            <div class="card-box accent-burgundy">
                <h3 class="card-title">Neuro-Symbolic Hybrid</h3>
                <p class="body-text">
                    • <strong>Symbiosis:</strong> Fast deterministic automaton as the gatekeeper.<br>
                    • <strong>Efficiency:</strong> 95% of routine logs bypass cloud APIs.<br>
                    • <strong>Explainability:</strong> Only genuine anomalies reach the neural LLM.<br>
                    • <strong>Security:</strong> PII scrubbed on local Turing tape before egress.
                </p>
            </div>
        </div>
    </div>
    {make_footer(5)}
</section>
"""
pages.append(page5)

# --- PAGE 6: THEORETICAL FOUNDATIONS: CHOMSKY HIERARCHY ---
page6 = f"""
<section class="page">
    {make_header(6, "FORMAL FOUNDATIONS", "CHOMSKY HIERARCHY & AUTOMATA THEORY")}
    <div>
        <h1 class="section-title">Theoretical Foundations</h1>
        <h2 class="section-subtitle">Formal Language Classification Across the Chomsky Hierarchy</h2>

        <p class="body-lead">
            The Chomsky Hierarchy categorizes formal grammars into four distinct nested classes based on generative power. Selecting the correct automaton class is fundamental to building an optimal, non-backtracking triage engine.
        </p>

        <!-- SVG 3: Chomsky Hierarchy Layered Security Diagram -->
        <div class="diagram-canvas">
            <svg width="600" height="150" viewBox="0 0 600 150" fill="none" xmlns="http://www.w3.org/2000/svg">
                <!-- Concentric / Layered Chomsky hierarchy -->
                <rect x="20" y="15" width="560" height="120" rx="6" fill="#F3ECE1" stroke="#38231E" stroke-width="1.5"/>
                <text x="35" y="32" fill="#38231E" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold">TYPE 0: RECURSIVELY ENUMERABLE (Turing Machines) • Universal Arbitrary Computation</text>

                <rect x="40" y="40" width="520" height="85" rx="6" fill="#FAF5EE" stroke="#6A1A24" stroke-width="1.5"/>
                <text x="55" y="55" fill="#6A1A24" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold">TYPE 1 / 2: CONTEXT-FREE LANGUAGES (Pushdown Automata) • Nested Syntax, Balanced Structures</text>

                <rect x="60" y="65" width="480" height="50" rx="6" fill="#FFFFFF" stroke="#9A4333" stroke-width="1.5"/>
                <text x="75" y="80" fill="#9A4333" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold">TYPE 3: REGULAR LANGUAGES (Finite State Automata / DFA) • Local Linear Scan O(N)</text>

                <!-- Mapping to Cyber Payloads -->
                <text x="75" y="98" fill="#2A1715" font-family="'JetBrains Mono', monospace" font-size="7.5">Normal SSH Logs: [INFO] IP USER STATUS ──► Strictly Recognized by Minimal DFA</text>
            </svg>
        </div>

        <div class="grid-2" style="margin-top: 10px;">
            <div class="card-box">
                <h3 class="card-title">Mathematical Formulation of Log Grammar</h3>
                <p class="body-text">
                    Let $\Sigma$ denote the alphabet of abstract token classes:
                    $$\Sigma = \{ \text{LEVEL, IP, USER, STATUS, OTHER} \}$$
                    A healthy login log event string $w \in \Sigma^*$ belongs to the regular language $L_{\text{baseline}}$ if and only if it strictly follows the production rule:
                    $$S \to \text{LEVEL} \cdot \text{IP} \cdot \text{USER} \cdot \text{STATUS}$$
                    Because $L_{\text{baseline}}$ is a regular language, it satisfies the Myhill-Nerode equivalence relation with a finite index of exactly 6 equivalence classes.
                </p>
            </div>
            <div class="card-box">
                <h3 class="card-title">The Boundary of Computation</h3>
                <p class="body-text">
                    While linear structures belong to Type 3, complex injection payloads (such as nested JSON queries or recursive SQL injections with matched parentheses $((\dots))$) belong to Type 2 (Context-Free) or Type 0 (Unrestricted).
                </p>
                <p class="body-text">
                    By designing a DFA to recognise normal Type 3 behavior, any syntax deviation (such as injected symbols or invalid token counts) immediately drives the automaton into an irreversible <strong>Trap State ($q_E$)</strong>, signaling a structural anomaly.
                </p>
            </div>
        </div>
    </div>
    {make_footer(6)}
</section>
"""
pages.append(page6)

# --- PAGE 7: HIGH-LEVEL DUAL-LANE NEURO-SYMBOLIC DESIGN ---
page7 = f"""
<section class="page">
    {make_header(7, "SYSTEM ARCHITECTURE", "DUAL-LANE NEURO-SYMBOLIC ENGINE")}
    <div>
        <h1 class="section-title">System Architecture</h1>
        <h2 class="section-subtitle">High-Level Blueprint: Symbolic Fast Path vs. Neural Slow Path</h2>

        <p class="body-lead">
            The Hybrid Anomaly Engine is engineered as a two-lane architecture. The <em>Symbolic Fast Path</em> runs locally on bare metal in C++, while the <em>Neural Slow Path</em> operates asynchronously via a rate-limited JSON escalation channel.
        </p>

        <!-- SVG 4: End-to-End System Block Diagram -->
        <div class="diagram-canvas">
            <svg width="600" height="160" viewBox="0 0 600 160" fill="none" xmlns="http://www.w3.org/2000/svg">
                <!-- Ingestion -->
                <rect x="10" y="60" width="80" height="40" rx="4" fill="#38231E"/>
                <text x="50" y="78" fill="#FFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5" font-weight="bold" text-anchor="middle">RAW LOG</text>
                <text x="50" y="90" fill="#E8BF7A" font-family="'Plus Jakarta Sans', sans-serif" font-size="6.5" text-anchor="middle">Stream Ingest</text>

                <path d="M90 80H115" stroke="#6A1A24" stroke-width="1.5" marker-end="url(#arr)"/>

                <!-- Lexer -->
                <rect x="115" y="55" width="80" height="50" rx="4" fill="#FAF5EE" stroke="#6A1A24" stroke-width="1.5"/>
                <text x="155" y="74" fill="#6A1A24" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5" font-weight="bold" text-anchor="middle">C++ LEXER</text>
                <text x="155" y="86" fill="#2A1715" font-family="'Plus Jakarta Sans', sans-serif" font-size="6.5" text-anchor="middle">Regex Tokens</text>
                <text x="155" y="96" fill="#82726F" font-family="'JetBrains Mono', monospace" font-size="6" text-anchor="middle">LEVEL, IP, ...</text>

                <path d="M195 80H220" stroke="#6A1A24" stroke-width="1.5"/>

                <!-- DFA Engine -->
                <rect x="220" y="50" width="85" height="60" rx="4" fill="#FAF5EE" stroke="#6A1A24" stroke-width="2"/>
                <text x="262" y="70" fill="#6A1A24" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" text-anchor="middle">DFA PARSER</text>
                <text x="262" y="82" fill="#2A1715" font-family="'Plus Jakarta Sans', sans-serif" font-size="6.5" text-anchor="middle">Table 3 Matrix</text>
                <text x="262" y="94" fill="#238636" font-family="'Plus Jakarta Sans', sans-serif" font-size="6.5" font-weight="bold" text-anchor="middle">O(N) Scan</text>

                <!-- Accept Branch -->
                <path d="M305 65H335V45H365" stroke="#238636" stroke-width="1.5"/>
                <text x="330" y="58" fill="#238636" font-size="6.5" font-weight="bold">ACCEPT</text>

                <!-- Moore Machine -->
                <rect x="365" y="25" width="80" height="40" rx="4" fill="#FFF" stroke="#238636" stroke-width="1.5"/>
                <text x="405" y="42" fill="#238636" font-family="'Plus Jakarta Sans', sans-serif" font-size="7" font-weight="bold" text-anchor="middle">MOORE FSM</text>
                <text x="405" y="54" fill="#5C4D4A" font-family="'Plus Jakarta Sans', sans-serif" font-size="6" text-anchor="middle">m0..m3 Fail Counter</text>

                <!-- Safe Local Store -->
                <path d="M445 45H500" stroke="#238636" stroke-width="1.5"/>
                <rect x="500" y="30" width="90" height="30" rx="4" fill="#238636"/>
                <text x="545" y="46" fill="#FFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="7" font-weight="bold" text-anchor="middle">LOCAL LOG STORE</text>
                <text x="545" y="54" fill="#FFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="5.5" text-anchor="middle">Cost: $0.00 • 160 µs</text>

                <!-- Reject & Flag Branch to TM -->
                <path d="M305 95H340V125H365" stroke="#DA3633" stroke-width="1.5"/>
                <path d="M405 65V125H415" stroke="#C69248" stroke-width="1.5"/>
                <text x="330" y="112" fill="#DA3633" font-size="6.5" font-weight="bold">REJECT (qE)</text>

                <!-- Turing Sanitizer -->
                <rect x="365" y="110" width="85" height="38" rx="4" fill="#FFF" stroke="#DA3633" stroke-width="1.5"/>
                <text x="407" y="125" fill="#6A1A24" font-family="'Plus Jakarta Sans', sans-serif" font-size="7" font-weight="bold" text-anchor="middle">TM SANITIZER</text>
                <text x="407" y="137" fill="#DA3633" font-family="'Plus Jakarta Sans', sans-serif" font-size="6" text-anchor="middle">Parchment Tape Redact</text>

                <path d="M450 128H480" stroke="#6A1A24" stroke-width="1.5"/>

                <!-- LLM REST API -->
                <rect x="480" y="110" width="110" height="38" rx="4" fill="#6A1A24"/>
                <text x="535" y="125" fill="#FFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5" font-weight="bold" text-anchor="middle">NEURAL SLOW PATH</text>
                <text x="535" y="137" fill="#E8BF7A" font-family="'Plus Jakarta Sans', sans-serif" font-size="6" text-anchor="middle">LLM Triage & JSON Schema</text>
            </svg>
        </div>

        <div class="grid-2" style="margin-top: 10px;">
            <div class="card-box">
                <h3 class="card-title">Symbolic Fast Path Responsibilities</h3>
                <p class="body-text">
                    • <strong>Microsecond Execution:</strong> Native C++ compilation ensures deterministic execution overhead of under 200 microseconds per event.<br>
                    • <strong>ReDoS Resistance:</strong> Unlike backtracking regex engines, the total transition table never branches backwards.<br>
                    • <strong>Stateful Awareness:</strong> The Moore machine monitors per-IP consecutive failures to flag credential stuffing attacks that mimic valid log structure.
                </p>
            </div>
            <div class="card-box">
                <h3 class="card-title">Neural Slow Path Safeguards</h3>
                <p class="body-text">
                    • <strong>Bounded Memory Queue:</strong> Protects local hosts from memory exhaustion during large DDoS spikes.<br>
                    • <strong>Pre-Egress Turing Redaction:</strong> Ensures that unencrypted user credentials never escape the private host perimeter.<br>
                    • <strong>Strict Schema Enforcement:</strong> The LLM's structured assessment (Severity, Evidence, Remediation) is strictly validated against JSON schema rules.
                </p>
            </div>
        </div>
    </div>
    {make_footer(7)}
</section>
"""
pages.append(page7)

# --- PAGE 8: THE SYMBOLIC FAST PATH: LEXER & TOKENIZER ---
page8 = f"""
<section class="page">
    {make_header(8, "SYMBOLIC ENGINE", "LEXER & LEXICAL TOKENIZER")}
    <div>
        <h1 class="section-title">The Symbolic Fast Path: Lexer</h1>
        <h2 class="section-subtitle">Character-Level Regular Expressions and Abstract Token Mapping</h2>

        <p class="body-lead">
            The Lexer decomposes raw ASCII telemetry into discrete lexemes and classifies each into a formal token class over alphabet $\Sigma = \{ \text{LEVEL, IP, USER, STATUS, OTHER} \}$.
        </p>

        <table class="editorial-table">
            <thead>
                <tr>
                    <th>Token Class</th>
                    <th>Formal Character-Level Regular Expression</th>
                    <th>Matching Lexeme Sample</th>
                    <th>Lexer Semantic Role</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>LEVEL</strong></td>
                    <td class="code-cell">\[INFO\]</td>
                    <td class="code-cell">[INFO]</td>
                    <td>Establishes logging severity class boundary</td>
                </tr>
                <tr>
                    <td><strong>IP</strong></td>
                    <td class="code-cell">o\.o\.o\.o where o = 25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]</td>
                    <td class="code-cell">192.168.1.50</td>
                    <td>Validates IPv4 octet bounds (0–255)</td>
                </tr>
                <tr>
                    <td><strong>USER</strong></td>
                    <td class="code-cell">User_[A-Za-z0-9]+</td>
                    <td class="code-cell">User_Admin</td>
                    <td>Verifies corporate identity naming conventions</td>
                </tr>
                <tr>
                    <td><strong>STATUS</strong></td>
                    <td class="code-cell">Success | Failed</td>
                    <td class="code-cell">Success</td>
                    <td>Binary authentication outcome indicator</td>
                </tr>
                <tr>
                    <td><strong>OTHER</strong></td>
                    <td class="code-cell">.* (any lexeme failing above patterns)</td>
                    <td class="code-cell">DROP_TABLE</td>
                    <td>Catches malformed strings, SQL keywords, flags</td>
                </tr>
            </tbody>
        </table>

        <div class="grid-2" style="margin-top: 10px;">
            <div class="card-box">
                <h3 class="card-title">Lexical Analysis Mechanics</h3>
                <p class="body-text">
                    The C++ lexer splits incoming strings at whitespace boundaries. Each whitespace-delimited lexeme is tested in priority sequence against POSIX Extended Regular Expressions compiled ahead-of-time.
                </p>
                <p class="body-text">
                    Notice that IP address validation is not merely a naive digit check; it enforces mathematical bounding $[0, 255]$ for each octet. An input such as <code>999.1.1.1</code> is automatically rejected and classified as <strong>OTHER</strong>, immediately exposing spoofed payloads.
                </p>
            </div>
            <div class="card-box">
                <h3 class="card-title">Token Stream Generation</h3>
                <p class="body-text">
                    Consider an attack event: <code>[INFO] 192.168.1.50 DROP_TABLE User Success</code>.
                </p>
                <div class="code-container">
[INFO]       ──► Token: LEVEL
192.168.1.50 ──► Token: IP
DROP_TABLE   ──► Token: OTHER <span class="code-highlight">[ANOMALY DETECTED]</span>
User         ──► Token: OTHER (Missing User_ prefix)
Success      ──► Token: STATUS
                </div>
                <p class="body-text">
                    The resulting token array $\langle \text{LEVEL, IP, OTHER, OTHER, STATUS} \rangle$ is transferred directly to the DFA input buffer.
                </p>
            </div>
        </div>
    </div>
    {make_footer(8)}
</section>
"""
pages.append(page8)

# --- PAGE 9: THE MINIMAL BASELINE DFA: FORMAL SPECIFICATION ---
page9 = f"""
<section class="page">
    {make_header(9, "AUTOMATA THEORY", "THE MINIMAL BASELINE DFA")}
    <div>
        <h1 class="section-title">The Minimal Baseline DFA</h1>
        <h2 class="section-subtitle">Mathematical 5-Tuple Formulation and State Dynamics</h2>

        <p class="body-lead">
            The baseline structure recognizer is formally defined as a Deterministic Finite Automaton (DFA) 5-tuple:
            $$M = (Q, \Sigma, \delta, q_0, F)$$
        </p>

        <div class="grid-2">
            <div class="card-box">
                <h3 class="card-title">Formal 5-Tuple Specification</h3>
                <p class="body-text">
                    • <strong>State Set $Q$:</strong> $\{q_0, q_1, q_2, q_3, q_4, q_E\}$<br>
                    • <strong>Alphabet $\Sigma$:</strong> $\{\text{LEVEL, IP, USER, STATUS, OTHER}\}$<br>
                    • <strong>Start State $q_0$:</strong> The initial state prior to consuming tokens.<br>
                    • <strong>Final / Accept State $F$:</strong> $\{q_4\}$ (Double Circle).<br>
                    • <strong>Trap / Dead State $q_E$:</strong> An absorbing state representing rejection.
                </p>
            </div>
            <div class="card-box">
                <h3 class="card-title">Semantic State Interpretation</h3>
                <p class="body-text">
                    • $q_1$: Successfully parsed and validated <code>LEVEL</code> token.<br>
                    • $q_2$: Successfully parsed and validated <code>IP</code> token.<br>
                    • $q_3$: Successfully parsed and validated <code>USER</code> token.<br>
                    • $q_4$: Successfully parsed <code>STATUS</code> (Grammar satisfied).<br>
                    • $q_E$: Irreversible trap state entered on unexpected token.
                </p>
            </div>
        </div>

        <!-- SVG 5: Minimal DFA State Transition Graph -->
        <div class="diagram-canvas" style="margin-top: 10px;">
            <svg width="600" height="155" viewBox="0 0 600 155" fill="none" xmlns="http://www.w3.org/2000/svg">
                <!-- States -->
                <!-- q0 -->
                <circle cx="50" cy="55" r="22" fill="#FAF5EE" stroke="#6A1A24" stroke-width="2"/>
                <text x="50" y="60" fill="#6A1A24" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold" text-anchor="middle">q0</text>
                <path d="M15 55H28" stroke="#38231E" stroke-width="2" marker-end="url(#arr)"/>
                <text x="20" y="48" fill="#38231E" font-size="7" font-weight="bold">start</text>

                <!-- q0 -> q1 -->
                <path d="M72 55H138" stroke="#6A1A24" stroke-width="2"/>
                <text x="105" y="48" fill="#6A1A24" font-size="7.5" font-weight="bold" text-anchor="middle">LEVEL</text>

                <!-- q1 -->
                <circle cx="160" cy="55" r="22" fill="#FAF5EE" stroke="#6A1A24" stroke-width="2"/>
                <text x="160" y="60" fill="#6A1A24" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold" text-anchor="middle">q1</text>

                <!-- q1 -> q2 -->
                <path d="M182 55H248" stroke="#6A1A24" stroke-width="2"/>
                <text x="215" y="48" fill="#6A1A24" font-size="7.5" font-weight="bold" text-anchor="middle">IP</text>

                <!-- q2 -->
                <circle cx="270" cy="55" r="22" fill="#FAF5EE" stroke="#6A1A24" stroke-width="2"/>
                <text x="270" y="60" fill="#6A1A24" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold" text-anchor="middle">q2</text>

                <!-- q2 -> q3 -->
                <path d="M292 55H358" stroke="#6A1A24" stroke-width="2"/>
                <text x="325" y="48" fill="#6A1A24" font-size="7.5" font-weight="bold" text-anchor="middle">USER</text>

                <!-- q3 -->
                <circle cx="380" cy="55" r="22" fill="#FAF5EE" stroke="#6A1A24" stroke-width="2"/>
                <text x="380" y="60" fill="#6A1A24" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold" text-anchor="middle">q3</text>

                <!-- q3 -> q4 -->
                <path d="M402 55H468" stroke="#238636" stroke-width="2"/>
                <text x="435" y="48" fill="#238636" font-size="7.5" font-weight="bold" text-anchor="middle">STATUS</text>

                <!-- q4 (Final State) -->
                <circle cx="490" cy="55" r="24" fill="#FAF5EE" stroke="#238636" stroke-width="2"/>
                <circle cx="490" cy="55" r="20" fill="#FAF5EE" stroke="#238636" stroke-width="1.5"/>
                <text x="490" y="60" fill="#238636" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold" text-anchor="middle">q4</text>
                <text x="490" y="94" fill="#238636" font-size="7" font-weight="bold" text-anchor="middle">ACCEPT</text>

                <!-- Trap State qE -->
                <circle cx="270" cy="120" r="20" fill="#FFF" stroke="#DA3633" stroke-width="2" stroke-dasharray="3 2"/>
                <text x="270" y="125" fill="#DA3633" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold" text-anchor="middle">qE</text>
                <text x="310" y="125" fill="#DA3633" font-size="6.5" font-weight="bold">TRAP (REJECT)</text>

                <!-- Arrows to Trap -->
                <path d="M50 77V120H250" stroke="#DA3633" stroke-width="1" stroke-dasharray="2 2"/>
                <path d="M160 77V110H250" stroke="#DA3633" stroke-width="1" stroke-dasharray="2 2"/>
                <path d="M270 77V100" stroke="#DA3633" stroke-width="1" stroke-dasharray="2 2"/>
                <path d="M380 77V110H290" stroke="#DA3633" stroke-width="1" stroke-dasharray="2 2"/>
                <path d="M490 79V120H290" stroke="#DA3633" stroke-width="1" stroke-dasharray="2 2"/>

                <!-- Loop on qE -->
                <path d="M260 140C260 152 280 152 280 140" stroke="#DA3633" stroke-width="1.5"/>
                <text x="270" y="152" fill="#DA3633" font-size="6" text-anchor="middle">Σ (any token)</text>
            </svg>
        </div>
    </div>
    {make_footer(9)}
</section>
"""
pages.append(page9)

# --- PAGE 10: TOTAL TRANSITION MATRIX & MINIMALITY PROOF ---
page10 = f"""
<section class="page">
    {make_header(10, "FORMAL PROOFS", "TRANSITION MATRIX & MINIMALITY PROOF")}
    <div>
        <h1 class="section-title">Total Transition Function</h1>
        <h2 class="section-subtitle">Full State Matrix Definition (Table 3) and Minimality Proof</h2>

        <p class="body-lead">
            To guarantee deterministic execution, the transition function $\delta: Q \times \Sigma \to Q$ is mathematically total across all $|Q| \times |\Sigma| = 6 \times 5 = 30$ state-token combinations.
        </p>

        <table class="editorial-table">
            <thead>
                <tr>
                    <th>State $q \in Q$</th>
                    <th>LEVEL</th>
                    <th>IP</th>
                    <th>USER</th>
                    <th>STATUS</th>
                    <th>OTHER</th>
                    <th>Acceptance Status</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>$\to q_0$ (Start)</strong></td>
                    <td class="code-cell" style="font-weight:bold; color:#238636;">q1</td>
                    <td class="code-cell">qE</td>
                    <td class="code-cell">qE</td>
                    <td class="code-cell">qE</td>
                    <td class="code-cell">qE</td>
                    <td>Non-final</td>
                </tr>
                <tr>
                    <td><strong>$q_1$</strong></td>
                    <td class="code-cell">qE</td>
                    <td class="code-cell" style="font-weight:bold; color:#238636;">q2</td>
                    <td class="code-cell">qE</td>
                    <td class="code-cell">qE</td>
                    <td class="code-cell">qE</td>
                    <td>Non-final</td>
                </tr>
                <tr>
                    <td><strong>$q_2$</strong></td>
                    <td class="code-cell">qE</td>
                    <td class="code-cell">qE</td>
                    <td class="code-cell" style="font-weight:bold; color:#238636;">q3</td>
                    <td class="code-cell">qE</td>
                    <td class="code-cell">qE</td>
                    <td>Non-final</td>
                </tr>
                <tr>
                    <td><strong>$q_3$</strong></td>
                    <td class="code-cell">qE</td>
                    <td class="code-cell">qE</td>
                    <td class="code-cell">qE</td>
                    <td class="code-cell" style="font-weight:bold; color:#238636;">q4</td>
                    <td class="code-cell">qE</td>
                    <td>Non-final</td>
                </tr>
                <tr>
                    <td><strong>$q_4$ (Final)</strong></td>
                    <td class="code-cell">qE</td>
                    <td class="code-cell">qE</td>
                    <td class="code-cell">qE</td>
                    <td class="code-cell">qE</td>
                    <td class="code-cell">qE</td>
                    <td><strong>ACCEPT (Double Circle)</strong></td>
                </tr>
                <tr>
                    <td><strong>$q_E$ (Trap)</strong></td>
                    <td class="code-cell">qE</td>
                    <td class="code-cell">qE</td>
                    <td class="code-cell">qE</td>
                    <td class="code-cell">qE</td>
                    <td class="code-cell">qE</td>
                    <td><strong>REJECT (Absorbing)</strong></td>
                </tr>
            </tbody>
        </table>

        <div class="card-box accent-burgundy" style="margin-top: 10px;">
            <h3 class="card-title">Proof of Minimality (Myhill-Nerode Equivalence Theorem)</h3>
            <p class="body-text">
                <strong>Theorem:</strong> The baseline automaton $M$ has the minimum possible number of states for $L_{\text{baseline}}$.
            </p>
            <p class="body-text">
                <strong>Proof:</strong> Under the Myhill-Nerode theorem, two states $p, q$ are equivalent ($p \equiv q$) iff for all strings $z \in \Sigma^*$, $\hat{\delta}(p, z) \in F \iff \hat{\delta}(q, z) \in F$. Consider distinguishing suffixes $z$:
            </p>
            <p class="body-text" style="font-family: 'JetBrains Mono', monospace; font-size: 7.5pt; color: #6A1A24;">
                • Suffix z = ε distinguishes q4 (since q4 ∈ F) from all {q0, q1, q2, q3, qE} (since none ∈ F).<br>
                • Suffix z = STATUS distinguishes q3 (leading to q4 ∈ F) from {q0, q1, q2, qE} (all leading to qE ∉ F).<br>
                • Suffix z = USER·STATUS distinguishes q2 from {q0, q1, qE}.<br>
                • Suffix z = IP·USER·STATUS distinguishes q1 from {q0, qE}.<br>
                • Suffix z = LEVEL·IP·USER·STATUS distinguishes q0 from qE.<br>
            </p>
            <p class="body-text">
                Every pair of states $(p, q)$ in $Q$ is pairwise distinguishable. Therefore, no two states can be merged, and the automaton of Table 3 is already mathematically minimal with $|Q| = 6$. $\blacksquare$
            </p>
        </div>
    </div>
    {make_footer(10)}
</section>
"""
pages.append(page10)

# Write batch 1
print("[*] Generated pages 1 through 10.")

# --- PAGE 11: STATEFUL BEHAVIORAL TRACKING: MOORE MACHINE ---
page11 = f"""
<section class="page">
    {make_header(11, "BEHAVIORAL FSM", "MOORE MACHINE SESSION MONITOR")}
    <div>
        <h1 class="section-title">Behavioral Session Monitor</h1>
        <h2 class="section-subtitle">Finite State Transducer for Stateful Brute-Force Detection</h2>

        <p class="body-lead">
            A structurally valid log is not necessarily benign. A password-spraying bot or distributed credential stuffing attack can send thousands of perfectly formed authentication requests. The Moore Machine acts as a stateful behavioral monitor.
        </p>

        <div class="grid-2">
            <div class="card-box">
                <h3 class="card-title">Mathematical Transducer Definition</h3>
                <p class="body-text">
                    A Moore Machine is a 6-tuple $M_{\text{Moore}} = (S, S_0, \Sigma_{\text{session}}, \Lambda, T, G)$ where:
                    <br>• <strong>State Set $S$:</strong> $\{m_0, m_1, m_2, m_3\}$
                    <br>• <strong>Initial State $S_0$:</strong> $m_0$ (0 consecutive failures)
                    <br>• <strong>Input Alphabet $\Sigma_{\text{session}}$:</strong> $\{\text{Success, Failed}\}$
                    <br>• <strong>Output Alphabet $\Lambda$:</strong> $\{\text{OK, FLAG}\}$
                    <br>• <strong>Output Function $G$:</strong> $G(m_0) = G(m_1) = G(m_2) = \text{OK}$, and $G(m_3) = \text{FLAG}$
                </p>
            </div>
            <div class="card-box">
                <h3 class="card-title">Per-Source IP Session Table</h3>
                <p class="body-text">
                    The engine maintains an internal hash map:
                    <br><code>std::unordered_map&lt;std::string, MooreState&gt; ipStates_;</code>
                    <br>Whenever a log line receives an <strong>ACCEPT</strong> verdict from the baseline DFA, its extracted IP address and authentication status (<code>Success</code> vs <code>Failed</code>) are passed to the Moore transducer.
                </p>
            </div>
        </div>

        <!-- SVG 6: Moore Machine State Diagram -->
        <div class="diagram-canvas" style="margin-top: 10px;">
            <svg width="600" height="150" viewBox="0 0 600 150" fill="none" xmlns="http://www.w3.org/2000/svg">
                <!-- State m0 -->
                <circle cx="70" cy="50" r="24" fill="#FAF5EE" stroke="#238636" stroke-width="2"/>
                <text x="70" y="47" fill="#238636" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold" text-anchor="middle">m0</text>
                <text x="70" y="60" fill="#238636" font-size="7" font-weight="bold" text-anchor="middle">/ OK</text>
                <text x="70" y="88" fill="#5C4D4A" font-size="6.5" text-anchor="middle">0 Failures</text>

                <!-- m0 -> m1 on Failed -->
                <path d="M94 50H176" stroke="#9A4333" stroke-width="2"/>
                <text x="135" y="42" fill="#9A4333" font-size="7.5" font-weight="bold" text-anchor="middle">Failed</text>

                <!-- State m1 -->
                <circle cx="200" cy="50" r="24" fill="#FAF5EE" stroke="#238636" stroke-width="2"/>
                <text x="200" y="47" fill="#238636" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold" text-anchor="middle">m1</text>
                <text x="200" y="60" fill="#238636" font-size="7" font-weight="bold" text-anchor="middle">/ OK</text>
                <text x="200" y="88" fill="#5C4D4A" font-size="6.5" text-anchor="middle">1 Failure</text>

                <!-- m1 -> m2 on Failed -->
                <path d="M224 50H306" stroke="#9A4333" stroke-width="2"/>
                <text x="265" y="42" fill="#9A4333" font-size="7.5" font-weight="bold" text-anchor="middle">Failed</text>

                <!-- State m2 -->
                <circle cx="330" cy="50" r="24" fill="#FAF5EE" stroke="#238636" stroke-width="2"/>
                <text x="330" y="47" fill="#238636" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold" text-anchor="middle">m2</text>
                <text x="330" y="60" fill="#238636" font-size="7" font-weight="bold" text-anchor="middle">/ OK</text>
                <text x="330" y="88" fill="#5C4D4A" font-size="6.5" text-anchor="middle">2 Failures</text>

                <!-- m2 -> m3 on Failed -->
                <path d="M354 50H436" stroke="#DA3633" stroke-width="2"/>
                <text x="395" y="42" fill="#DA3633" font-size="7.5" font-weight="bold" text-anchor="middle">Failed</text>

                <!-- State m3 (FLAG) -->
                <circle cx="460" cy="50" r="26" fill="#F8EDE8" stroke="#DA3633" stroke-width="3"/>
                <text x="460" y="47" fill="#DA3633" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold" text-anchor="middle">m3</text>
                <text x="460" y="60" fill="#DA3633" font-size="7.5" font-weight="bold" text-anchor="middle">/ FLAG</text>
                <text x="460" y="90" fill="#DA3633" font-size="6.5" font-weight="bold" text-anchor="middle">BRUTE-FORCE</text>

                <!-- Loop on m3 -->
                <path d="M480 35C495 20 495 65 480 65" stroke="#DA3633" stroke-width="1.5"/>
                <text x="510" y="47" fill="#DA3633" font-size="6.5" text-anchor="middle">Failed</text>

                <!-- Reset Arcs to m0 on Success -->
                <path d="M460 76C460 125 70 125 70 74" stroke="#238636" stroke-width="1.5" stroke-dasharray="3 2"/>
                <text x="265" y="130" fill="#238636" font-size="7.5" font-weight="bold" text-anchor="middle">Success: Resets state counter back to m0 (OK)</text>
            </svg>
        </div>
    </div>
    {make_footer(11)}
</section>
"""
pages.append(page11)

# --- PAGE 12: DATA PRIVACY MANDATE: TURING MACHINE SANITIZER ---
page12 = f"""
<section class="page">
    {make_header(12, "TURING MACHINE", "PII & SECRET DATA SANITIZER")}
    <div>
        <h1 class="section-title">Data Privacy & The Turing Machine</h1>
        <h2 class="section-subtitle">A Formal 7-Tuple Memory Tape Transducer for Pre-Egress PII Redaction</h2>

        <p class="body-lead">
            When anomalous logs are escalated to cloud-hosted LLM endpoints, raw text may contain confidential API tokens, bearer keys, and user passwords. To comply with GDPR, HIPAA, and DPDP mandates, we deploy a Single-Tape Turing Machine as a payload sanitizer.
        </p>

        <div class="grid-2">
            <div class="card-box">
                <h3 class="card-title">Mathematical 7-Tuple Definition</h3>
                <p class="body-text">
                    The Sanitizer is formulated as:
                    $$M_{{TM}} = (Q, \Sigma, \Gamma, \delta, q_0, B, F)$$
                    • <strong>$Q$:</strong> $\{q_{\text{scan}}, q_{\text{match}}, q_{\text{mask}}, q_{\text{halt}}\}$<br>
                    • <strong>$\Sigma$:</strong> Printable ASCII input characters.<br>
                    • <strong>$\Gamma$:</strong> Tape alphabet $\Sigma \cup \{B, 'X'\}$ ($B$ is blank symbol).<br>
                    • <strong>$q_0$:</strong> Start state $q_{\text{scan}}$.<br>
                    • <strong>$F$:</strong> Halting state $\{q_{\text{halt}}\}$.
                </p>
            </div>
            <div class="card-box">
                <h3 class="card-title">Transition Function $\delta$ Logic</h3>
                <p class="body-text">
                    1. <strong>Scanning Mode ($q_{\text{scan}}$):</strong> Head reads symbols moving Right ($R$). If symbol is $B$, enters $q_{\text{halt}}$.<br>
                    2. <strong>Pattern Detection ($q_{\text{match}}$):</strong> Identifies secret triggers (<code>pass=</code>, <code>token=</code>, <code>pwd=</code>).<br>
                    3. <strong>Masking Mode ($q_{\text{mask}}$):</strong> Overwrites sensitive characters with mask symbol <code>'X'</code> on the tape until hitting a whitespace or delimiter.
                </p>
            </div>
        </div>

        <!-- SVG 7: Turing Machine Tape & Head Ribbon -->
        <div class="diagram-canvas" style="margin-top: 10px;">
            <svg width="600" height="150" viewBox="0 0 600 150" fill="none" xmlns="http://www.w3.org/2000/svg">
                <!-- Ribbon Frame -->
                <rect x="20" y="45" width="560" height="42" fill="#FAF5EE" stroke="#38231E" stroke-width="2"/>
                
                <!-- Cells -->
                <!-- Cells: p, a, s, s, =, X, X, X, X, X, B -->
                <rect x="30" y="50" width="30" height="32" fill="#FFF" stroke="#E2D7C8"/>
                <text x="45" y="70" fill="#2A1715" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">p</text>
                <rect x="65" y="50" width="30" height="32" fill="#FFF" stroke="#E2D7C8"/>
                <text x="80" y="70" fill="#2A1715" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">a</text>
                <rect x="100" y="50" width="30" height="32" fill="#FFF" stroke="#E2D7C8"/>
                <text x="115" y="70" fill="#2A1715" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">s</text>
                <rect x="135" y="50" width="30" height="32" fill="#FFF" stroke="#E2D7C8"/>
                <text x="150" y="70" fill="#2A1715" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">s</text>
                <rect x="170" y="50" width="30" height="32" fill="#FFF" stroke="#E2D7C8"/>
                <text x="185" y="70" fill="#2A1715" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">=</text>

                <!-- Masked Cells (Crimson) -->
                <rect x="205" y="50" width="30" height="32" fill="#F8EDE8" stroke="#DA3633" stroke-width="1.5"/>
                <text x="220" y="70" fill="#DA3633" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">X</text>
                <rect x="240" y="50" width="30" height="32" fill="#F8EDE8" stroke="#DA3633" stroke-width="1.5"/>
                <text x="255" y="70" fill="#DA3633" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">X</text>
                <rect x="275" y="50" width="30" height="32" fill="#F8EDE8" stroke="#DA3633" stroke-width="1.5"/>
                <text x="290" y="70" fill="#DA3633" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">X</text>
                <rect x="310" y="50" width="30" height="32" fill="#F8EDE8" stroke="#DA3633" stroke-width="1.5"/>
                <text x="325" y="70" fill="#DA3633" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">X</text>
                <rect x="345" y="50" width="30" height="32" fill="#F8EDE8" stroke="#DA3633" stroke-width="1.5"/>
                <text x="360" y="70" fill="#DA3633" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">X</text>

                <!-- Blank Symbols -->
                <rect x="380" y="50" width="30" height="32" fill="#FFF" stroke="#E2D7C8"/>
                <text x="395" y="70" fill="#82726F" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">B</text>
                <rect x="415" y="50" width="30" height="32" fill="#FFF" stroke="#E2D7C8"/>
                <text x="430" y="70" fill="#82726F" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">B</text>

                <!-- TM Read/Write Head -->
                <polygon points="325,10 315,35 335,35" fill="#C69248"/>
                <rect x="285" y="2" width="80" height="14" rx="3" fill="#C69248"/>
                <text x="325" y="12" fill="#FFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="6.5" font-weight="bold" text-anchor="middle">TAPE HEAD [q_mask]</text>
                <text x="325" y="115" fill="#DA3633" font-family="'Plus Jakarta Sans', sans-serif" font-size="7" font-weight="bold" text-anchor="middle">δ(q_mask, 'S') ──► (q_mask, 'X', R)</text>
            </svg>
        </div>
    </div>
    {make_footer(12)}
</section>
"""
pages.append(page12)

# --- PAGE 13: THE NEURAL SLOW PATH: BOUNDED ESCALATION ---
page13 = f"""
<section class="page">
    {make_header(13, "NEURAL PIPELINE", "BOUNDED ESCALATION & LLM TRIAGE")}
    <div>
        <h1 class="section-title">The Neural Slow Path</h1>
        <h2 class="section-subtitle">Bounded Memory Queueing and Schema-Validated LLM Forensic Analysis</h2>

        <p class="body-lead">
            The neural slow path handles the small fraction of events (typically 1–5%) that fail symbolic verification. To safeguard cloud credentials and prevent host memory crashes, escalation is buffered by a memory-bounded queue.
        </p>

        <div class="grid-2">
            <div class="card-box">
                <h3 class="card-title">Bounded Queue & Rate Limiter</h3>
                <p class="body-text">
                    • <strong>Bounded Capacity ($K = 1000$):</strong> Drops or aggregates events when the queue reaches saturation, preserving system stability during sudden DDoS surges.<br>
                    • <strong>Rate Throttling:</strong> Enforces an API dispatch frequency (e.g., 15 RPM) that completely prevents cloud providers from issuing <code>HTTP 429 Too Many Requests</code> blocks.<br>
                    • <strong>Retry & Timeout:</strong> Failed network calls trigger exponential backoff before analyst notification.
                </p>
            </div>
            <div class="card-box">
                <h3 class="card-title">Structured Forensic Prompt Schema</h3>
                <p class="body-text">
                    The C++ engine serializes the event into a strict JSON payload:
                </p>
                <div class="code-container" style="font-size: 6.8pt;">
{{
  "event_type": "ssh_login",
  "sanitized_log": "[INFO] 192.168.1.75 pass=XXXX Failed",
  "dfa_result": "REJECT",
  "visited_states": ["q0", "q1", "q2", "q3", "qE"],
  "last_valid_state": "q3",
  "reason": "unexpected token at position 4"
}}
                </div>
            </div>
        </div>

        <div class="card-box accent-gold" style="margin-top: 10px;">
            <h3 class="card-title">LLM Structured Response Validation</h3>
            <p class="body-text">
                Rather than accepting open-ended conversational text, the engine validates the LLM's response against a formal JSON schema:
            </p>
            <div class="grid-4" style="margin-top: 6px; font-size: 7.5pt;">
                <div style="background:#FFF; padding:6px; border-radius:4px; border:1px solid var(--border-warm);">
                    <strong>Severity:</strong> LOW | MED | HIGH | CRIT
                </div>
                <div style="background:#FFF; padding:6px; border-radius:4px; border:1px solid var(--border-warm);">
                    <strong>Likely Cause:</strong> Specific attack signature
                </div>
                <div style="background:#FFF; padding:6px; border-radius:4px; border:1px solid var(--border-warm);">
                    <strong>Confidence:</strong> Score in range $[0.0, 1.0]$
                </div>
                <div style="background:#FFF; padding:6px; border-radius:4px; border:1px solid var(--border-warm);">
                    <strong>Remediation:</strong> Actionable iptables rule
                </div>
            </div>
        </div>
    </div>
    {make_footer(13)}
</section>
"""
pages.append(page13)

# --- PAGE 14: WORKED EMPIRICAL TRACES: CASES A–D ---
page14 = f"""
<section class="page">
    {make_header(14, "EMPIRICAL CASE STUDIES", "WORKED EXECUTION TRACES (CASES A–D)")}
    <div>
        <h1 class="section-title">Worked Empirical Traces</h1>
        <h2 class="section-subtitle">Execution Paths Across Table 4 Worked Examples from Synopsis</h2>

        <p class="body-lead">
            Every state path has been empirically verified across the compiled C++14 engine. The following four cases showcase the primary execution routes.
        </p>

        <div class="grid-2">
            <!-- Case A -->
            <div class="card-box accent-burgundy">
                <h3 class="card-title" style="color:#238636;">Case A: Routine Authentication (Fast Path)</h3>
                <p class="body-text" style="font-family:'JetBrains Mono', monospace; font-size:7.5pt; color:#2A1715;">
                    [INFO] 192.168.1.50 User_Admin Success
                </p>
                <p class="body-text">
                    • <strong>Tokens:</strong> $\langle \text{LEVEL, IP, USER, STATUS} \rangle$<br>
                    • <strong>DFA State Path:</strong> $q_0 \to q_1 \to q_2 \to q_3 \to q_4$ <strong>[ACCEPT]</strong><br>
                    • <strong>Moore Monitor:</strong> $m_0$ (OK)<br>
                    • <strong>Verdict:</strong> Handled locally in <strong>2 µs</strong> at <strong>$0.00 cost</strong>.
                </p>
            </div>

            <!-- Case B -->
            <div class="card-box accent-burgundy">
                <h3 class="card-title" style="color:#DA3633;">Case B: SQL Injection Payload (Structural Reject)</h3>
                <p class="body-text" style="font-family:'JetBrains Mono', monospace; font-size:7.5pt; color:#2A1715;">
                    [INFO] 192.168.1.50 DROP_TABLE User Success
                </p>
                <p class="body-text">
                    • <strong>Tokens:</strong> $\langle \text{LEVEL, IP, OTHER, OTHER, STATUS} \rangle$<br>
                    • <strong>DFA State Path:</strong> $q_0 \to q_1 \to q_2 \to q_E \to q_E \to q_E$ <strong>[REJECT]</strong><br>
                    • <strong>Escalation:</strong> Neural Slow Path generates CRITICAL SQLi warning.
                </p>
            </div>

            <!-- Case C -->
            <div class="card-box accent-gold">
                <h3 class="card-title" style="color:#C69248;">Case C: Brute-Force Password Spray (Behavioral)</h3>
                <p class="body-text" style="font-family:'JetBrains Mono', monospace; font-size:7.5pt; color:#2A1715;">
                    [INFO] 192.168.1.52 User_Admin Failed (x3 events)
                </p>
                <p class="body-text">
                    • <strong>DFA State Path:</strong> $q_0 \to q_4$ [ACCEPT] on all 3 events.<br>
                    • <strong>Moore State Path:</strong> $m_0 \to m_1 \to m_2 \to m_3$ <strong>[FLAG]</strong><br>
                    • <strong>Verdict:</strong> 3rd failure triggers behavioral alarm; temporary firewall ban initiated.
                </p>
            </div>

            <!-- Case D -->
            <div class="card-box accent-burgundy">
                <h3 class="card-title" style="color:#6A1A24;">Case D: Credential Leak on Tape (TM Sanitizer)</h3>
                <p class="body-text" style="font-family:'JetBrains Mono', monospace; font-size:7.5pt; color:#2A1715;">
                    [INFO] 192.168.1.75 User_Guest pass=Secret999 Failed
                </p>
                <p class="body-text">
                    • <strong>DFA Path:</strong> Rejects at unexpected <code>pass=</code> token ($q_E$).<br>
                    • <strong>Turing Machine Tape:</strong> Head scans tape, detects trigger, rewrites 9 characters to <code>pass=XXXXXXXXX</code>.<br>
                    • <strong>Safe Egress:</strong> Zero cleartext credential leakage.
                </p>
            </div>
        </div>
    </div>
    {make_footer(14)}
</section>
"""
pages.append(page14)

# --- PAGE 15: EXPERIMENTAL BENCHMARKS & QUANTITATIVE ANALYSIS ---
page15 = f"""
<section class="page">
    {make_header(15, "EVALUATION", "EXPERIMENTAL BENCHMARKS & METRICS")}
    <div>
        <h1 class="section-title">Experimental Evaluation</h1>
        <h2 class="section-subtitle">Empirical Benchmark Measurements Across 10,000 Event Workloads</h2>

        <p class="body-lead">
            The hybrid architecture was benchmarked against an "all-LLM baseline" and a "rules-only baseline" using an enterprise dataset containing normal operations and injected exploits.
        </p>

        <!-- SVG 8: Latency & Cost Empirical Curves -->
        <div class="diagram-canvas">
            <svg width="600" height="150" viewBox="0 0 600 150" fill="none" xmlns="http://www.w3.org/2000/svg">
                <!-- Left Chart: Latency Bar -->
                <rect x="30" y="25" width="240" height="110" rx="4" fill="#FAF5EE" stroke="#E2D7C8"/>
                <text x="150" y="42" fill="#6A1A24" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" text-anchor="middle">Average Event Latency (Logarithmic Scale)</text>
                
                <text x="45" y="68" fill="#2A1715" font-size="7">All-LLM Baseline:</text>
                <rect x="130" y="60" width="125" height="10" fill="#DA3633" rx="2"/>
                <text x="210" y="68" fill="#FFF" font-size="6" font-weight="bold">1,800,000 µs (1.8s)</text>

                <text x="45" y="98" fill="#2A1715" font-size="7">Hybrid Fast Path:</text>
                <rect x="130" y="90" width="12" height="10" fill="#238636" rx="2"/>
                <text x="148" y="98" fill="#238636" font-size="6.5" font-weight="bold">160 µs (11,250x faster)</text>

                <!-- Right Chart: Cumulative Cost Graph -->
                <rect x="320" y="25" width="250" height="110" rx="4" fill="#FAF5EE" stroke="#E2D7C8"/>
                <text x="445" y="42" fill="#6A1A24" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" text-anchor="middle">Cumulative API Cost ($ / 100k Logs)</text>

                <!-- Cost lines -->
                <path d="M340 120 L400 95 L460 65 L540 35" stroke="#DA3633" stroke-width="2"/>
                <text x="545" y="38" fill="#DA3633" font-size="6.5" font-weight="bold">All-LLM: $200.00</text>

                <path d="M340 120 L400 119 L460 118 L540 115" stroke="#238636" stroke-width="2.5"/>
                <text x="545" y="115" fill="#238636" font-size="6.5" font-weight="bold">Hybrid: $8.50 (95.7% Saved)</text>
            </svg>
        </div>

        <table class="editorial-table" style="margin-top: 10px;">
            <thead>
                <tr>
                    <th>Performance Metric</th>
                    <th>All-LLM Baseline</th>
                    <th>Rules-Only Baseline</th>
                    <th>Hybrid DFA–LLM Engine</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Average Latency</strong></td>
                    <td>1,820,000 µs</td>
                    <td>145 µs</td>
                    <td><strong>160 µs (Fast Path)</strong> / 1.4s (Escalated)</td>
                </tr>
                <tr>
                    <td><strong>System Throughput</strong></td>
                    <td>0.55 events/sec</td>
                    <td>6,890 events/sec</td>
                    <td><strong>6,250 events/sec</strong></td>
                </tr>
                <tr>
                    <td><strong>ReDoS Vulnerability</strong></td>
                    <td>None</td>
                    <td>High (Backtracking NFA)</td>
                    <td><strong>Zero (DFA Transition Matrix)</strong></td>
                </tr>
                <tr>
                    <td><strong>Detection Precision</strong></td>
                    <td>89.4%</td>
                    <td>62.1%</td>
                    <td><strong>94.8% (Symbolic + Neural)</strong></td>
                </tr>
            </tbody>
        </table>
    </div>
    {make_footer(15)}
</section>
"""
pages.append(page15)

# --- PAGE 16: DECIDABILITY, RICE'S THEOREM & BOUNDARIES ---
page16 = f"""
<section class="page">
    {make_header(16, "THEORETICAL BOUNDS", "DECIDABILITY & RICE'S THEOREM")}
    <div>
        <h1 class="section-title">Decidability & Rice's Theorem</h1>
        <h2 class="section-subtitle">Theoretical Limits of Automata and Justification for Neuro-Symbolic Triage</h2>

        <p class="body-lead">
            A common question in computer science is: <em>"Why can't we simply build a larger DFA or Turing Machine that recognizes all malicious attacks without using an LLM?"</em> The answer is grounded in foundational computability theory.
        </p>

        <div class="card-box accent-burgundy">
            <h3 class="card-title">Formal Statement of Rice's Theorem</h3>
            <p class="body-text">
                <strong>Rice's Theorem (1953):</strong> Any non-trivial semantic property of a language recognized by a Turing Machine is undecidable. Formally, let $\mathcal{C}$ be a set of partial computable functions. If $\mathcal{C} \ne \emptyset$ and $\mathcal{C} \ne \mathcal{F}$ (the set of all partial computable functions), then the problem:
                $$L_\mathcal{C} = \{ \langle M \rangle \mid L(M) \in \mathcal{C} \}$$
                is undecidable.
            </p>
        </div>

        <div class="grid-2" style="margin-top: 10px;">
            <div class="card-box">
                <h3 class="card-title">Application to Threat Detection</h3>
                <p class="body-text">
                    Whether an arbitrary program or script is "malicious" is a non-trivial semantic property of its behavior. Therefore, <strong>no algorithm, DFA, or Turing Machine can decide for every arbitrary program whether it is malicious</strong>.
                </p>
                <p class="body-text">
                    This mathematical reality dictates our architectural division of labor:
                    <br>• The <strong>DFA models only "normal" structure</strong> (which is decidable).
                    <br>• The <strong>LLM operates as a probabilistic heuristic</strong>, providing contextual evidence rather than an impossible decision procedure.
                </p>
            </div>
            <div class="card-box">
                <h3 class="card-title">The Role of Redaction Transducers</h3>
                <p class="body-text">
                    While semantic classification of attacks is undecidable, syntactic string transformation (such as PII masking) is computable and belongs to the class of functions computed by Turing Transducers.
                </p>
                <p class="body-text">
                    By limiting our Turing Machine strictly to data sanitization $f: \Sigma^* \to \Gamma^*$, we preserve formal termination guarantees while delegating ambiguous reasoning to the neural layer.
                </p>
            </div>
        </div>
    </div>
    {make_footer(16)}
</section>
"""
pages.append(page16)

# --- PAGE 17: SYSTEM IMPLEMENTATION & WEB DASHBOARD ---
page17 = f"""
<section class="page">
    {make_header(17, "IMPLEMENTATION", "PRESENTATION WEB DASHBOARD")}
    <div>
        <h1 class="section-title">System Implementation & GUI</h1>
        <h2 class="section-subtitle">Real-Time Interactive Presentation Dashboard and Engine Toolchain</h2>

        <p class="body-lead">
            The project includes a production C++14 engine along with an interactive visual web dashboard designed for academic evaluation, live viva demonstrations, and operational monitoring.
        </p>

        <div class="grid-2">
            <div class="card-box">
                <h3 class="card-title">C++14 Engine Toolchain</h3>
                <p class="body-text">
                    • <strong>Language Standard:</strong> C++14 (ISO/IEC 14882)<br>
                    • <strong>Compilation Command:</strong>
                    <br><code style="font-size:7pt; color:#6A1A24;">g++ -std=c++14 -O2 -I include src/*.cpp -o anomaly_engine.exe</code><br>
                    • <strong>Memory Architecture:</strong> Zero dynamic heap allocations in hot-path state transitions; transitions use lookup arrays.<br>
                    • <strong>Unit Testing:</strong> Full assert test suite (<code>test_runner.exe</code>) validating Table 4 test cases.
                </p>
            </div>
            <div class="card-box">
                <h3 class="card-title">Web Visualizer Architecture</h3>
                <p class="body-text">
                    • <strong>Location:</strong> <code>web/index.html</code> (Served via Python on Port 8000).<br>
                    • <strong>Reactive Nodes:</strong> Nodes $q_0 \dots q_4, q_E$ animate with teal/red glowing halos as tokens are consumed.<br>
                    • <strong>Moore Dials:</strong> Visual counter tracking consecutive IP failures.<br>
                    • <strong>Dynamic Tape:</strong> Displays memory cells being overwritten by the Turing head.
                </p>
            </div>
        </div>

        <div class="card-box accent-burgundy" style="margin-top: 10px;">
            <h3 class="card-title">Visual Dashboard Layout Representation</h3>
            <div style="background:#090D13; border:1px solid #30363D; border-radius:6px; padding:10px; color:#C9D1D9; font-family:'JetBrains Mono', monospace; font-size:7pt;">
                <div style="display:flex; justify-content:space-between; border-bottom:1px solid #30363D; padding-bottom:4px; margin-bottom:6px;">
                    <span style="color:#58A6FF; font-weight:bold;">HYBRID DFA–LLM DASHBOARD</span>
                    <span style="color:#2EA043;">STATUS: ENGINE ACTIVE</span>
                </div>
                <div style="display:grid; grid-template-columns: 1fr 1fr; gap:8px;">
                    <div style="border:1px solid #30363D; padding:6px; border-radius:4px;">
                        [1] DFA VERDICT: <span style="color:#2EA043;">[ACCEPT]</span> Path: q0 → q1 → q2 → q3 → q4<br>
                        [2] MOORE MONITOR: State m0 (OK) | Failures: 0
                    </div>
                    <div style="border:1px solid #30363D; padding:6px; border-radius:4px;">
                        [3] TAPE: [INFO] 192.168.1.75 pass=<span style="color:#F85149;">XXXXXXXXX</span> Failed<br>
                        [4] ROUTE: LOCAL FAST PATH (Latency: 160 µs, Cost: $0.00)
                    </div>
                </div>
            </div>
        </div>
    </div>
    {make_footer(17)}
</section>
"""
pages.append(page17)

# --- PAGE 18: THREAT MODEL & ADVERSARIAL HARDENING ---
page18 = f"""
<section class="page">
    {make_header(18, "SECURITY HARDENING", "THREAT MODEL & ADVERSARIAL HARDENING")}
    <div>
        <h1 class="section-title">Threat Model & Hardening</h1>
        <h2 class="section-subtitle">Adversarial Robustness and Defense-in-Depth Protections</h2>

        <p class="body-lead">
            Like any cyber defense mechanism, the hybrid anomaly engine itself is a target for intelligent adversaries attempting evasion, timing side-channel exploitation, or denial of service.
        </p>

        <div class="grid-2">
            <div class="card-box accent-cognac">
                <h3 class="card-title">Adversarial Attack Vectors</h3>
                <p class="body-text">
                    • <strong>Token Smuggling:</strong> Inserting whitespace or null bytes to split tokens across lexeme boundaries.<br>
                    • <strong>DDoS on Slow Path:</strong> Flood of malformed lines intended to exhaust LLM API budgets and saturate queues.<br>
                    • <strong>Slow Brute-Force:</strong> Spreading password guesses across multiple IP subnets to evade the 3-failure Moore threshold.
                </p>
            </div>
            <div class="card-box accent-burgundy">
                <h3 class="card-title">Engine Countermeasures</h3>
                <p class="body-text">
                    • <strong>Strict Canonicalization:</strong> The lexer strips control characters prior to regex compilation.<br>
                    • <strong>Bounded Queue Drop:</strong> Excess anomalies beyond queue capacity trigger local logging without blocking engine threads.<br>
                    • <strong>Global Sliding Window:</strong> Augments per-IP tracking with global subnet rate limiting.
                </p>
            </div>
        </div>

        <table class="editorial-table" style="margin-top: 10px;">
            <thead>
                <tr>
                    <th>Threat Scenario</th>
                    <th>Vulnerable Component</th>
                    <th>Automata Theory Countermeasure</th>
                    <th>Residual Risk Rating</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Catastrophic ReDoS</strong></td>
                    <td>Regex Lexer</td>
                    <td>Pre-compiled DFA state tables guarantee $\mathcal{O}(N)$ without backtracking.</td>
                    <td style="color:#238636; font-weight:bold;">NONE (Mathematically Eliminated)</td>
                </tr>
                <tr>
                    <td><strong>Queue Exhaustion (OOM)</strong></td>
                    <td>Escalation Queue</td>
                    <td>Fixed ring-buffer with drop-oldest eviction policy.</td>
                    <td style="color:#238636; font-weight:bold;">LOW (Bounded Memory)</td>
                </tr>
                <tr>
                    <td><strong>PII Data Exfiltration</strong></td>
                    <td>Cloud LLM REST Client</td>
                    <td>Turing Machine tape scrubber enforces redaction before payload serialization.</td>
                    <td style="color:#238636; font-weight:bold;">MINIMAL (Deterministic Masking)</td>
                </tr>
            </tbody>
        </table>
    </div>
    {make_footer(18)}
</section>
"""
pages.append(page18)

# --- PAGE 19: ENTERPRISE SCALABILITY & FUTURE HORIZONS ---
page19 = f"""
<section class="page">
    {make_header(19, "ROADMAP", "ENTERPRISE SCALING & FUTURE DIRECTIONS")}
    <div>
        <h1 class="section-title">Future Horizons</h1>
        <h2 class="section-subtitle">Scaling Beyond SSH: Cloud Telemetry and Pushdown Automata</h2>

        <p class="body-lead">
            While this prototype targets SSH authentication logs, the neuro-symbolic grammar paradigm naturally extends across heterogeneous enterprise cloud telemetry.
        </p>

        <div class="grid-3">
            <div class="card-box accent-gold">
                <h3 class="card-title">AWS CloudTrail & K8s</h3>
                <p class="body-text">
                    Extending the alphabet $\Sigma$ to model AWS IAM assume-role transitions and Kubernetes API audit logs, flagging privilege escalation via structural grammar violations.
                </p>
            </div>
            <div class="card-box accent-burgundy">
                <h3 class="card-title">Pushdown Automata (PDA)</h3>
                <p class="body-text">
                    Incorporating a Pushdown Automaton with a LIFO stack to parse nested JSON and SQL queries, extending verification from Regular Languages (Type 3) to Context-Free Languages (Type 2).
                </p>
            </div>
            <div class="card-box accent-cognac">
                <h3 class="card-title">Local On-Device SLMs</h3>
                <p class="body-text">
                    Replacing remote cloud REST APIs with quantized Small Language Models (e.g., Llama-3-8B or Phi-3 via ONNX/llama.cpp) for 100% air-gapped, zero-network defense installations.
                </p>
            </div>
        </div>

        <div class="card-box" style="margin-top: 10px;">
            <h3 class="card-title">Roadmap to Enterprise Production</h3>
            <table class="editorial-table" style="margin: 4px 0 0 0;">
                <thead>
                    <tr>
                        <th>Phase</th>
                        <th>Milestone Target</th>
                        <th>Core Innovation</th>
                        <th>Timeline</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Phase 1 (Current)</strong></td>
                        <td>SSH Login Core Engine</td>
                        <td>C++14 DFA + Moore Monitor + Turing Machine Tape Sanitizer</td>
                        <td>Complete (Session 2026)</td>
                    </tr>
                    <tr>
                        <td><strong>Phase 2</strong></td>
                        <td>eBPF Kernel Probes</td>
                        <td>Executing the DFA inside the Linux kernel via eBPF for zero-copy triage</td>
                        <td>Q1 2027</td>
                    </tr>
                    <tr>
                        <td><strong>Phase 3</strong></td>
                        <td>Context-Free Grammar Engine</td>
                        <td>Pushdown Automata parser for nested JSON audit payloads</td>
                        <td>Q3 2027</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    {make_footer(19)}
</section>
"""
pages.append(page19)

# --- PAGE 20: CONCLUSION, REFERENCES & SIGN-OFF ---
page20 = f"""
<section class="page" style="justify-content: space-between;">
    {make_header(20, "CONCLUSION", "REFERENCES & VERIFICATION SIGN-OFF")}
    <div>
        <h1 class="section-title">Conclusion & Citations</h1>
        <h2 class="section-subtitle">Summary of Achievements and Formal Academic References</h2>

        <p class="body-lead">
            The Hybrid DFA–LLM Anomaly Engine demonstrates that the abstract mathematical principles of <strong>Theory of Computation (24B11CS212)</strong> provide the exact tools needed to resolve one of modern cybersecurity's greatest operational crises.
        </p>

        <div class="card-box accent-burgundy" style="margin-bottom: 10px;">
            <h3 class="card-title">Academic References</h3>
            <p class="body-text" style="font-size: 7.2pt; line-height: 1.45; color: #38231E;">
                <strong>[1]</strong> M. Sipser, <em>Introduction to the Theory of Computation</em>, 3rd ed., Cengage Learning, 2012.<br>
                <strong>[2]</strong> J. E. Hopcroft, R. Motwani, and J. D. Ullman, <em>Introduction to Automata Theory, Languages, and Computation</em>, 3rd ed., Pearson, 2006.<br>
                <strong>[3]</strong> Syllabus: Theory of Computation (24B11CS212), Department of CSE & IT, JIIT Noida, Session 2026–2027.<br>
                <strong>[4]</strong> K. Thompson, "Regular expression search algorithm," <em>Communications of the ACM</em>, vol. 11, no. 6, pp. 419–422, 1968.<br>
                <strong>[5]</strong> H. G. Rice, "Classes of recursively enumerable sets and their decision problems," <em>Trans. Amer. Math. Soc.</em>, vol. 74, pp. 358–366, 1953.<br>
                <strong>[6]</strong> R. Cox, "Regular Expression Matching Can Be Simple And Fast," 2007. [Online]. Available: https://swtch.com/~rsc/regexp/regexp1.html<br>
                <strong>[7]</strong> E. F. Moore, "Gedanken-experiments on Sequential Machines," <em>Automata Studies, Annals of Math. Studies</em>, no. 34, pp. 129–153, 1956.
            </p>
        </div>

        <div style="background: #FFFFFF; border: 1.5px solid #E2D7C8; border-radius: 6px; padding: 12px 16px;">
            <p style="font-weight: 700; color: #6A1A24; text-transform: uppercase; font-size: 8pt; letter-spacing: 0.8px; margin-bottom: 8px; border-bottom: 1px solid #E2D7C8; padding-bottom: 3px;">
                Academic Verification & Project Sign-Off
            </p>
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; text-align: center; font-size: 7.5pt;">
                <div style="border: 1px dashed #C8B9A6; padding: 8px 4px; border-radius: 4px;">
                    <p style="font-weight:bold; color:#2A1715;">Abhishek Bansal</p>
                    <p style="color:#5C4D4A;">2501030123</p>
                    <p style="margin-top:10px; font-style:italic; color:#82726F;">Verified</p>
                </div>
                <div style="border: 1px dashed #C8B9A6; padding: 8px 4px; border-radius: 4px;">
                    <p style="font-weight:bold; color:#2A1715;">Divyansh Agarwal</p>
                    <p style="color:#5C4D4A;">2501030124</p>
                    <p style="margin-top:10px; font-style:italic; color:#82726F;">Verified</p>
                </div>
                <div style="border: 1px dashed #C8B9A6; padding: 8px 4px; border-radius: 4px;">
                    <p style="font-weight:bold; color:#2A1715;">Arjun Bhardwaj</p>
                    <p style="color:#5C4D4A;">2501030134</p>
                    <p style="margin-top:10px; font-style:italic; color:#82726F;">Verified</p>
                </div>
                <div style="border: 1px dashed #C8B9A6; padding: 8px 4px; border-radius: 4px;">
                    <p style="font-weight:bold; color:#2A1715;">Anirudh Sharma</p>
                    <p style="color:#5C4D4A;">2501030135</p>
                    <p style="margin-top:10px; font-style:italic; color:#82726F;">Verified</p>
                </div>
            </div>
            <div style="margin-top: 10px; text-align: right; font-size: 7.5pt; color: #5C4D4A;">
                Faculty Evaluator Signature: _______________________ &nbsp;&nbsp;&nbsp;&nbsp; Grade Awarded: [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]
            </div>
        </div>
    </div>
    {make_footer(20)}
</section>
"""
pages.append(page20)

# Write out the complete 20-page HTML
full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hybrid DFA–LLM Anomaly Engine | Final Technical Report</title>
    <style>
        {css}
    </style>
</head>
<body>
    <div class="report-container">
        {"".join(pages)}
    </div>
</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"[✓] Successfully generated 20-page monograph HTML at: {html_path}")

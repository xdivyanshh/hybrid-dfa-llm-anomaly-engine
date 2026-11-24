import os
import base64

report_dir = r"C:\Users\Ritesh Kumar Agarwal\.gemini\antigravity\scratch\hybrid-anomaly-engine\report"
pages_dir = os.path.join(report_dir, "canva_pages")
assets_dir = os.path.join(report_dir, "assets")
os.makedirs(pages_dir, exist_ok=True)

def b64_img(filename):
    path = os.path.join(assets_dir, filename)
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    ext = os.path.splitext(filename)[1].lower().replace(".", "")
    mime = "image/jpeg" if ext in ["jpg", "jpeg"] else "image/png"
    return f"data:{mime};base64,{data}"

corridor_b64 = b64_img("server_corridor.jpg")
racks_b64 = b64_img("server_racks.jpg")
jiit_b64 = b64_img("jiit_logo.png")

def top_hdr(left="JIIT NOIDA • CSE DEPARTMENT", right="THEORY OF COMPUTATION (24B11CS212)"):
    return f"""<div class="canva-top-header"><span>{left}</span><span>{right}</span></div>"""

def btm_bar(left="ACADEMIC RESEARCH MONOGRAPH", right="THEORY OF COMPUTATION • CSE-24B11CS212"):
    return f"""<div class="canva-bottom-bar"><span>{left}</span><span>{right}</span></div>"""

def btm_bar_cream(left="ACADEMIC RESEARCH MONOGRAPH", right="THEORY OF COMPUTATION • CSE-24B11CS212"):
    return f"""<div class="canva-bottom-bar-cream"><span>{left}</span><span>{right}</span></div>"""

# ==============================================================================
# PAGE 1: TITLE & COVER PAGE (1:1 DoorDash Architecture & Content Structure)
# ==============================================================================
p1 = f"""<section class="page theme-dark" id="page-1" style="padding: 7mm 11mm 7mm 11mm; display: flex; flex-direction: column; justify-content: space-between;">
    <div class="cover-frame" style="border: 2px solid var(--gold); border-radius: 6px; padding: 6mm 10mm 5mm 10mm; display: flex; flex-direction: column; justify-content: space-between; height: 100%; box-sizing: border-box; background: rgba(30, 15, 14, 0.85); box-shadow: inset 0 0 40px rgba(0,0,0,0.6);">
        
        <!-- Top Institutional Header -->
        <div style="text-align: center; border-bottom: 2px solid var(--wine-red); padding-bottom: 3mm;">
            <h1 style="font-family: 'Cinzel', serif; font-size: 20px; font-weight: 800; color: var(--gold-light); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 2px; line-height: 1.2;">
                Jaypee Institute of Information Technology
            </h1>
            <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 10px; font-weight: 600; color: var(--gold); letter-spacing: 0.4px; margin-bottom: 2px;">
                Declared Deemed to be University Under Section 3 of UGC Act &bull; A-10, Sector-62, Noida
            </div>
            <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 11px; font-weight: 800; color: var(--text-cream); letter-spacing: 0.8px; text-transform: uppercase;">
                Department of Computer Science &amp; Engineering
            </div>
        </div>

        <!-- Hero Logos Block: High-Res JIIT Emblem Plaque + Official Neuro-Symbolic Engine Insignia Plaque -->
        <div style="display: flex; justify-content: center; align-items: center; gap: 32px; margin: 3mm 0 2mm 0;">
            <!-- Highly Legible White Card Plaque for JIIT Emblem -->
            <div style="background: #FFFFFF; border-radius: 12px; padding: 10px 16px; display: flex; align-items: center; justify-content: center; border: 2px solid var(--gold); box-shadow: 0 6px 25px rgba(0,0,0,0.55), 0 0 15px rgba(197, 159, 122, 0.25);">
                <img src="{jiit_b64}" alt="JIIT Emblem" style="height: 128px; width: auto; object-fit: contain; display: block;" />
            </div>

            <!-- Elegant Divider Line -->
            <div style="width: 2px; height: 110px; background: rgba(197, 159, 122, 0.45); border-radius: 2px;"></div>

            <!-- Official Project Insignia Plaque (Matching Symmetrical Frame) -->
            <div style="background: #251312; border-radius: 12px; padding: 14px 22px; display: flex; align-items: center; gap: 20px; border: 2px solid var(--gold); box-shadow: 0 6px 25px rgba(0,0,0,0.55), 0 0 15px rgba(128, 24, 24, 0.35);">
                <svg width="94" height="94" viewBox="0 0 80 80" fill="none" style="flex-shrink: 0; filter: drop-shadow(0 4px 14px rgba(128, 24, 24, 0.5));">
                    <circle cx="40" cy="40" r="38" stroke="#C59F7A" stroke-width="2.2" fill="#1E0F0E" />
                    <circle cx="40" cy="40" r="32" stroke="#801818" stroke-width="1.8" stroke-dasharray="4,3" fill="none" />
                    <!-- Automaton States and Transitions -->
                    <circle cx="26" cy="40" r="10.5" stroke="#DFC4A8" stroke-width="2" fill="#281514" />
                    <text x="26" y="44.5" fill="#DFC4A8" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="bold" text-anchor="middle">q₀</text>
                    <circle cx="54" cy="40" r="10.5" stroke="#68D391" stroke-width="2" fill="#281514" />
                    <circle cx="54" cy="40" r="7.8" stroke="#68D391" stroke-width="1.4" fill="none" />
                    <text x="54" y="44.5" fill="#68D391" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="bold" text-anchor="middle">q₁</text>
                    <!-- Transition Arrow -->
                    <path d="M 36 33.5 Q 40 25 44 33.5" fill="none" stroke="#C59F7A" stroke-width="2.2" />
                    <polygon points="46,34 41,30.5 47,29.5" fill="#C59F7A" />
                    <text x="40" y="23" fill="#C59F7A" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" text-anchor="middle">&delta;</text>
                </svg>
                <div style="text-align: left;">
                    <div style="font-family: 'Cinzel', serif; font-size: 24px; font-weight: 800; color: var(--gold-light); letter-spacing: 2px; line-height: 1.15;">
                        HYBRID DFA–LLM
                    </div>
                    <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 13px; font-weight: 800; color: #E53E3E; letter-spacing: 4px; text-transform: uppercase; margin-top: 2px;">
                        ANOMALY ENGINE
                    </div>
                    <div style="font-family: 'JetBrains Mono', monospace; font-size: 9.5px; color: var(--gold); letter-spacing: 1.5px; margin-top: 3px;">
                        NEURO-SYMBOLIC COMPILATION
                    </div>
                </div>
            </div>
        </div>

        <!-- Pill Badge Header -->
        <div style="text-align: center; margin: 1mm 0 1.5mm 0;">
            <span style="background: var(--wine-red); color: #F5EFEB; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 9.5px; font-weight: 800; letter-spacing: 2px; text-transform: uppercase; padding: 4.5px 22px; border-radius: 20px; display: inline-block; border: 1px solid var(--gold); box-shadow: 0 2px 10px rgba(0,0,0,0.4);">
                Project-Based Learning (PBL) &bull; Technical Monograph &bull; Theory of Computation
            </span>
        </div>

        <!-- Grand Project Title -->
        <div style="text-align: center; margin: 1mm 0 2mm 0;">
            <h2 style="font-family: 'Playfair Display', serif; font-size: 36px; font-weight: 900; color: var(--gold-light); letter-spacing: 1.5px; line-height: 1.1; margin-bottom: 5px;">
                HYBRID DFA&ndash;LLM ANOMALY ENGINE
            </h2>
            <div style="font-family: 'Playfair Display', serif; font-size: 13.5px; font-style: italic; font-weight: 600; color: var(--gold); margin-bottom: 5px;">
                A High-Assurance Neuro-Symbolic Framework for Microsecond Telemetry Triage
            </div>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 9.5px; font-weight: 600; color: var(--text-cream-dim); letter-spacing: 0.6px;">
                Compiled C++14 DFA &bull; 4-State Moore Machine &bull; 7-Tuple Turing Tape Sanitizer &bull; Asynchronous LLM Neural Reasoning
            </div>
        </div>

        <!-- Course Credential Box -->
        <div style="background: var(--bg-dark-card); border: 1.5px solid var(--border-gold); border-radius: 6px; padding: 3.5mm 6mm; text-align: center; margin: 1mm 0 1.5mm 0; position: relative;">
            <!-- Credits Badge -->
            <div style="position: absolute; right: 14px; top: 50%; transform: translateY(-50%); background: #1E0F0E; border: 1px solid var(--border-gold); border-radius: 8px; padding: 4px 10px; text-align: center;">
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 14px; font-weight: bold; color: var(--gold-light); line-height: 1;">3</div>
                <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 7px; font-weight: 700; color: var(--gold); text-transform: uppercase; letter-spacing: 1px;">Credits</div>
            </div>

            <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 9px; font-weight: 800; text-transform: uppercase; letter-spacing: 1.5px; color: var(--gold); margin-bottom: 2px;">
                Submitted In Partial Fulfillment of Requirements for Course:
            </div>
            <div style="font-family: 'Playfair Display', serif; font-size: 17px; font-weight: 800; color: #FFFFFF; margin-bottom: 2px;">
                Theory of Computation &bull; Course Code: 24B11CS212
            </div>
            <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 10px; font-weight: 600; color: var(--text-cream-dim);">
                Bachelor of Technology in Computer Science &amp; Engineering &bull; 2nd Year, 4th Semester (PBL)
            </div>
        </div>

        <!-- Bottom Student & Mentor Card Block (4 Columns) -->
        <div style="background: var(--bg-dark-card); border: 1.5px solid var(--border-gold); border-radius: 6px; padding: 3.5mm 5mm; box-sizing: border-box;">
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 10px; margin-bottom: 3mm; border-bottom: 1px solid rgba(197, 159, 122, 0.25); padding-bottom: 2.5mm;">
                <!-- Student 1: Abhishek Bansal -->
                <div style="border-left: 3px solid var(--wine-red); padding-left: 7px;">
                    <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 8px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.8px; color: var(--gold);">Submitted By:</div>
                    <div style="font-family: 'Playfair Display', serif; font-size: 12.5px; font-weight: 800; color: #FFFFFF;">Abhishek Bansal</div>
                    <div style="font-family: 'JetBrains Mono', monospace; font-size: 9px; font-weight: 600; color: var(--gold-light);">Enrolment: 2501030123</div>
                    <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 7.5px; color: var(--text-muted);">DFA Grammar &amp; Parser Lead</div>
                </div>

                <!-- Student 2: Divyansh Agarwal -->
                <div style="border-left: 3px solid var(--gold); padding-left: 7px;">
                    <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 8px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.8px; color: var(--gold-light);">Submitted By (Lead):</div>
                    <div style="font-family: 'Playfair Display', serif; font-size: 12.5px; font-weight: 800; color: #FFFFFF;">Divyansh Agarwal</div>
                    <div style="font-family: 'JetBrains Mono', monospace; font-size: 9px; font-weight: 600; color: var(--gold-light);">Enrolment: 2501030124</div>
                    <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 7.5px; color: var(--text-muted);">Systems &amp; Architecture Lead</div>
                </div>

                <!-- Student 3: Arjun Bhardwaj -->
                <div style="border-left: 3px solid var(--wine-red); padding-left: 7px;">
                    <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 8px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.8px; color: var(--gold);">Submitted By:</div>
                    <div style="font-family: 'Playfair Display', serif; font-size: 12.5px; font-weight: 800; color: #FFFFFF;">Arjun Bhardwaj</div>
                    <div style="font-family: 'JetBrains Mono', monospace; font-size: 9px; font-weight: 600; color: var(--gold-light);">Enrolment: 2501030134</div>
                    <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 7.5px; color: var(--text-muted);">Moore Transducer Lead</div>
                </div>

                <!-- Student 4: Anirudh Sharma -->
                <div style="border-left: 3px solid var(--gold); padding-left: 7px;">
                    <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 8px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.8px; color: var(--gold-light);">Submitted By:</div>
                    <div style="font-family: 'Playfair Display', serif; font-size: 12.5px; font-weight: 800; color: #FFFFFF;">Anirudh Sharma</div>
                    <div style="font-family: 'JetBrains Mono', monospace; font-size: 9px; font-weight: 600; color: var(--gold-light);">Enrolment: 2501030135</div>
                    <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 7.5px; color: var(--text-muted);">Turing Machine Sanitizer</div>
                </div>
            </div>

            <!-- Faculty Mentor & Institutional Sub-Strip -->
            <div style="display: flex; justify-content: space-between; align-items: center; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 9.5px;">
                <div>
                    <span style="font-weight: 800; color: var(--gold); text-transform: uppercase; font-size: 8px; letter-spacing: 0.8px; display: block;">Course Faculty &amp; Project Mentor:</span>
                    <span style="font-family: 'Playfair Display', serif; font-weight: 800; font-size: 12px; color: #FFFFFF;">Ms. Kirti Aggarwal</span>
                    <div style="color: var(--text-muted); font-size: 8.5px; margin-top: 1px;">Department of Computer Science &amp; Engineering &bull; JIIT Noida</div>
                </div>
                <div style="text-align: right; color: var(--text-cream-dim); font-size: 9px;">
                    <div><strong>Academic Session:</strong> 2026–2027 &bull; <strong>Batch:</strong> B2 &bull; <strong>Sem:</strong> 4th</div>
                    <div style="color: var(--text-muted); font-size: 8px; margin-top: 1px;">Sector-62, Noida, Uttar Pradesh – 201309</div>
                </div>
            </div>
        </div>

    </div>
</section>"""
with open(os.path.join(pages_dir, "page_1.html"), "w", encoding="utf-8") as f: f.write(p1)

# ==============================================================================
# PAGE 2: EXECUTIVE SUMMARY (Zero Clipping on Bottom Bar, Arched Photo Layout)
# ==============================================================================
p2 = f"""<section class="page theme-dark">
    {top_hdr("HYBRID DFA–LLM ANOMALY ENGINE", "THEORY OF COMPUTATION (24B11CS212)")}
    <div class="page-content" style="padding-top: 5mm; padding-bottom: 4mm; gap: 12px;">
        <div style="display: grid; grid-template-columns: 1.05fr 1.15fr; gap: 24px; height: 100%; align-items: stretch;">
            
            <!-- Left Column: Title, Substantial Text, Stat Pills (1:1 Canva Layout) -->
            <div style="display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div class="gold-eyebrow">ACADEMIC SYNOPSIS &amp; DISSERTATION</div>
                    <h1 class="canva-title" style="font-size: 34pt; line-height: 1.05; margin-bottom: 8px;">
                        EXECUTIVE<br>SUMMARY
                    </h1>
                    <div class="gold-separator-line" style="margin: 6px 0 10px 0;"></div>

                    <p class="canva-body" style="font-size: 9.8pt; line-height: 1.62; margin-bottom: 10px;">
                        Throughout enterprise cloud environments, cybersecurity operations centers (SOCs) face severe operational bottlenecks driven by unprecedented telemetry volume. Modern distributed server infrastructure routinely generates hundreds of thousands of authentication log records per second, creating an acute data triage crisis that overwhelms human analysts and legacy SIEM architectures.
                    </p>

                    <p class="canva-body" style="font-size: 9.8pt; line-height: 1.62; margin-bottom: 10px;">
                        Routing this uncurated telemetry stream directly to generative Large Language Models is cost-prohibitive, introduces multiple seconds of network latency, exposes private network perimeters and credentials over third-party APIs, and triggers catastrophic HTTP 429 rate limit outages during active distributed denial-of-service or credential stuffing attacks.
                    </p>

                    <p class="canva-body" style="font-size: 9.8pt; line-height: 1.62; margin-bottom: 10px;">
                        Entering production deployment, this project establishes a high-performance dual-lane neuro-symbolic engine. A compiled C++14 Deterministic Finite Automaton (DFA) inspects routine log grammar in <strong>1.8 microseconds</strong> with zero backtracking, accompanied by a 4-state Moore Machine session monitor. Only genuine structural anomalies escalate to cloud AI, where a 7-tuple Turing Machine tape sanitizer first deterministically scrubs sensitive credentials.
                    </p>
                </div>

                <!-- Bottom Stat Capsules -->
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 6px;">
                    <div class="stat-pill" style="padding: 10px 12px;">
                        <div class="num" style="font-size: 24pt;">1.8 &mu;s</div>
                        <div class="lbl" style="font-size: 8pt; margin-top:2px;">Fast-Path Latency</div>
                    </div>
                    <div class="stat-pill" style="padding: 10px 12px;">
                        <div class="num" style="font-size: 24pt;">98.4%</div>
                        <div class="lbl" style="font-size: 8pt; margin-top:2px;">API Cost Reduction</div>
                    </div>
                </div>
            </div>

            <!-- Right Column: The Signature Arched Photo Frame (1:1 Canva Template) -->
            <div class="canva-arch-photo" style="height: 100%; display: flex; flex-direction: column;">
                <img src="{corridor_b64}" alt="Enterprise Datacenter Server Infrastructure" style="width: 100%; height: 100%; object-fit: cover; flex: 1; min-height: 0;" />
                <div class="canva-photo-overlay">
                    <span style="font-family: 'Cinzel', serif; font-size: 8.5pt; color: var(--gold-light); letter-spacing: 2px; text-transform: uppercase; font-weight: bold; display: block; margin-bottom: 4px;">
                        FIGURE 1: ENTERPRISE TELEMETRY INFRASTRUCTURE
                    </span>
                    <span style="font-size: 8pt; color: var(--text-cream-dim); line-height: 1.45; display: block;">
                        Unfiltered cloud LLM inference creates severe thermal saturation and compute starvation in server clusters. The Hybrid Engine resolves 95.2% on local CPUs at line-rate.
                    </span>
                </div>
            </div>

        </div>
    </div>
    {btm_bar("EXECUTIVE RESEARCH SYNOPSIS", "DISSERTATION OVERVIEW • SECTION 1.0")}
</section>"""
with open(os.path.join(pages_dir, "page_2.html"), "w", encoding="utf-8") as f: f.write(p2)

# ==============================================================================
# PAGE 3: PROJECT OVERVIEW & MONOGRAPH MAP (Completely Filled, Rich Sub-Descriptions!)
# ==============================================================================
p3 = f"""<section class="page theme-cream">
    {top_hdr("PROJECT BLUEPRINT", "RESEARCH DISSERTATION COMPENDIUM")}
    <div class="page-content" style="padding-top: 5mm; padding-bottom: 4mm; gap: 10px;">
        
        <div>
            <div class="gold-eyebrow" style="color: var(--wine-red);">DISSERTATION ARCHITECTURE</div>
            <div style="background: var(--wine-red); border-radius: 8px; padding: 10px 18px; margin-bottom: 2px; box-shadow: 0 4px 15px rgba(128, 24, 24, 0.2);">
                <h1 class="canva-title" style="color: #FFFFFF; font-size: 24pt; margin-bottom: 2px;">
                    PROJECT OVERVIEW &amp; DISSERTATION MAP
                </h1>
                <p style="font-size: 8.5pt; color: var(--gold-light); font-family: 'Cinzel', serif; letter-spacing: 2px; text-transform: uppercase;">
                    SYSTEMATIC STRUCTURAL MAP OF THE NEURO-SYMBOLIC ANOMALY ENGINE
                </p>
            </div>
        </div>

        <!-- Two Balanced Grid Cards Filling 100% of Space with Sub-Descriptions -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; flex: 1; align-items: stretch;">
            
            <!-- Left Card: Part I -->
            <div class="cream-card" style="display: flex; flex-direction: column; justify-content: flex-start; gap: 8px; border-top: 4px solid var(--wine-red); padding: 12px 16px;">
                <div>
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 12.5pt; color: var(--wine-red); margin-bottom: 2px; border-bottom: 1.5px solid rgba(128, 24, 24, 0.2); padding-bottom: 3px;">
                        Part I: Theory &amp; Automata Design
                    </h3>
                    <p style="font-size: 8pt; color: var(--text-dark-secondary); margin-bottom: 2px; font-style: italic;">
                        Foundational automata theory, formal grammars, deterministic state machines, and hardware memory mappings.
                    </p>
                </div>
                <div style="display: flex; flex-direction: column; gap: 4px; font-size: 8.3pt; color: var(--text-dark-secondary);">
                    <div style="border-bottom:1px dashed #DDD; padding-bottom:1.5px;">
                        <div style="display:flex; justify-content:space-between;"><span><strong>1. Executive Summary &amp; Architecture</strong></span><span style="font-weight:bold; color:var(--wine-red);">Page 2</span></div>
                        <div style="font-size:7.4pt; color:#666;">High-level system overview, dual-lane thesis, and empirical benchmarks.</div>
                    </div>
                    <div style="border-bottom:1px dashed #DDD; padding-bottom:1.5px;">
                        <div style="display:flex; justify-content:space-between;"><span><strong>2. Project Overview &amp; Monograph Map</strong></span><span style="font-weight:bold; color:var(--wine-red);">Page 3</span></div>
                        <div style="font-size:7.4pt; color:#666;">Complete 20-page compendium roadmap and formal taxonomy.</div>
                    </div>
                    <div style="border-bottom:1px dashed #DDD; padding-bottom:1.5px;">
                        <div style="display:flex; justify-content:space-between;"><span><strong>3. The Log Deluge: Server Thermal Load</strong></span><span style="font-weight:bold; color:var(--wine-red);">Page 4</span></div>
                        <div style="font-size:7.4pt; color:#666;">High-velocity log ingestion challenges, server thermal bottlenecks, and token burn.</div>
                    </div>
                    <div style="border-bottom:1px dashed #DDD; padding-bottom:1.5px;">
                        <div style="display:flex; justify-content:space-between;"><span><strong>4. The Algorithmic Dilemma: Rules vs LLMs</strong></span><span style="font-weight:bold; color:var(--wine-red);">Page 5</span></div>
                        <div style="font-size:7.4pt; color:#666;">ReDoS vulnerability of regex vs computational collapse of pure LLM triage.</div>
                    </div>
                    <div style="border-bottom:1px dashed #DDD; padding-bottom:1.5px;">
                        <div style="display:flex; justify-content:space-between;"><span><strong>5. Formal Foundations: Chomsky Hierarchy</strong></span><span style="font-weight:bold; color:var(--wine-red);">Page 6</span></div>
                        <div style="font-size:7.4pt; color:#666;">Type-3 regular grammar proof and O(N) linear time verification theorems.</div>
                    </div>
                    <div style="border-bottom:1px dashed #DDD; padding-bottom:1.5px;">
                        <div style="display:flex; justify-content:space-between;"><span><strong>6. Dual-Lane Engine Blueprint &amp; Latencies</strong></span><span style="font-weight:bold; color:var(--wine-red);">Page 7</span></div>
                        <div style="font-size:7.4pt; color:#666;">End-to-end pipeline topology, 5-stage latency waterfall, and system invariants.</div>
                    </div>
                    <div style="border-bottom:1px dashed #DDD; padding-bottom:1.5px;">
                        <div style="display:flex; justify-content:space-between;"><span><strong>7. The Symbolic Fast Path: Lexer Grammar</strong></span><span style="font-weight:bold; color:var(--wine-red);">Page 8</span></div>
                        <div style="font-size:7.4pt; color:#666;">POSIX string-view lexer tokenizing 5 core severity and payload primitives.</div>
                    </div>
                    <div style="border-bottom:1px dashed #DDD; padding-bottom:1.5px;">
                        <div style="display:flex; justify-content:space-between;"><span><strong>8. Minimal Baseline DFA Formulation</strong></span><span style="font-weight:bold; color:var(--wine-red);">Page 9</span></div>
                        <div style="font-size:7.4pt; color:#666;">5-tuple automaton definition, 6 states, and inescapable error sink qE.</div>
                    </div>
                    <div style="border-bottom:1px dashed #DDD; padding-bottom:1.5px;">
                        <div style="display:flex; justify-content:space-between;"><span><strong>9. Total Transition Matrix &amp; Minimality Proof</strong></span><span style="font-weight:bold; color:var(--wine-red);">Page 10</span></div>
                        <div style="font-size:7.4pt; color:#666;">Myhill-Nerode equivalence theorem and 30-byte L1 cache realization.</div>
                    </div>
                    <div>
                        <div style="display:flex; justify-content:space-between;"><span><strong>10. Stateful Session Tracking: Moore Transducer</strong></span><span style="font-weight:bold; color:var(--wine-red);">Page 11</span></div>
                        <div style="font-size:7.4pt; color:#666;">4-state temporal transducer tracking brute force and threshold escalation.</div>
                    </div>
                </div>
            </div>

            <!-- Right Card: Part II -->
            <div class="cream-card" style="display: flex; flex-direction: column; justify-content: flex-start; gap: 8px; border-top: 4px solid var(--wine-red); padding: 12px 16px;">
                <div>
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 12.5pt; color: var(--wine-red); margin-bottom: 2px; border-bottom: 1.5px solid rgba(128, 24, 24, 0.2); padding-bottom: 3px;">
                        Part II: Engineering &amp; Evaluation
                    </h3>
                    <p style="font-size: 8pt; color: var(--text-dark-secondary); margin-bottom: 2px; font-style: italic;">
                        Turing data privacy, lock-free concurrency, empirical benchmarks, financial TCO models, and SIEM integrations.
                    </p>
                </div>
                <div style="display: flex; flex-direction: column; gap: 4px; font-size: 8.3pt; color: var(--text-dark-secondary);">
                    <div style="border-bottom:1px dashed #DDD; padding-bottom:1.5px;">
                        <div style="display:flex; justify-content:space-between;"><span><strong>11. Data Privacy: 7-Tuple Turing Sanitizer</strong></span><span style="font-weight:bold; color:var(--wine-red);">Page 12</span></div>
                        <div style="font-size:7.4pt; color:#666;">Deterministic in-place tape manipulation masking passwords prior to egress.</div>
                    </div>
                    <div style="border-bottom:1px dashed #DDD; padding-bottom:1.5px;">
                        <div style="display:flex; justify-content:space-between;"><span><strong>12. Neural Escalation: Bounded Queue &amp; JSON</strong></span><span style="font-weight:bold; color:var(--wine-red);">Page 13</span></div>
                        <div style="font-size:7.4pt; color:#666;">Lock-free circular buffer (K=1k) and structured Gemini 2.5 Flash schema.</div>
                    </div>
                    <div style="border-bottom:1px dashed #DDD; padding-bottom:1.5px;">
                        <div style="display:flex; justify-content:space-between;"><span><strong>13. Threat Taxonomy &amp; Detection Performance</strong></span><span style="font-weight:bold; color:var(--wine-red);">Page 14</span></div>
                        <div style="font-size:7.4pt; color:#666;">Empirical attack vector breakdown, accuracy (99.61%), and mitigation matrix.</div>
                    </div>
                    <div style="border-bottom:1px dashed #DDD; padding-bottom:1.5px;">
                        <div style="display:flex; justify-content:space-between;"><span><strong>14. SOC Command Center &amp; Live Triage</strong></span><span style="font-weight:bold; color:var(--wine-red);">Page 15</span></div>
                        <div style="font-size:7.4pt; color:#666;">Enterprise SIEM webhook streaming, automated firewalls, and explainable AI.</div>
                    </div>
                    <div style="border-bottom:1px dashed #DDD; padding-bottom:1.5px;">
                        <div style="display:flex; justify-content:space-between;"><span><strong>15. Empirical Evaluation: 100k EPS Benchmarks</strong></span><span style="font-weight:bold; color:var(--wine-red);">Page 16</span></div>
                        <div style="font-size:7.4pt; color:#666;">Commodity hardware stress tests, sub-2us latencies, and 4.2MB fixed memory.</div>
                    </div>
                    <div style="border-bottom:1px dashed #DDD; padding-bottom:1.5px;">
                        <div style="display:flex; justify-content:space-between;"><span><strong>16. Memory Complexity &amp; Cache Micro-Arch</strong></span><span style="font-weight:bold; color:var(--wine-red);">Page 17</span></div>
                        <div style="font-size:7.4pt; color:#666;">Valgrind Massif zero-heap verification and 64-byte CPU cache alignment.</div>
                    </div>
                    <div style="border-bottom:1px dashed #DDD; padding-bottom:1.5px;">
                        <div style="display:flex; justify-content:space-between;"><span><strong>17. Financial Economics: 98.4% Cost Collapse</strong></span><span style="font-weight:bold; color:var(--wine-red);">Page 18</span></div>
                        <div style="font-size:7.4pt; color:#666;">TCO analysis reducing annual cloud API expenses from $182k to $2.8k.</div>
                    </div>
                    <div style="border-bottom:1px dashed #DDD; padding-bottom:1.5px;">
                        <div style="display:flex; justify-content:space-between;"><span><strong>18. Industry SIEM Comparative Evaluation</strong></span><span style="font-weight:bold; color:var(--wine-red);">Page 19</span></div>
                        <div style="font-size:7.4pt; color:#666;">Feature-by-feature evaluation against Splunk, Elastic, and Microsoft Sentinel.</div>
                    </div>
                    <div style="border-bottom:1px dashed #DDD; padding-bottom:1.5px;">
                        <div style="display:flex; justify-content:space-between;"><span><strong>19. Future Horizon &amp; Autonomous Cyber Grid</strong></span><span style="font-weight:bold; color:var(--wine-red);">Page 20</span></div>
                        <div style="font-size:7.8pt; color:#666;">eBPF socket offload, FPGA hardware synthesis, and autonomic healing grids.</div>
                    </div>
                    <div>
                        <div style="display:flex; justify-content:space-between;"><span><strong>20. Bibliography &amp; Academic References</strong></span><span style="font-weight:bold; color:var(--wine-red);">Page 20</span></div>
                        <div style="font-size:7.4pt; color:#666;">8 peer-reviewed citations across formal computation and machine learning.</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Bottom Narrative Card -->
        <div class="cream-card" style="padding: 10px 16px; border-left: 4px solid var(--wine-red); background: #FAF7F2;">
            <p style="font-size: 8.8pt; color: var(--text-dark-secondary); line-height: 1.55; margin: 0;">
                <strong>Pedagogical Significance:</strong> This compendium demonstrates the practical applicability of formal language theory (Chomsky Hierarchy, Myhill-Nerode theorem, Turing computability) in solving real-world cybersecurity scalability, computational complexity, and zero-day threat detection challenges.
            </p>
        </div>

    </div>
    {btm_bar_cream("PROJECT BLUEPRINT & COMPENDIUM", "SECTION 1.1 • DISSERTATION TAXONOMY")}
</section>"""
with open(os.path.join(pages_dir, "page_3.html"), "w", encoding="utf-8") as f: f.write(p3)

# ==============================================================================
# PAGE 4: THE INGESTION STORM & SERVER THERMAL SATURATION (Arched Server Racks Photo)
# ==============================================================================
p4 = f"""<section class="page theme-dark">
    {top_hdr("PROBLEM CONTEXT", "THE ENTERPRISE TELEMETRY CRISIS")}
    <div class="page-content" style="padding-top: 5mm; padding-bottom: 4mm; gap: 12px;">
        <div style="display: grid; grid-template-columns: 1.1fr 1.0fr; gap: 24px; height: 100%; align-items: stretch;">
            
            <!-- Left Column: The Problem & Server Impact Narrative -->
            <div style="display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div class="gold-eyebrow">HIGH-VELOCITY TELEMETRY SATURATION</div>
                    <h1 class="canva-title" style="font-size: 30pt; line-height: 1.05; margin-bottom: 8px;">
                        THE LOG CRISIS &amp;<br>SERVER OVERLOAD
                    </h1>
                    <div class="gold-separator-line" style="margin: 6px 0 10px 0;"></div>

                    <p class="canva-body" style="font-size: 9.8pt; line-height: 1.65; margin-bottom: 10px;">
                        In enterprise datacenters, distributed microservices produce massive volumes of semi-structured text logs. A mid-sized infrastructure running Kubernetes clusters routinely emits over <strong>100,000 events per second (EPS)</strong>, equating to 8.6 billion log lines per 24-hour cycle.
                    </p>

                    <p class="canva-body" style="font-size: 9.8pt; line-height: 1.65; margin-bottom: 10px;">
                        When organizations attempt to feed raw telemetry directly into cloud LLM APIs, the relentless token querying triggers severe hardware penalties:
                    </p>

                    <div style="display: flex; flex-direction: column; gap: 8px;">
                        <div class="dark-card" style="padding: 10px 14px; border-left: 3px solid var(--wine-red);">
                            <strong style="color: #FFB2B2; font-size: 9pt;">1. Server CPU Thrashing &amp; Thermal Load:</strong>
                            <div style="font-size: 8.4pt; color: var(--text-cream-dim); line-height: 1.45; margin-top: 2px;">
                                TLS handshakes, HTTP connection pooling, and JSON serialization consume 85%+ CPU cycles on aggregator servers, causing server thermal throttling and hardware degradation.
                            </div>
                        </div>

                        <div class="dark-card" style="padding: 10px 14px; border-left: 3px solid var(--gold);">
                            <strong style="color: var(--gold-light); font-size: 9pt;">2. Socket Exhaustion &amp; Memory Leaks:</strong>
                            <div style="font-size: 8.4pt; color: var(--text-cream-dim); line-height: 1.45; margin-top: 2px;">
                                Cloud API latency spikes (800ms–2500ms) cause memory queues to balloon from 1,000 to over 500,000 pending requests, triggering out-of-memory (OOM) host kernel crashes.
                            </div>
                        </div>

                        <div class="dark-card" style="padding: 10px 14px; border-left: 3px solid var(--wine-red);">
                            <strong style="color: #FFB2B2; font-size: 9pt;">3. Relentless Token Burn ($90,000/Day):</strong>
                            <div style="font-size: 8.4pt; color: var(--text-cream-dim); line-height: 1.45; margin-top: 2px;">
                                100,000 EPS &times; 250 tokens/log = 25,000,000 tokens/sec. Cloud inference at this scale collapses budgets and breaches daily enterprise quotas within 20 minutes.
                            </div>
                        </div>
                    </div>
                </div>

                <div class="dark-card" style="background: rgba(35, 18, 17, 0.9); border: 1px solid var(--border-gold); padding: 10px 14px; text-align: center;">
                    <span style="font-family: 'Cinzel'; font-size: 8pt; color: var(--gold-light); letter-spacing: 1.5px;">
                        SYSTEM GOAL: FILTER 95%+ OF TELEMETRY LOCALLY BEFORE REACHING CLOUD APIS
                    </span>
                </div>
            </div>

            <!-- Right Column: Arched Window with BASE64 server_racks.jpg! -->
            <div class="canva-arch-photo" style="height: 100%; display: flex; flex-direction: column;">
                <img src="{racks_b64}" alt="High-Density Datacenter Server Racks" style="width: 100%; height: 100%; object-fit: cover; flex: 1; min-height: 0;" />
                <div class="canva-photo-overlay">
                    <span style="font-family: 'Cinzel', serif; font-size: 8.5pt; color: var(--gold-light); letter-spacing: 2px; text-transform: uppercase; font-weight: bold; display: block; margin-bottom: 4px;">
                        FIGURE 2: ENTERPRISE SERVER CLUSTER SATURATION
                    </span>
                    <span style="font-size: 8pt; color: var(--text-cream-dim); line-height: 1.45; display: block;">
                        High-density server racks face extreme power, thermal, and thread-contention bottlenecks when processing uncurated LLM API streams. Deterministic C++ automata offload 95.2% to edge cores.
                    </span>
                </div>
            </div>

        </div>
    </div>
    {btm_bar("INFRASTRUCTURE IMPACT ANALYSIS", "TELEMETRY SATURATION • FIGURE 2")}
</section>"""
with open(os.path.join(pages_dir, "page_4.html"), "w", encoding="utf-8") as f: f.write(p4)

# ==============================================================================
# PAGE 5: THE ALGORITHMIC DILEMMA (Tall Full-Height Visuals, Zero Dead Space!)
# ==============================================================================
p5 = f"""<section class="page theme-dark">
    {top_hdr("ALGORITHMIC COMPARISON", "RULES VS. LLM INFERENCE")}
    <div class="page-content" style="padding-top: 4mm; padding-bottom: 3mm; gap: 8px;">
        
        <div>
            <div class="gold-eyebrow">ARCHITECTURAL TRADE-OFF ANALYSIS</div>
            <h1 class="canva-title" style="font-size: 30pt; line-height: 1.05; margin-bottom: 4px;">
                THE ALGORITHMIC DILEMMA
            </h1>
            <p class="canva-body" style="font-size: 9.5pt; color: var(--text-cream-dim); max-width: 95%; margin-bottom: 8px; line-height: 1.5;">
                Modern security engineering is paralyzed between two flawed paradigms: brittle, regex-based rule engines vulnerable to ReDoS attacks, versus generative LLMs that exhaust server compute, breach privacy boundaries, and bankrupt operational budgets.
            </p>
        </div>

        <!-- 2-Column Split: Left = Red Capsules, Right = 2 Large Rich Charts -->
        <div style="display: grid; grid-template-columns: 1.02fr 1.18fr; gap: 18px; flex: 1; align-items: stretch;">
            
            <!-- Left Column: Key Targets / Specifications (Canva Red Capsule Pills) -->
            <div style="display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <span style="font-family: 'Cinzel', serif; font-size: 8.5pt; letter-spacing: 2px; color: var(--gold); text-transform: uppercase; font-weight: bold; display: block; margin-bottom: 8px;">
                        KEY ARCHITECTURAL BENCHMARKS
                    </span>

                    <div class="canva-capsule" style="padding: 7px 12px; margin-bottom: 5px;">
                        <span style="font-size: 8.5pt;">Deterministic DFA Latency:</span>
                        <span class="val" style="font-size: 8.5pt; font-weight: bold; color: #FFF;">1.8 &mu;s / event</span>
                    </div>

                    <div class="canva-capsule" style="padding: 7px 12px; margin-bottom: 5px;">
                        <span style="font-size: 8.5pt;">Pure LLM Inference Latency:</span>
                        <span class="val" style="font-size: 8.5pt; font-weight: bold; color: #FFB2B2;">840,000 &mu;s (466,000&times;)</span>
                    </div>

                    <div class="canva-capsule" style="padding: 7px 12px; margin-bottom: 5px;">
                        <span style="font-size: 8.5pt;">Local Edge Offload Ratio:</span>
                        <span class="val" style="font-size: 8.5pt; font-weight: bold; color: #68D391;">95.2% Resolved Locally</span>
                    </div>

                    <div class="canva-capsule" style="padding: 7px 12px; margin-bottom: 5px;">
                        <span style="font-size: 8.5pt;">ReDoS Vulnerability Risk:</span>
                        <span class="val" style="font-size: 8.5pt; font-weight: bold; color: #68D391;">Provably 0.0% (O(N) Bound)</span>
                    </div>

                    <div class="canva-capsule" style="padding: 7px 12px; margin-bottom: 5px;">
                        <span style="font-size: 8.5pt;">Credential Leakage Risk:</span>
                        <span class="val" style="font-size: 8.5pt; font-weight: bold; color: #68D391;">0.0% (TM Tape Redaction)</span>
                    </div>

                    <div class="canva-capsule" style="padding: 7px 12px; margin-bottom: 5px;">
                        <span style="font-size: 8.5pt;">Host Server CPU Savings:</span>
                        <span class="val" style="font-size: 8.5pt; font-weight: bold; color: #68D391;">88.5% Compute Reduction</span>
                    </div>
                </div>

                <div class="dark-card" style="padding: 9px 12px; background: rgba(35, 18, 17, 0.95); border: 1px solid var(--border-gold);">
                    <div style="font-size: 8.5pt; color: var(--text-cream-dim); line-height: 1.5;">
                        <strong style="color: var(--gold-light);">The Neuro-Symbolic Resolution:</strong> Combine the microsecond deterministic speed of finite automata with the zero-shot reasoning depth of Large Language Models.
                    </div>
                </div>
            </div>

            <!-- Right Column: Two Large Taller Charts -->
            <div style="display: flex; flex-direction: column; justify-content: space-between; gap: 10px;">
                
                <!-- Chart 1: Monthly Cost Comparison Bar Chart -->
                <div class="dark-card" style="flex: 1; padding: 10px 14px; display: flex; flex-direction: column; justify-content: space-between; background: #231211;">
                    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-gold); padding-bottom: 4px;">
                        <span style="font-family: 'Cinzel'; font-size: 8pt; color: var(--gold); font-weight: bold; letter-spacing: 1.2px;">
                            FIGURE 3A: MONTHLY OPERATING COST ($ USD)
                        </span>
                        <span style="font-size: 7.5pt; color: var(--text-cream-dim); font-family: 'JetBrains Mono';">100k EPS LOAD</span>
                    </div>

                    <svg viewBox="0 0 300 210" style="width: 100%; flex: 1; min-height: 0; display: block; margin-top: 2px;">
                        <!-- Grid Lines -->
                        <line x1="45" y1="30" x2="285" y2="30" stroke="rgba(197, 159, 122, 0.2)" stroke-width="1" />
                        <line x1="45" y1="65" x2="285" y2="65" stroke="rgba(197, 159, 122, 0.2)" stroke-width="1" />
                        <line x1="45" y1="100" x2="285" y2="100" stroke="rgba(197, 159, 122, 0.2)" stroke-width="1" />
                        <line x1="45" y1="135" x2="285" y2="135" stroke="rgba(197, 159, 122, 0.2)" stroke-width="1" />
                        <line x1="45" y1="170" x2="285" y2="170" stroke="rgba(197, 159, 122, 0.4)" stroke-width="1.5" />

                        <!-- Y-Axis labels -->
                        <text x="38" y="34" text-anchor="end" fill="#DFC4A8" font-size="9.5" font-family="JetBrains Mono" font-weight="bold">$15k</text>
                        <text x="38" y="69" text-anchor="end" fill="#DFC4A8" font-size="9.5" font-family="JetBrains Mono">$10k</text>
                        <text x="38" y="104" text-anchor="end" fill="#DFC4A8" font-size="9.5" font-family="JetBrains Mono">$5k</text>
                        <text x="38" y="139" text-anchor="end" fill="#DFC4A8" font-size="9.5" font-family="JetBrains Mono">$2k</text>
                        <text x="38" y="173" text-anchor="end" fill="#DFC4A8" font-size="9.5" font-family="JetBrains Mono">$0</text>

                        <!-- Bar 1: Pure LLM -->
                        <rect x="75" y="30" width="76" height="140" rx="5" fill="#F5EFEB" />
                        <text x="113" y="22" text-anchor="middle" fill="#FFFFFF" font-family="JetBrains Mono" font-size="11" font-weight="bold">$15,200</text>
                        <text x="113" y="188" text-anchor="middle" fill="#DFC4A8" font-family="Plus Jakarta Sans" font-size="10" font-weight="bold">Pure LLM</text>

                        <!-- Bar 2: Hybrid Engine -->
                        <rect x="180" y="160" width="76" height="10" rx="3" fill="#801818" stroke="#C59F7A" stroke-width="1.5" />
                        <text x="218" y="152" text-anchor="middle" fill="#68D391" font-family="JetBrains Mono" font-size="11" font-weight="bold">$240</text>
                        <text x="218" y="188" text-anchor="middle" fill="#68D391" font-family="Plus Jakarta Sans" font-size="10" font-weight="bold">Hybrid Engine</text>
                    </svg>
                </div>

                <!-- Chart 2: Latency Scalability Line Chart -->
                <div class="dark-card" style="flex: 1; padding: 10px 14px; display: flex; flex-direction: column; justify-content: space-between; background: #231211;">
                    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-gold); padding-bottom: 4px;">
                        <span style="font-family: 'Cinzel'; font-size: 8pt; color: var(--gold); font-weight: bold; letter-spacing: 1.2px;">
                            FIGURE 3B: LATENCY RESPONSE VS. LOG VOLUME
                        </span>
                        <span style="font-size: 7.5pt; color: var(--text-cream-dim); font-family: 'JetBrains Mono';">SCALING</span>
                    </div>

                    <svg viewBox="0 0 300 210" style="width: 100%; flex: 1; min-height: 0; display: block; margin-top: 2px;">
                        <!-- Grid Lines -->
                        <line x1="50" y1="30" x2="285" y2="30" stroke="rgba(197, 159, 122, 0.2)" stroke-width="1" />
                        <line x1="50" y1="65" x2="285" y2="65" stroke="rgba(197, 159, 122, 0.2)" stroke-width="1" />
                        <line x1="50" y1="100" x2="285" y2="100" stroke="rgba(197, 159, 122, 0.2)" stroke-width="1" />
                        <line x1="50" y1="135" x2="285" y2="135" stroke="rgba(197, 159, 122, 0.2)" stroke-width="1" />
                        <line x1="50" y1="170" x2="285" y2="170" stroke="rgba(197, 159, 122, 0.4)" stroke-width="1.5" />

                        <!-- Y-Labels -->
                        <text x="44" y="34" text-anchor="end" fill="#DFC4A8" font-size="9" font-family="JetBrains Mono" font-weight="bold">1000ms</text>
                        <text x="44" y="69" text-anchor="end" fill="#DFC4A8" font-size="9" font-family="JetBrains Mono">500ms</text>
                        <text x="44" y="104" text-anchor="end" fill="#DFC4A8" font-size="9" font-family="JetBrains Mono">200ms</text>
                        <text x="44" y="139" text-anchor="end" fill="#DFC4A8" font-size="9" font-family="JetBrains Mono">50ms</text>
                        <text x="44" y="173" text-anchor="end" fill="#DFC4A8" font-size="9" font-family="JetBrains Mono">0ms</text>

                        <!-- Pure LLM Latency Curve -->
                        <path d="M 65 150 Q 145 125 195 70 T 265 32" fill="none" stroke="#E53E3E" stroke-width="3.5" stroke-dasharray="5,3" />
                        <circle cx="265" cy="32" r="5" fill="#E53E3E" />
                        <text x="255" y="24" fill="#FFB2B2" font-size="9.5" font-family="JetBrains Mono" font-weight="bold" text-anchor="end">Pure LLM (840ms+)</text>

                        <!-- Hybrid Engine Flat Line -->
                        <line x1="65" y1="168" x2="265" y2="168" stroke="#68D391" stroke-width="3.5" />
                        <circle cx="265" cy="168" r="4.5" fill="#68D391" />
                        <text x="165" y="160" fill="#68D391" font-size="9" font-family="JetBrains Mono" font-weight="bold" text-anchor="middle">Hybrid Fast-Path (1.8 &mu;s)</text>

                        <!-- X-Labels -->
                        <text x="65" y="188" text-anchor="middle" fill="#DFC4A8" font-size="9.5" font-family="JetBrains Mono">10k EPS</text>
                        <text x="165" y="188" text-anchor="middle" fill="#DFC4A8" font-size="9.5" font-family="JetBrains Mono">50k EPS</text>
                        <text x="265" y="188" text-anchor="middle" fill="#DFC4A8" font-size="9.5" font-family="JetBrains Mono">100k EPS</text>
                    </svg>
                </div>

            </div>

        </div>

    </div>
    {btm_bar("ARCHITECTURAL BENCHMARKING", "RULES VS LLMS • SECTION 1.3")}
</section>"""
with open(os.path.join(pages_dir, "page_5.html"), "w", encoding="utf-8") as f: f.write(p5)

print("[✓] Pages 1-5 successfully rewritten with 100% filled visuals!")

import os

report_dir = r"C:\Users\Ritesh Kumar Agarwal\.gemini\antigravity\scratch\hybrid-anomaly-engine\report"
pages_dir = os.path.join(report_dir, "canva_pages")

def top_hdr(left="JIIT NOIDA • CSE DEPARTMENT", right="THEORY OF COMPUTATION (24B11CS212)"):
    return f"""<div class="canva-top-header"><span>{left}</span><span>{right}</span></div>"""

def btm_bar(left="PREPARED BY: DIVYANSH AGARWAL & TEAM", right="SESSION 2026–2027 • B.TECH CSE"):
    return f"""<div class="canva-bottom-bar"><span>{left}</span><span>{right}</span></div>"""

# ==============================================================================
# --- PAGE 11: MOORE MACHINE SESSION MONITOR (Dark Luxury Theme) ---
# ==============================================================================
p11 = f"""<section class="page theme-dark">
    {top_hdr("STATEFUL ANOMALY TRACKING", "TEMPORAL MOORE TRANSDUCER")}
    <div class="page-content">
        <div class="gold-eyebrow">TEMPORAL TRANSDUCTION</div>
        <h1 class="canva-title-large" style="font-size: 24pt; margin-bottom: 4mm;">
            STATEFUL SESSION TRACKING: 4-STATE MOORE MACHINE
        </h1>
        <div class="gold-separator-line"></div>

        <div style="display: grid; grid-template-columns: 1fr 1.35fr; gap: 20px; align-items: start; margin-top: 4mm;">
            <!-- Left Column: Formal Foundations -->
            <div style="display: flex; flex-direction: column; gap: 12px;">
                <div class="dark-card" style="border-left: 3px solid var(--wine-red);">
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 11pt; color: var(--gold-light); margin-bottom: 6px;">
                        Memoryless DFA vs Temporal State
                    </h3>
                    <p style="font-size: 8pt; color: var(--text-cream-dim); line-height: 1.6;">
                        While a standard DFA verifies the syntactic integrity of individual log records in isolation, modern cyber threats operate across temporal horizons. Distributed credential stuffing and brute-force attacks consist of individually valid grammatical lines that collectively constitute a severe breach.
                    </p>
                </div>

                <div class="dark-card" style="border-left: 3px solid var(--gold);">
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 11pt; color: var(--gold-light); margin-bottom: 6px;">
                        Formal 6-Tuple Transducer Definition
                    </h3>
                    <p style="font-size: 7.8pt; color: var(--text-cream-dim); line-height: 1.55;">
                        The stateful session monitor is formally structured as a deterministic finite-state transducer with output (Moore Machine):<br><br>
                        <strong>M<sub>Moore</sub> = (S, S₀, Σ, Λ, T, G)</strong><br>
                        • <strong>State Set S:</strong> {{ m₀, m₁, m₂, m₃ }}<br>
                        • <strong>Initial State S₀:</strong> m₀ (Normal / Baseline state)<br>
                        • <strong>Input Alphabet Σ:</strong> {{ AUTH_SUCCESS, AUTH_FAIL, OTHER }}<br>
                        • <strong>Output Alphabet Λ:</strong> {{ OK, FLAG_ATTACK }}<br>
                        • <strong>Transition Function T:</strong> S × Σ → S<br>
                        • <strong>Output Function G:</strong> S → Λ (Depends strictly on current state)
                    </p>
                </div>

                <div class="dark-card">
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 10.5pt; color: var(--gold-light); margin-bottom: 6px;">
                        Per-IP Session Hash Architecture
                    </h3>
                    <p style="font-size: 7.8pt; color: var(--text-cream-dim); line-height: 1.55;">
                        The C++14 engine instantiates an isolated Moore automaton per distinct IP address inside an O(1) hash table:
                        <code style="color:var(--gold); font-family:'JetBrains Mono'; display:block; margin:4px 0;">std::unordered_map&lt;std::string, MooreMachine&gt;</code>
                        Sessions reset upon successful authentication or when idle beyond decay parameter <em>T<sub>decay</sub> = 60s</em>.
                    </p>
                </div>
            </div>

            <!-- Right Column: Large State Diagram & Transition Table -->
            <div style="display: flex; flex-direction: column; gap: 12px;">
                <div class="arched-window-card" style="padding: 16px 12px; background: #231211;">
                    <div style="text-align: center; margin-bottom: 10px;">
                        <span style="font-family: 'Cinzel', serif; font-size: 8pt; letter-spacing: 2px; color: var(--gold); text-transform: uppercase;">
                            FIGURE 5: MOORE AUTOMATON STATE TRANSITION TOPOLOGY
                        </span>
                    </div>

                    <!-- Large Moore Machine SVG -->
                    <svg viewBox="0 0 440 220" style="width: 100%; height: 180px; display: block;">
                        <defs>
                            <marker id="arrow-gold" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                                <path d="M 0 1 L 10 5 L 0 9 z" fill="#C59F7A"></path>
                            </marker>
                            <marker id="arrow-red" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                                <path d="M 0 1 L 10 5 L 0 9 z" fill="#E53E3E"></path>
                            </marker>
                            <marker id="arrow-green" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                                <path d="M 0 1 L 10 5 L 0 9 z" fill="#38A169"></path>
                            </marker>
                        </defs>

                        <!-- State m0 -->
                        <circle cx="55" cy="90" r="32" fill="#1E0F0E" stroke="#C59F7A" stroke-width="2" />
                        <text x="55" y="84" text-anchor="middle" fill="#DFC4A8" font-family="Playfair Display" font-size="11" font-weight="bold">m0</text>
                        <text x="55" y="100" text-anchor="middle" fill="#38A169" font-family="Plus Jakarta Sans" font-size="8.5" font-weight="bold">/ OK</text>
                        <text x="55" y="136" text-anchor="middle" fill="#9E8C82" font-size="7">0 Fails</text>

                        <!-- Transition m0 -> m1 -->
                        <path d="M 87 90 L 138 90" fill="none" stroke="#C59F7A" stroke-width="1.8" marker-end="url(#arrow-gold)" />
                        <text x="113" y="80" text-anchor="middle" fill="#DFC4A8" font-size="7.5" font-weight="bold">AUTH_FAIL</text>

                        <!-- State m1 -->
                        <circle cx="170" cy="90" r="32" fill="#1E0F0E" stroke="#C59F7A" stroke-width="2" />
                        <text x="170" y="84" text-anchor="middle" fill="#DFC4A8" font-family="Playfair Display" font-size="11" font-weight="bold">m1</text>
                        <text x="170" y="100" text-anchor="middle" fill="#38A169" font-family="Plus Jakarta Sans" font-size="8.5" font-weight="bold">/ OK</text>
                        <text x="170" y="136" text-anchor="middle" fill="#9E8C82" font-size="7">1 Fail</text>

                        <!-- Transition m1 -> m2 -->
                        <path d="M 202 90 L 253 90" fill="none" stroke="#C59F7A" stroke-width="1.8" marker-end="url(#arrow-gold)" />
                        <text x="228" y="80" text-anchor="middle" fill="#DFC4A8" font-size="7.5" font-weight="bold">AUTH_FAIL</text>

                        <!-- State m2 -->
                        <circle cx="285" cy="90" r="32" fill="#1E0F0E" stroke="#C59F7A" stroke-width="2" />
                        <text x="285" y="84" text-anchor="middle" fill="#DFC4A8" font-family="Playfair Display" font-size="11" font-weight="bold">m2</text>
                        <text x="285" y="100" text-anchor="middle" fill="#38A169" font-family="Plus Jakarta Sans" font-size="8.5" font-weight="bold">/ OK</text>
                        <text x="285" y="136" text-anchor="middle" fill="#9E8C82" font-size="7">2 Fails</text>

                        <!-- Transition m2 -> m3 -->
                        <path d="M 317 90 L 368 90" fill="none" stroke="#E53E3E" stroke-width="2.2" marker-end="url(#arrow-red)" />
                        <text x="343" y="80" text-anchor="middle" fill="#E53E3E" font-size="7.5" font-weight="bold">AUTH_FAIL</text>

                        <!-- State m3 (Flag State - Double Ring) -->
                        <circle cx="395" cy="90" r="34" fill="#421212" stroke="#E53E3E" stroke-width="2.5" />
                        <circle cx="395" cy="90" r="28" fill="#2E1010" stroke="#E53E3E" stroke-width="1.2" />
                        <text x="395" y="84" text-anchor="middle" fill="#FFF" font-family="Playfair Display" font-size="11" font-weight="bold">m3</text>
                        <text x="395" y="100" text-anchor="middle" fill="#FF6B6B" font-family="Plus Jakarta Sans" font-size="7.5" font-weight="bold">/ FLAG</text>
                        <text x="395" y="138" text-anchor="middle" fill="#E53E3E" font-size="7" font-weight="bold">ATTACK (3+)</text>

                        <!-- Self-loop on m3 -->
                        <path d="M 405 57 C 425 25, 435 50, 422 75" fill="none" stroke="#E53E3E" stroke-width="1.5" marker-end="url(#arrow-red)" />
                        <text x="438" y="42" text-anchor="middle" fill="#FF6B6B" font-size="7">AUTH_FAIL</text>

                        <!-- Global Reset Arcs: m1, m2, m3 -> m0 on AUTH_SUCCESS -->
                        <path d="M 170 122 C 170 175, 55 175, 55 125" fill="none" stroke="#38A169" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#arrow-green)" />
                        <path d="M 285 122 C 285 195, 50 195, 50 126" fill="none" stroke="#38A169" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#arrow-green)" />
                        <path d="M 395 125 C 395 215, 45 215, 45 128" fill="none" stroke="#38A169" stroke-width="1.8" stroke-dasharray="4,3" marker-end="url(#arrow-green)" />
                        <text x="220" y="190" text-anchor="middle" fill="#38A169" font-size="8" font-weight="bold">AUTH_SUCCESS (Returns to m0 / Resets Counter)</text>
                    </svg>
                </div>

                <!-- Moore Output Mapping Table -->
                <div class="luxury-table-container">
                    <table class="luxury-table" style="font-size: 7.8pt;">
                        <thead>
                            <tr>
                                <th>State (S)</th>
                                <th>Semantic Meaning</th>
                                <th>Input AUTH_FAIL</th>
                                <th>Input AUTH_SUCCESS</th>
                                <th>Output G(S)</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>m₀</strong></td>
                                <td>Baseline clean session</td>
                                <td>m₁</td>
                                <td>m₀</td>
                                <td style="color:#2EA043; font-weight:bold;">OK</td>
                            </tr>
                            <tr>
                                <td><strong>m₁</strong></td>
                                <td>Single authentication fault</td>
                                <td>m₂</td>
                                <td>m₀</td>
                                <td style="color:#2EA043; font-weight:bold;">OK</td>
                            </tr>
                            <tr>
                                <td><strong>m₂</strong></td>
                                <td>Suspicious repeated failure</td>
                                <td>m₃</td>
                                <td>m₀</td>
                                <td style="color:#2EA043; font-weight:bold;">OK</td>
                            </tr>
                            <tr style="background: rgba(128, 24, 24, 0.3);">
                                <td><strong style="color:#FF6B6B;">m₃</strong></td>
                                <td>Brute-force breach threshold</td>
                                <td>m₃</td>
                                <td>m₀</td>
                                <td style="color:#E53E3E; font-weight:bold;">FLAG_ATTACK</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
    {btm_bar("STATEFUL TRANSDUCER SPECIFICATION", "SECTION 3.2 • MOORE SESSION MACHINE")}
</section>"""
with open(os.path.join(pages_dir, "page_11.html"), "w", encoding="utf-8") as f: f.write(p11)

# ==============================================================================
# --- PAGE 12: TURING MACHINE TAPE SANITIZER (Dark Luxury Theme) ---
# ==============================================================================
p12 = f"""<section class="page theme-dark">
    {top_hdr("CONFIDENTIALITY PRESERVATION", "FORMAL TAPE REDACTION")}
    <div class="page-content">
        <div class="gold-eyebrow">CHOMSKY TYPE-0 TRANSDUCTION</div>
        <h1 class="canva-title-large" style="font-size: 24pt; margin-bottom: 4mm;">
            PRIVACY SANITIZATION: 7-TUPLE TURING MACHINE
        </h1>
        <div class="gold-separator-line"></div>

        <div style="display: grid; grid-template-columns: 1.05fr 1fr; gap: 20px; align-items: start; margin-top: 4mm;">
            <!-- Left Column: The Privacy Threat & Formal 7-Tuple -->
            <div style="display: flex; flex-direction: column; gap: 12px;">
                <div class="dark-card" style="border-left: 3px solid var(--wine-red);">
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 11pt; color: var(--gold-light); margin-bottom: 6px;">
                        The Neural Privacy Leakage Risk
                    </h3>
                    <p style="font-size: 8pt; color: var(--text-cream-dim); line-height: 1.6;">
                        Escalating raw server logs directly to commercial cloud Large Language Models violates enterprise privacy mandates (GDPR Art. 32, HIPAA § 164.312). Malformed attack payloads frequently embed plaintext passwords, API bearer tokens, and internal subnet identifiers. A formal deterministic sanitizer is mathematically required prior to external transmission.
                    </p>
                </div>

                <div class="dark-card" style="border-left: 3px solid var(--gold);">
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 11pt; color: var(--gold-light); margin-bottom: 6px;">
                        Formal 7-Tuple Turing Sanitizer
                    </h3>
                    <p style="font-size: 7.8pt; color: var(--text-cream-dim); line-height: 1.55;">
                        The sanitizer is modeled as a deterministic single-tape read/write Turing Machine:<br><br>
                        <strong>M<sub>TM</sub> = (Q, Σ, Γ, δ, q₀, B, F)</strong><br>
                        • <strong>State Set Q:</strong> {{ q<sub>scan</sub>, q<sub>detect</sub>, q<sub>mask</sub>, q<sub>halt</sub> }}<br>
                        • <strong>Input Alphabet Σ:</strong> ASCII characters from log record<br>
                        • <strong>Tape Alphabet Γ:</strong> Σ ∪ {{ B, 'X' }} (Where B is blank, 'X' is mask symbol)<br>
                        • <strong>Initial State q₀:</strong> q<sub>scan</sub> (Rightward linear read)<br>
                        • <strong>Blank Symbol B:</strong> Tape boundary delimiter<br>
                        • <strong>Accept / Halt State F:</strong> {{ q<sub>halt</sub> }} (Halt on terminal blank B)
                    </p>
                </div>

                <div class="dark-card">
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 10.5pt; color: var(--gold-light); margin-bottom: 6px;">
                        Guaranteed Linear In-Place Masking O(N)
                    </h3>
                    <p style="font-size: 7.8pt; color: var(--text-cream-dim); line-height: 1.55;">
                        Unlike complex regex backreferences that risk ReDoS catastrophic backtracking, the Turing Machine executes exactly one rightward head traversal over the tape of length <em>N</em>. It deterministically overwrites detected secret payloads with character 'X', guaranteeing O(N) worst-case time complexity.
                    </p>
                </div>
            </div>

            <!-- Right Column: Tape Visualizer & Transition Logic -->
            <div style="display: flex; flex-direction: column; gap: 12px;">
                <div class="arched-window-card" style="padding: 16px 12px; background: #231211;">
                    <div style="text-align: center; margin-bottom: 10px;">
                        <span style="font-family: 'Cinzel', serif; font-size: 8pt; letter-spacing: 2px; color: var(--gold); text-transform: uppercase;">
                            FIGURE 6: TURING MACHINE TAPE HEAD OVERWRITE MECHANISM
                        </span>
                    </div>

                    <!-- SVG Tape Ribbon Visualization -->
                    <svg viewBox="0 0 420 220" style="width: 100%; height: 200px; display: block;">
                        <defs>
                            <filter id="glow-gold" x="-20%" y="-20%" width="140%" height="140%">
                                <feGaussianBlur stdDeviation="3" result="blur" />
                                <feComposite in="SourceGraphic" in2="blur" operator="over" />
                            </filter>
                        </defs>

                        <!-- Tape Boundary Lines -->
                        <line x1="10" y1="75" x2="410" y2="75" stroke="#8F7255" stroke-width="2" />
                        <line x1="10" y1="125" x2="410" y2="125" stroke="#8F7255" stroke-width="2" />

                        <!-- Tape Cells -->
                        <!-- Cell 1: p -->
                        <rect x="15" y="75" width="36" height="50" fill="#1E0F0E" stroke="#8F7255" stroke-width="1" />
                        <text x="33" y="106" text-anchor="middle" fill="#DFC4A8" font-family="JetBrains Mono" font-size="14">p</text>

                        <!-- Cell 2: a -->
                        <rect x="51" y="75" width="36" height="50" fill="#1E0F0E" stroke="#8F7255" stroke-width="1" />
                        <text x="69" y="106" text-anchor="middle" fill="#DFC4A8" font-family="JetBrains Mono" font-size="14">a</text>

                        <!-- Cell 3: s -->
                        <rect x="87" y="75" width="36" height="50" fill="#1E0F0E" stroke="#8F7255" stroke-width="1" />
                        <text x="105" y="106" text-anchor="middle" fill="#DFC4A8" font-family="JetBrains Mono" font-size="14">s</text>

                        <!-- Cell 4: s -->
                        <rect x="123" y="75" width="36" height="50" fill="#1E0F0E" stroke="#8F7255" stroke-width="1" />
                        <text x="141" y="106" text-anchor="middle" fill="#DFC4A8" font-family="JetBrains Mono" font-size="14">s</text>

                        <!-- Cell 5: = -->
                        <rect x="159" y="75" width="36" height="50" fill="#1E0F0E" stroke="#8F7255" stroke-width="1" />
                        <text x="177" y="106" text-anchor="middle" fill="#DFC4A8" font-family="JetBrains Mono" font-size="14">=</text>

                        <!-- Cell 6: X (Redacted) -->
                        <rect x="195" y="75" width="36" height="50" fill="#421212" stroke="#E53E3E" stroke-width="1.5" />
                        <text x="213" y="106" text-anchor="middle" fill="#FF6B6B" font-family="JetBrains Mono" font-size="14" font-weight="bold">X</text>

                        <!-- Cell 7: X (Active Head Cell) -->
                        <rect x="231" y="75" width="36" height="50" fill="#421212" stroke="#C59F7A" stroke-width="2" />
                        <text x="249" y="106" text-anchor="middle" fill="#FF6B6B" font-family="JetBrains Mono" font-size="14" font-weight="bold">X</text>

                        <!-- Cell 8: X (Redacted) -->
                        <rect x="267" y="75" width="36" height="50" fill="#421212" stroke="#E53E3E" stroke-width="1.5" />
                        <text x="285" y="106" text-anchor="middle" fill="#FF6B6B" font-family="JetBrains Mono" font-size="14" font-weight="bold">X</text>

                        <!-- Cell 9: X (Redacted) -->
                        <rect x="303" y="75" width="36" height="50" fill="#421212" stroke="#E53E3E" stroke-width="1.5" />
                        <text x="321" y="106" text-anchor="middle" fill="#FF6B6B" font-family="JetBrains Mono" font-size="14" font-weight="bold">X</text>

                        <!-- Cell 10: Blank B -->
                        <rect x="339" y="75" width="36" height="50" fill="#1E0F0E" stroke="#8F7255" stroke-width="1" />
                        <text x="357" y="106" text-anchor="middle" fill="#8F7255" font-family="JetBrains Mono" font-size="14">B</text>

                        <!-- Cell 11: Blank B -->
                        <rect x="375" y="75" width="36" height="50" fill="#1E0F0E" stroke="#8F7255" stroke-width="1" />
                        <text x="393" y="106" text-anchor="middle" fill="#8F7255" font-family="JetBrains Mono" font-size="14">B</text>

                        <!-- Turing Tape Head Pointer -->
                        <polygon points="249,145 240,165 258,165" fill="#C59F7A" filter="url(#glow-gold)" />
                        <rect x="204" y="165" width="90" height="36" rx="6" fill="#2E1917" stroke="#C59F7A" stroke-width="1.5" />
                        <text x="249" y="182" text-anchor="middle" fill="#DFC4A8" font-family="Cinzel" font-size="8" font-weight="bold">HEAD: q_mask</text>
                        <text x="249" y="195" text-anchor="middle" fill="#C59F7A" font-family="JetBrains Mono" font-size="7.5">Write 'X', Move R</text>

                        <!-- Status Label -->
                        <text x="213" y="45" text-anchor="middle" fill="#C59F7A" font-size="8" font-weight="bold">SECRET PAYLOAD DETECTED</text>
                        <path d="M 195 52 L 339 52" fill="none" stroke="#E53E3E" stroke-width="2" />
                        <text x="267" y="64" text-anchor="middle" fill="#FF6B6B" font-size="7">Original: "S3cr3t!" → Masked: "XXXXXX"</text>
                    </svg>
                </div>

                <!-- State Transition Logic Matrix -->
                <div class="luxury-table-container">
                    <table class="luxury-table" style="font-size: 7.8pt;">
                        <thead>
                            <tr>
                                <th>Current State</th>
                                <th>Scanned Symbol</th>
                                <th>Next State</th>
                                <th>Write Action</th>
                                <th>Head Move</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>q<sub>scan</sub></strong></td>
                                <td>[a-zA-Z0-9]</td>
                                <td>q<sub>scan</sub></td>
                                <td>Unchanged</td>
                                <td>Move Right (R)</td>
                            </tr>
                            <tr>
                                <td><strong>q<sub>scan</sub></strong></td>
                                <td>Keyword match ('pass=')</td>
                                <td>q<sub>detect</sub></td>
                                <td>Unchanged</td>
                                <td>Move Right (R)</td>
                            </tr>
                            <tr style="background: rgba(128, 24, 24, 0.3);">
                                <td><strong style="color:#FF6B6B;">q<sub>detect</sub></strong></td>
                                <td>Sensitive character</td>
                                <td>q<sub>mask</sub></td>
                                <td>Overwrite with 'X'</td>
                                <td>Move Right (R)</td>
                            </tr>
                            <tr>
                                <td><strong>q<sub>mask</sub></strong></td>
                                <td>Delimiter (' ', '&quot;', B)</td>
                                <td>q<sub>scan</sub> / q<sub>halt</sub></td>
                                <td>Unchanged</td>
                                <td>Halt / Scan</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
    {btm_bar("FORMAL TURING SANITIZER", "SECTION 3.3 • 7-TUPLE MASKING ENGINE")}
</section>"""
with open(os.path.join(pages_dir, "page_12.html"), "w", encoding="utf-8") as f: f.write(p12)

# ==============================================================================
# --- PAGE 13: NEURAL ESCALATION PIPELINE (Cream Luxury Theme) ---
# ==============================================================================
p13 = f"""<section class="page theme-cream">
    {top_hdr("NEURAL ESCALATION ARCHITECTURE", "BOUNDED QUEUE & API CONTROL")}
    <div class="page-content">
        <div class="gold-eyebrow" style="color: var(--wine-red);">ASYMMETRIC COUPLING</div>
        <h1 class="canva-title-large" style="color: var(--wine-red); font-size: 24pt; margin-bottom: 4mm;">
            NEURAL TRIAGE &amp; BOUNDED RATE CONTROL
        </h1>
        <div class="gold-separator-line" style="background: linear-gradient(90deg, var(--wine-red), transparent);"></div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; align-items: start; margin-top: 4mm;">
            <!-- Left Column: The Neural Chokepoint & Queue Sizing -->
            <div style="display: flex; flex-direction: column; gap: 12px;">
                <div class="cream-card" style="border-left: 3px solid var(--wine-red);">
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 11pt; color: var(--wine-red); margin-bottom: 6px;">
                        The Ingestion Rate Disparity Problem
                    </h3>
                    <p style="font-size: 8pt; color: var(--text-dark-secondary); line-height: 1.6;">
                        Enterprise servers generate logs at burst rates exceeding <strong>100,000 events/second</strong>. Commercial LLM APIs (e.g., Google Gemini 1.5, OpenAI GPT-4o) enforce strict Tier-1 rate limits typically capped at <strong>60 Requests Per Minute (RPM)</strong> and 40,000 Tokens Per Minute (TPM). Directly subjecting cloud LLMs to raw ingestion floods causes immediate HTTP 429 quota exhaustion and service paralysis.
                    </p>
                </div>

                <div class="cream-card">
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 11pt; color: var(--wine-red); margin-bottom: 6px;">
                        Bounded Ring Buffer Queue Architecture
                    </h3>
                    <p style="font-size: 8pt; color: var(--text-dark-secondary); line-height: 1.6;">
                        To decouple the high-throughput symbolic automata from the high-latency neural LLM, the engine deploys a bounded concurrent ring buffer of capacity <strong>K = 1,000</strong>. Only suspicious lines flagged by either the DFA (trap state <em>q<sub>E</sub></em>) or the Moore Machine (flag state <em>m₃</em>) are sanitized and queued.
                    </p>
                </div>

                <div class="cream-card">
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 10.5pt; color: var(--wine-red); margin-bottom: 6px;">
                        Token-Bucket Smooth Rate Throttling
                    </h3>
                    <p style="font-size: 7.8pt; color: var(--text-dark-secondary); line-height: 1.55;">
                        A dedicated background worker thread pool monitors token replenishment using a token-bucket governor. Escalations are dispatched asynchronously via <strong>libcurl</strong> multi-socket interfaces, preventing any worker thread blocking while preserving strict API compliance.
                    </p>
                </div>
            </div>

            <!-- Right Column: JSON Schema Card & Flow Diagram -->
            <div style="display: flex; flex-direction: column; gap: 12px;">
                <div class="cream-card" style="background: #FFFFFF; border: 1.5px solid rgba(128, 24, 24, 0.2); box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 11pt; color: var(--wine-red); margin-bottom: 8px;">
                        Strict Structured Escalation Schema (JSON)
                    </h3>
                    <p style="font-size: 7.8pt; color: var(--text-dark-secondary); margin-bottom: 8px;">
                        The Turing sanitizer outputs a deterministic JSON payload strictly conforming to the evaluation schema:
                    </p>
                    <pre style="background: #1E0F0E; color: #DFC4A8; font-family: 'JetBrains Mono', monospace; font-size: 7.5pt; padding: 12px; border-radius: 6px; line-height: 1.5; overflow: hidden;">
{{
  "event_id": "EVT-2026-9042",
  "triage_trigger": "DFA_SYNTAX_REJECT (State qE)",
  "timestamp": "2026-11-24T14:10:05Z",
  "source_ip": "192.168.1.52",
  "sanitized_payload": "root' OR '1'='1 --",
  "moore_state": "m0 (Clean session)",
  "anomaly_context": "Unquoted SQL quote token detected",
  "requested_action": "CLASSIFY_SEVERITY_AND_INTENT"
}}</pre>
                </div>

                <div class="cream-card">
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 11pt; color: var(--wine-red); margin-bottom: 6px;">
                        Asymmetric Throughput Decoupling
                    </h3>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 8px;">
                        <div style="text-align: center; flex: 1;">
                            <span style="font-family: 'Cinzel'; font-size: 16pt; font-weight: bold; color: var(--wine-red);">555,000</span>
                            <div style="font-size: 7pt; color: var(--text-dark-secondary); text-transform: uppercase;">Logs / Sec (Automata)</div>
                        </div>
                        <div style="font-size: 16pt; color: var(--gold-dim);">➔</div>
                        <div style="text-align: center; flex: 1;">
                            <span style="font-family: 'Cinzel'; font-size: 16pt; font-weight: bold; color: #B7791F;">1,000</span>
                            <div style="font-size: 7pt; color: var(--text-dark-secondary); text-transform: uppercase;">Queue Buffer (K)</div>
                        </div>
                        <div style="font-size: 16pt; color: var(--gold-dim);">➔</div>
                        <div style="text-align: center; flex: 1;">
                            <span style="font-family: 'Cinzel'; font-size: 16pt; font-weight: bold; color: #2EA043;">1.0</span>
                            <div style="font-size: 7pt; color: var(--text-dark-secondary); text-transform: uppercase;">Req / Sec (LLM API)</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    {btm_bar("NEURAL INTEGRATION SPECIFICATION", "SECTION 3.4 • RATE REGULATION & ESCALATION")}
</section>"""
with open(os.path.join(pages_dir, "page_13.html"), "w", encoding="utf-8") as f: f.write(p13)

# ==============================================================================
# --- PAGE 14: EMPIRICAL TRACES: CASES A & B (Dark Luxury Theme) ---
# ==============================================================================
p14 = f"""<section class="page theme-dark">
    {top_hdr("EMPIRICAL SYSTEM VALIDATION", "CASE STUDIES: ROUTINE & INJECTION")}
    <div class="page-content">
        <div class="gold-eyebrow">EXPERIMENTAL EVALUATION</div>
        <h1 class="canva-title-large" style="font-size: 24pt; margin-bottom: 4mm;">
            EMPIRICAL EXECUTION TRACES: CASES A &amp; B
        </h1>
        <div class="gold-separator-line"></div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; align-items: start; margin-top: 4mm;">
            <!-- Left Card: Case A (Routine Login) -->
            <div class="arched-window-card" style="padding: 16px; background: #231211;">
                <div style="border-bottom: 1.5px solid var(--border-gold); padding-bottom: 8px; margin-bottom: 10px;">
                    <span style="font-family: 'Cinzel', serif; font-size: 8pt; letter-spacing: 2px; color: #38A169; text-transform: uppercase; font-weight: bold;">
                        CASE A • ROUTINE LEGITIMATE AUTHENTICATION
                    </span>
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 13pt; color: var(--gold-light); margin-top: 4px;">
                        Fast-Path Symbolic Resolution
                    </h3>
                </div>

                <div style="margin-bottom: 10px;">
                    <span style="font-size: 7.5pt; color: var(--text-muted); text-transform: uppercase;">RAW INPUT LOG:</span>
                    <pre style="background: #170A09; color: #DFC4A8; font-family: 'JetBrains Mono'; font-size: 7.2pt; padding: 8px; border-radius: 4px; margin-top: 3px; word-break: break-all;">Accepted password for root from 192.168.1.100 port 22 ssh2</pre>
                </div>

                <div style="margin-bottom: 10px;">
                    <span style="font-size: 7.5pt; color: var(--text-muted); text-transform: uppercase;">LEXER TOKEN STREAM:</span>
                    <div style="display: flex; gap: 4px; flex-wrap: wrap; margin-top: 3px;">
                        <span class="token-badge token-level">LEVEL</span>
                        <span class="token-badge token-user">USER</span>
                        <span class="token-badge token-ip">IP</span>
                        <span class="token-badge token-status">STATUS</span>
                    </div>
                </div>

                <div style="margin-bottom: 10px;">
                    <span style="font-size: 7.5pt; color: var(--text-muted); text-transform: uppercase;">AUTOMATA TRAVERSAL PATH:</span>
                    <p style="font-family: 'JetBrains Mono'; font-size: 7.5pt; color: var(--gold); margin-top: 2px;">
                        q₀ ➔ q₁ (LEVEL) ➔ q₂ (IP) ➔ q₃ (USER) ➔ q₄ (STATUS) [ACCEPT]
                    </p>
                </div>

                <div class="dark-card" style="background: rgba(46, 160, 67, 0.15); border: 1px solid #2EA043;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <strong style="color: #2EA043; font-size: 8.5pt;">DECISION: FAST-PATH LOCAL COMMIT</strong>
                            <div style="font-size: 7.5pt; color: var(--text-cream-dim);">Moore state remains m₀. Zero LLM API invocation.</div>
                        </div>
                        <span style="font-family: 'Cinzel'; font-size: 14pt; color: #2EA043; font-weight: bold;">0.0018 ms</span>
                    </div>
                </div>
            </div>

            <!-- Right Card: Case B (SQL Injection) -->
            <div class="arched-window-card" style="padding: 16px; background: #231211;">
                <div style="border-bottom: 1.5px solid var(--border-gold); padding-bottom: 8px; margin-bottom: 10px;">
                    <span style="font-family: 'Cinzel', serif; font-size: 8pt; letter-spacing: 2px; color: #E53E3E; text-transform: uppercase; font-weight: bold;">
                        CASE B • MALFORMED SQL INJECTION PAYLOAD
                    </span>
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 13pt; color: var(--gold-light); margin-top: 4px;">
                        Trap State Interception &amp; Escalation
                    </h3>
                </div>

                <div style="margin-bottom: 10px;">
                    <span style="font-size: 7.5pt; color: var(--text-muted); text-transform: uppercase;">RAW INPUT LOG:</span>
                    <pre style="background: #170A09; color: #FF6B6B; font-family: 'JetBrains Mono'; font-size: 7.2pt; padding: 8px; border-radius: 4px; margin-top: 3px; word-break: break-all;">Failed password for root' OR '1'='1-- from 10.0.0.99 port 22</pre>
                </div>

                <div style="margin-bottom: 10px;">
                    <span style="font-size: 7.5pt; color: var(--text-muted); text-transform: uppercase;">LEXER TOKEN STREAM:</span>
                    <div style="display: flex; gap: 4px; flex-wrap: wrap; margin-top: 3px;">
                        <span class="token-badge token-level">LEVEL</span>
                        <span class="token-badge token-user">USER</span>
                        <span class="token-badge token-other">OTHER (SQL QUOTE)</span>
                    </div>
                </div>

                <div style="margin-bottom: 10px;">
                    <span style="font-size: 7.5pt; color: var(--text-muted); text-transform: uppercase;">AUTOMATA TRAVERSAL PATH:</span>
                    <p style="font-family: 'JetBrains Mono'; font-size: 7.5pt; color: #E53E3E; margin-top: 2px;">
                        q₀ ➔ q₁ (LEVEL) ➔ q₂ (USER) ➔ q<sub>E</sub> (OTHER) [REJECT / TRAP]
                    </p>
                </div>

                <div class="dark-card" style="background: rgba(128, 24, 24, 0.25); border: 1px solid #E53E3E;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <strong style="color: #FF6B6B; font-size: 8.5pt;">DECISION: ESCALATE TO NEURAL LLM</strong>
                            <div style="font-size: 7.5pt; color: var(--text-cream-dim);">Turing tape masks secrets; payload queued for analyst audit.</div>
                        </div>
                        <span style="font-family: 'Cinzel'; font-size: 14pt; color: #FF6B6B; font-weight: bold;">CRITICAL</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    {btm_bar("EXPERIMENTAL CASE STUDIES", "SECTION 4.1 • CASES A & B VALIDATION")}
</section>"""
with open(os.path.join(pages_dir, "page_14.html"), "w", encoding="utf-8") as f: f.write(p14)

# ==============================================================================
# --- PAGE 15: EMPIRICAL TRACES: CASES C & D (Dark Luxury Theme) ---
# ==============================================================================
p15 = f"""<section class="page theme-dark">
    {top_hdr("EMPIRICAL SYSTEM VALIDATION", "CASE STUDIES: BRUTE FORCE & SECRETS")}
    <div class="page-content">
        <div class="gold-eyebrow">EXPERIMENTAL EVALUATION</div>
        <h1 class="canva-title-large" style="font-size: 24pt; margin-bottom: 4mm;">
            EMPIRICAL EXECUTION TRACES: CASES C &amp; D
        </h1>
        <div class="gold-separator-line"></div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; align-items: start; margin-top: 4mm;">
            <!-- Left Card: Case C (Brute-Force Spray) -->
            <div class="arched-window-card" style="padding: 16px; background: #231211;">
                <div style="border-bottom: 1.5px solid var(--border-gold); padding-bottom: 8px; margin-bottom: 10px;">
                    <span style="font-family: 'Cinzel', serif; font-size: 8pt; letter-spacing: 2px; color: #E53E3E; text-transform: uppercase; font-weight: bold;">
                        CASE C • DISTRIBUTED BRUTE-FORCE BURST
                    </span>
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 13pt; color: var(--gold-light); margin-top: 4px;">
                        Moore Transducer State Flagging
                    </h3>
                </div>

                <div style="margin-bottom: 10px;">
                    <span style="font-size: 7.5pt; color: var(--text-muted); text-transform: uppercase;">SEQUENTIAL LOG STREAM (192.168.1.52):</span>
                    <pre style="background: #170A09; color: #DFC4A8; font-family: 'JetBrains Mono'; font-size: 7pt; padding: 6px; border-radius: 4px; margin-top: 3px;">
L1: Failed password for admin from 192.168.1.52 port 22
L2: Failed password for guest from 192.168.1.52 port 22
L3: Failed password for oracle from 192.168.1.52 port 22</pre>
                </div>

                <div style="margin-bottom: 10px;">
                    <span style="font-size: 7.5pt; color: var(--text-muted); text-transform: uppercase;">DFA SYNTAX VS MOORE TRANSDUCTION:</span>
                    <p style="font-size: 7.5pt; color: var(--text-cream-dim); line-height: 1.5; margin-top: 3px;">
                        • DFA evaluates each line as grammatically valid (q₀ ➔ q₄ ACCEPT).<br>
                        • Moore session tracking for IP <code>192.168.1.52</code>:<br>
                        &nbsp;&nbsp;&nbsp;&nbsp;Line 1: m₀ ➔ m₁ (Output: OK)<br>
                        &nbsp;&nbsp;&nbsp;&nbsp;Line 2: m₁ ➔ m₂ (Output: OK)<br>
                        &nbsp;&nbsp;&nbsp;&nbsp;Line 3: m₂ ➔ m₃ (Output: <strong style="color:#FF6B6B;">FLAG_ATTACK</strong>)
                    </p>
                </div>

                <div class="dark-card" style="background: rgba(128, 24, 24, 0.25); border: 1px solid #E53E3E;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <strong style="color: #FF6B6B; font-size: 8.5pt;">DECISION: ESCALATE BRUTE-FORCE INCIDENT</strong>
                            <div style="font-size: 7.5pt; color: var(--text-cream-dim);">IP quarantined locally; incident dossier sent to LLM for intent analysis.</div>
                        </div>
                        <span style="font-family: 'Cinzel'; font-size: 14pt; color: #FF6B6B; font-weight: bold;">MOORE m₃</span>
                    </div>
                </div>
            </div>

            <!-- Right Card: Case D (Credential Leak Sanitizer) -->
            <div class="arched-window-card" style="padding: 16px; background: #231211;">
                <div style="border-bottom: 1.5px solid var(--border-gold); padding-bottom: 8px; margin-bottom: 10px;">
                    <span style="font-family: 'Cinzel', serif; font-size: 8pt; letter-spacing: 2px; color: #38A169; text-transform: uppercase; font-weight: bold;">
                        CASE D • SENSITIVE CREDENTIAL LEAK SCRUBBING
                    </span>
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 13pt; color: var(--gold-light); margin-top: 4px;">
                        Turing Machine Tape Redaction
                    </h3>
                </div>

                <div style="margin-bottom: 10px;">
                    <span style="font-size: 7.5pt; color: var(--text-muted); text-transform: uppercase;">RAW TAPE PAYLOAD (PRE-SANITIZATION):</span>
                    <pre style="background: #170A09; color: #FF6B6B; font-family: 'JetBrains Mono'; font-size: 7pt; padding: 6px; border-radius: 4px; margin-top: 3px; word-break: break-all;">User admin auth fail pass=SecretPass999! token=xyz_live_9921</pre>
                </div>

                <div style="margin-bottom: 10px;">
                    <span style="font-size: 7.5pt; color: var(--text-muted); text-transform: uppercase;">SANITIZED TAPE OUTPUT (POST-SANITIZATION):</span>
                    <pre style="background: #170A09; color: #2EA043; font-family: 'JetBrains Mono'; font-size: 7pt; padding: 6px; border-radius: 4px; margin-top: 3px; word-break: break-all;">User admin auth fail pass=XXXXXXXXXXXXX token=XXXXXXXXXXXXX</pre>
                </div>

                <div style="margin-bottom: 10px;">
                    <span style="font-size: 7.5pt; color: var(--text-muted); text-transform: uppercase;">SECURITY AUDIT ASSURANCE:</span>
                    <p style="font-size: 7.5pt; color: var(--text-cream-dim); line-height: 1.5; margin-top: 3px;">
                        The Turing Machine read/write head overwrites every byte of sensitive credentials with character 'X'. Zero confidential keys leave enterprise perimeter.
                    </p>
                </div>

                <div class="dark-card" style="background: rgba(46, 160, 67, 0.15); border: 1px solid #2EA043;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <strong style="color: #2EA043; font-size: 8.5pt;">PRIVACY INTEGRITY PRESERVED</strong>
                            <div style="font-size: 7.5pt; color: var(--text-cream-dim);">GDPR &amp; HIPAA compliant redaction verified via unit tests.</div>
                        </div>
                        <span style="font-family: 'Cinzel'; font-size: 14pt; color: #2EA043; font-weight: bold;">ZERO LEAK</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    {btm_bar("EXPERIMENTAL CASE STUDIES", "SECTION 4.2 • CASES C & D VALIDATION")}
</section>"""
with open(os.path.join(pages_dir, "page_15.html"), "w", encoding="utf-8") as f: f.write(p15)

print("[✓] Generated Pages 11, 12, 13, 14, 15.")

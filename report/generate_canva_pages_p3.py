import os

report_dir = r"C:\Users\Ritesh Kumar Agarwal\.gemini\antigravity\scratch\hybrid-anomaly-engine\report"
pages_dir = os.path.join(report_dir, "canva_pages")

def top_hdr(left="JIIT NOIDA • CSE DEPARTMENT", right="THEORY OF COMPUTATION (24B11CS212)"):
    return f"""<div class="canva-top-header"><span>{left}</span><span>{right}</span></div>"""

def btm_bar(left="PREPARED BY: DIVYANSH AGARWAL & TEAM", right="SESSION 2026–2027 • B.TECH CSE"):
    return f"""<div class="canva-bottom-bar"><span>{left}</span><span>{right}</span></div>"""

# --- PAGE 6: CHOMSKY HIERARCHY (Cream Luxury Theme) ---
p6 = f"""<section class="page theme-cream">
    {top_hdr("FORMAL LANGUAGE THEORY", "CHOMSKY HIERARCHY MAPPING")}
    <div class="page-content" style="padding-top: 10mm;">
        <div>
            <div style="background: var(--wine-red); color: #FFF; padding: 10px 18px; border-radius: 4px; margin-bottom: 14px;">
                <h1 style="font-family: 'Playfair Display', serif; font-size: 24pt; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 3px;">
                    THE CHOMSKY HIERARCHY
                </h1>
                <p style="font-size: 8.5pt; color: #EAE0D5; letter-spacing: 1px; text-transform: uppercase;">
                    Mathematical Categorization of Telemetry and Cyber Injection Payloads
                </p>
            </div>

            <!-- Large Concentric Chomsky Diagram -->
            <div class="cream-card" style="margin-bottom: 14px; padding: 14px; text-align: center;">
                <svg width="600" height="150" viewBox="0 0 600 150" fill="none">
                    <!-- Type 0: Unrestricted -->
                    <rect x="20" y="10" width="560" height="130" rx="8" fill="#F0E8DD" stroke="#801818" stroke-width="1.5"/>
                    <text x="35" y="28" fill="#801818" font-family="'Playfair Display', serif" font-size="9" font-weight="bold">TYPE 0: RECURSIVELY ENUMERABLE (Turing Machines) • Arbitrary Unrestricted Computation</text>

                    <!-- Type 1/2: Context-Free -->
                    <rect x="40" y="38" width="520" height="92" rx="6" fill="#FDFBF7" stroke="#C59F7A" stroke-width="1.5"/>
                    <text x="55" y="55" fill="#C59F7A" font-family="'Playfair Display', serif" font-size="8.5" font-weight="bold">TYPE 1 / 2: CONTEXT-FREE (Pushdown Automata) • Nested Syntax, Balanced Structures</text>

                    <!-- Type 3: Regular Language -->
                    <rect x="60" y="66" width="480" height="54" rx="5" fill="#801818"/>
                    <text x="80" y="84" fill="#FFF" font-family="'Playfair Display', serif" font-size="9" font-weight="bold">TYPE 3: REGULAR LANGUAGES (Deterministic Finite Automata) • Linear Scan 𝒪(N)</text>
                    <text x="80" y="102" fill="#EAE0D5" font-family="'JetBrains Mono', monospace" font-size="7.5">Standard Telemetry: [INFO] IP USER STATUS ──► Strictly Recognized by Minimal DFA</text>
                </svg>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
                <div class="cream-card" style="border-top: 3px solid var(--wine-red);">
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 11pt; color: var(--wine-red); margin-bottom: 6px;">
                        Grammar Production Formulation
                    </h3>
                    <p style="font-size: 8pt; color: var(--text-dark-secondary); line-height: 1.55;">
                        Let <strong>Σ</strong> denote the formal token alphabet:
                        <br><code style="font-family: 'JetBrains Mono', monospace; font-size: 7.5pt; color: var(--wine-red);">Σ = {{ LEVEL, IP, USER, STATUS, OTHER }}</code><br>
                        A valid login event string <em>w</em> ∈ Σ* belongs to regular language <em>L</em><sub>baseline</sub> if it strictly satisfies:
                        <br><code style="font-family: 'JetBrains Mono', monospace; font-size: 7.5pt; color: var(--wine-red);">S → LEVEL · IP · USER · STATUS</code><br>
                        Because <em>L</em><sub>baseline</sub> is regular, its equivalence classes under the Myhill-Nerode relation are strictly finite (index = 6).
                    </p>
                </div>

                <div class="cream-card" style="border-top: 3px solid var(--wine-red);">
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 11pt; color: var(--wine-red); margin-bottom: 6px;">
                        The Computational Frontier
                    </h3>
                    <p style="font-size: 8pt; color: var(--text-dark-secondary); line-height: 1.55;">
                        While standard events reside in Type 3, complex web attacks (such as recursive SQL injections with balanced parentheses <code>((1))</code> or nested JSON objects) belong to Type 2 or Type 0.
                        <br><br>
                        By implementing a DFA tuned precisely to Type 3 syntax, any structural deviation triggers a fatal transition into the <strong>Trap State (q<sub>E</sub>)</strong>, cleanly segregating complex anomalies.
                    </p>
                </div>
            </div>
        </div>
    </div>
    {btm_bar("FORMAL GRAMMAR SPECIFICATIONS", "TYPE 3 VS TYPE 0 BOUNDARIES")}
</section>"""
with open(os.path.join(pages_dir, "page_6.html"), "w", encoding="utf-8") as f: f.write(p6)

# --- PAGE 7: DUAL-LANE ARCHITECTURE BLUEPRINT (Dark Luxury Theme) ---
p7 = f"""<section class="page theme-dark">
    {top_hdr("ENGINE ARCHITECTURE", "DUAL-LANE NEURO-SYMBOLIC BLUEPRINT")}
    <div class="page-content" style="padding-top: 10mm;">
        <div>
            <h1 class="canva-title" style="font-size: 28pt; margin-bottom: 6px;">
                SYSTEM ARCHITECTURE
            </h1>
            <h2 class="canva-subtitle">End-to-End Symbolic Fast Path & Neural Slow Path Pipeline</h2>

            <!-- Large Architecture Diagram -->
            <div class="dark-card" style="margin-bottom: 14px; padding: 14px; background: #241211;">
                <svg width="600" height="155" viewBox="0 0 600 155" fill="none">
                    <!-- Raw Ingestion -->
                    <rect x="10" y="55" width="75" height="42" rx="4" fill="#38231E" stroke="#C59F7A" stroke-width="1.2"/>
                    <text x="47" y="72" fill="#FFF" font-family="'Playfair Display', serif" font-size="8" font-weight="bold" text-anchor="middle">RAW LOG</text>
                    <text x="47" y="85" fill="#DFC4A8" font-size="6.5" text-anchor="middle">Stream Inflow</text>

                    <path d="M85 76H115" stroke="#C59F7A" stroke-width="1.5"/>
                    <polygon points="115,76 109,73 109,79" fill="#C59F7A"/>

                    <!-- C++ Lexer -->
                    <rect x="115" y="50" width="85" height="52" rx="4" fill="#2E1716" stroke="#801818" stroke-width="1.5"/>
                    <text x="157" y="70" fill="#FFF" font-family="'Playfair Display', serif" font-size="8.5" font-weight="bold" text-anchor="middle">C++ LEXER</text>
                    <text x="157" y="82" fill="#EAE0D5" font-size="6.5" text-anchor="middle">Token Regex Map</text>
                    <text x="157" y="93" fill="#C59F7A" font-family="'JetBrains Mono', monospace" font-size="6" text-anchor="middle">LEVEL, IP, USER</text>

                    <path d="M200 76H230" stroke="#C59F7A" stroke-width="1.5"/>
                    <polygon points="230,76 224,73 224,79" fill="#C59F7A"/>

                    <!-- Minimal DFA Engine -->
                    <rect x="230" y="45" width="90" height="62" rx="5" fill="#801818" stroke="#C59F7A" stroke-width="1.8"/>
                    <text x="275" y="66" fill="#FFF" font-family="'Playfair Display', serif" font-size="9" font-weight="bold" text-anchor="middle">DFA RECOGNIZER</text>
                    <text x="275" y="78" fill="#EAE0D5" font-size="7" text-anchor="middle">Table 3 Matrix</text>
                    <text x="275" y="90" fill="#DFC4A8" font-size="6.5" text-anchor="middle">𝒪(N) Linear Time</text>
                    <text x="275" y="100" fill="#FFF" font-size="6" font-weight="bold" text-anchor="middle">Zero Backtracking</text>

                    <!-- Split Routes -->
                    <path d="M320 62H350V40H375" stroke="#238636" stroke-width="1.5"/>
                    <polygon points="375,40 369,37 369,43" fill="#238636"/>
                    <text x="345" y="54" fill="#2EA043" font-size="6.5" font-weight="bold">ACCEPT</text>

                    <!-- Moore FSM -->
                    <rect x="375" y="22" width="85" height="36" rx="4" fill="#2E1716" stroke="#238636" stroke-width="1.5"/>
                    <text x="417" y="37" fill="#2EA043" font-family="'Playfair Display', serif" font-size="7.5" font-weight="bold" text-anchor="middle">MOORE FSM</text>
                    <text x="417" y="49" fill="#D1C4BC" font-size="6" text-anchor="middle">m₀..m₃ Counter</text>

                    <!-- Local Store -->
                    <path d="M460 40H495" stroke="#238636" stroke-width="1.5"/>
                    <polygon points="495,40 489,37 489,43" fill="#238636"/>
                    <rect x="495" y="24" width="95" height="32" rx="4" fill="#238636"/>
                    <text x="542" y="38" fill="#FFF" font-size="7.5" font-weight="bold" text-anchor="middle">LOCAL LOG STORE</text>
                    <text x="542" y="48" fill="#FFF" font-size="6" text-anchor="middle">Latency: 160 µs • Cost: $0</text>

                    <!-- Reject / Flag Route to TM -->
                    <path d="M320 90H350V120H375" stroke="#DA3633" stroke-width="1.5"/>
                    <path d="M417 58V120H425" stroke="#C59F7A" stroke-width="1.5"/>
                    <polygon points="375,120 369,117 369,123" fill="#DA3633"/>
                    <text x="345" y="108" fill="#DA3633" font-size="6.5" font-weight="bold">REJECT (qE)</text>

                    <!-- TM Sanitizer -->
                    <rect x="375" y="104" width="85" height="36" rx="4" fill="#2E1716" stroke="#DA3633" stroke-width="1.5"/>
                    <text x="417" y="119" fill="#DA3633" font-family="'Playfair Display', serif" font-size="7.5" font-weight="bold" text-anchor="middle">TM SANITIZER</text>
                    <text x="417" y="131" fill="#DFC4A8" font-size="6" text-anchor="middle">Tape Redaction</text>

                    <!-- LLM REST API -->
                    <path d="M460 122H495" stroke="#C59F7A" stroke-width="1.5"/>
                    <polygon points="495,122 489,119 489,125" fill="#C59F7A"/>
                    <rect x="495" y="106" width="95" height="32" rx="4" fill="#801818" stroke="#C59F7A" stroke-width="1.2"/>
                    <text x="542" y="120" fill="#FFF" font-size="7.5" font-weight="bold" text-anchor="middle">NEURAL SLOW PATH</text>
                    <text x="542" y="130" fill="#DFC4A8" font-size="6" text-anchor="middle">Forensic JSON Schema</text>
                </svg>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
                <div class="dark-card" style="border-left: 3px solid #238636;">
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 11pt; color: #2EA043; margin-bottom: 4px;">Symbolic Fast Path Guarantees</h3>
                    <p style="font-size: 7.8pt; color: var(--text-cream-dim); line-height: 1.5;">
                        • Deterministic execution bound of 160 microseconds per log line.<br>
                        • Immune to catastrophic ReDoS backtracking by construction.<br>
                        • Moore machine monitors per-IP state to flag brute-force guessing.
                    </p>
                </div>
                <div class="dark-card" style="border-left: 3px solid var(--wine-red);">
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 11pt; color: var(--gold-light); margin-bottom: 4px;">Neural Slow Path Controls</h3>
                    <p style="font-size: 7.8pt; color: var(--text-cream-dim); line-height: 1.5;">
                        • Memory-bounded queue (K = 1,000) prevents host OOM crashes.<br>
                        • Turing Machine scrubs cleartext credentials on tape prior to egress.<br>
                        • Strict JSON schema validates AI severity, evidence, and remediation rules.
                    </p>
                </div>
            </div>
        </div>
    </div>
    {btm_bar("SYSTEM ARCHITECTURE BLUEPRINT", "DUAL-LANE EXECUTION")}
</section>"""
with open(os.path.join(pages_dir, "page_7.html"), "w", encoding="utf-8") as f: f.write(p7)

# --- PAGE 8: LEXER & TOKENIZER (Dark Luxury Theme) ---
p8 = f"""<section class="page theme-dark">
    {top_hdr("SYMBOLIC ENGINE", "LEXER & TOKEN SPECIFICATION")}
    <div class="page-content" style="padding-top: 10mm;">
        <div>
            <h1 class="canva-title" style="font-size: 28pt; margin-bottom: 6px;">
                THE SYMBOLIC LEXER
            </h1>
            <h2 class="canva-subtitle">Character-Level Regular Expressions and Abstract Token Classification</h2>

            <div class="dark-card" style="margin-bottom: 14px; padding: 10px;">
                <table class="luxury-table">
                    <thead>
                        <tr>
                            <th>Token</th>
                            <th>POSIX Extended Regular Expression</th>
                            <th>Sample Lexeme</th>
                            <th>Semantic Role in Grammar</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong style="color:var(--gold-light);">LEVEL</strong></td>
                            <td style="font-family:'JetBrains Mono', monospace; color:#DFC4A8;">\\[INFO\\]</td>
                            <td>[INFO]</td>
                            <td>Establishes logging severity class boundary</td>
                        </tr>
                        <tr>
                            <td><strong style="color:var(--gold-light);">IP</strong></td>
                            <td style="font-family:'JetBrains Mono', monospace; color:#DFC4A8;">o\\.o\\.o\\.o (where o = 0..255)</td>
                            <td>192.168.1.50</td>
                            <td>Validates IPv4 octet bounds [0, 255]</td>
                        </tr>
                        <tr>
                            <td><strong style="color:var(--gold-light);">USER</strong></td>
                            <td style="font-family:'JetBrains Mono', monospace; color:#DFC4A8;">User_[A-Za-z0-9]+</td>
                            <td>User_Admin</td>
                            <td>Enforces identity naming standard</td>
                        </tr>
                        <tr>
                            <td><strong style="color:var(--gold-light);">STATUS</strong></td>
                            <td style="font-family:'JetBrains Mono', monospace; color:#DFC4A8;">Success | Failed</td>
                            <td>Success</td>
                            <td>Binary authentication outcome indicator</td>
                        </tr>
                        <tr>
                            <td><strong style="color:var(--gold-light);">OTHER</strong></td>
                            <td style="font-family:'JetBrains Mono', monospace; color:#DFC4A8;">.* (failing all above patterns)</td>
                            <td>DROP_TABLE</td>
                            <td>Catches malformed tokens, SQLi, flags</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div style="display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 14px;">
                <div class="dark-card">
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 11pt; color: var(--gold-light); margin-bottom: 6px;">Lexical Analysis Execution</h3>
                    <p style="font-size: 8pt; color: var(--text-cream-dim); line-height: 1.55;">
                        The C++ lexer partitions telemetry lines at whitespace delimiters. Each lexeme is matched against compiled regex patterns. 
                        <br><br>
                        IPv4 octet ranges are enforced mathematically: values exceeding 255 (e.g. <code>999.1.1.1</code>) fail the IP regex and are marked as <strong>OTHER</strong>, ensuring malicious spoofing is isolated before entering the automaton.
                    </p>
                </div>

                <div class="dark-card" style="background:#1B0E0D; border-color:var(--wine-red);">
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 11pt; color: var(--gold-light); margin-bottom: 6px;">Token Stream Sample</h3>
                    <div style="font-family:'JetBrains Mono', monospace; font-size:7pt; color:#EAE0D5; line-height:1.6;">
                        Input: [INFO] 192.168.1.50 DROP_TABLE User Success<br>
                        ────────────────────────────────<br>
                        [INFO]       ──► <span style="color:#2EA043;">LEVEL</span><br>
                        192.168.1.50 ──► <span style="color:#2EA043;">IP</span><br>
                        DROP_TABLE   ──► <span style="color:#DA3633; font-weight:bold;">OTHER [ANOMALY]</span><br>
                        User         ──► <span style="color:#DA3633;">OTHER</span> (Missing User_)<br>
                        Success      ──► <span style="color:#2EA043;">STATUS</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    {btm_bar("LEXICAL TOKENIZATION GRAMMAR", "POSIX COMPILED PATTERNS")}
</section>"""
with open(os.path.join(pages_dir, "page_8.html"), "w", encoding="utf-8") as f: f.write(p8)

# --- PAGE 9: THE MINIMAL BASELINE DFA (Cream Luxury Theme - Thumbnail 6) ---
p9 = f"""<section class="page theme-cream">
    {top_hdr("AUTOMATA DESIGN", "MINIMAL BASELINE DFA (TABLE 3)")}
    <div class="page-content" style="padding-top: 10mm;">
        <div>
            <div style="background: var(--wine-red); color: #FFF; padding: 10px 18px; border-radius: 4px; margin-bottom: 12px;">
                <h1 style="font-family: 'Playfair Display', serif; font-size: 24pt; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 3px;">
                    THE MINIMAL BASELINE DFA
                </h1>
                <p style="font-size: 8.5pt; color: #EAE0D5; letter-spacing: 1px; text-transform: uppercase;">
                    Mathematical 5-Tuple Formulation and State Transition Graph
                </p>
            </div>

            <!-- Large Clean DFA State Diagram -->
            <div class="cream-card" style="margin-bottom: 14px; padding: 14px; text-align: center;">
                <svg width="600" height="150" viewBox="0 0 600 150" fill="none">
                    <!-- q0 Start -->
                    <circle cx="50" cy="50" r="22" fill="#FAF5EE" stroke="#801818" stroke-width="2"/>
                    <text x="50" y="55" fill="#801818" font-family="'Playfair Display', serif" font-size="11" font-weight="bold" text-anchor="middle">q₀</text>
                    <path d="M15 50H28" stroke="#1E0F0E" stroke-width="2"/>
                    <polygon points="28,50 22,47 22,53" fill="#1E0F0E"/>
                    <text x="20" y="42" fill="#1E0F0E" font-size="7" font-weight="bold">start</text>

                    <!-- q0 -> q1 -->
                    <path d="M72 50H138" stroke="#801818" stroke-width="2"/>
                    <polygon points="138,50 132,47 132,53" fill="#801818"/>
                    <text x="105" y="42" fill="#801818" font-size="7.5" font-weight="bold" text-anchor="middle">LEVEL</text>

                    <!-- q1 -->
                    <circle cx="160" cy="50" r="22" fill="#FAF5EE" stroke="#801818" stroke-width="2"/>
                    <text x="160" y="55" fill="#801818" font-family="'Playfair Display', serif" font-size="11" font-weight="bold" text-anchor="middle">q₁</text>

                    <!-- q1 -> q2 -->
                    <path d="M182 50H248" stroke="#801818" stroke-width="2"/>
                    <polygon points="248,50 242,47 242,53" fill="#801818"/>
                    <text x="215" y="42" fill="#801818" font-size="7.5" font-weight="bold" text-anchor="middle">IP</text>

                    <!-- q2 -->
                    <circle cx="270" cy="50" r="22" fill="#FAF5EE" stroke="#801818" stroke-width="2"/>
                    <text x="270" y="55" fill="#801818" font-family="'Playfair Display', serif" font-size="11" font-weight="bold" text-anchor="middle">q₂</text>

                    <!-- q2 -> q3 -->
                    <path d="M292 50H358" stroke="#801818" stroke-width="2"/>
                    <polygon points="358,50 352,47 352,53" fill="#801818"/>
                    <text x="325" y="42" fill="#801818" font-size="7.5" font-weight="bold" text-anchor="middle">USER</text>

                    <!-- q3 -->
                    <circle cx="380" cy="50" r="22" fill="#FAF5EE" stroke="#801818" stroke-width="2"/>
                    <text x="380" y="55" fill="#801818" font-family="'Playfair Display', serif" font-size="11" font-weight="bold" text-anchor="middle">q₃</text>

                    <!-- q3 -> q4 -->
                    <path d="M402 50H468" stroke="#238636" stroke-width="2"/>
                    <polygon points="468,50 462,47 462,53" fill="#238636"/>
                    <text x="435" y="42" fill="#238636" font-size="7.5" font-weight="bold" text-anchor="middle">STATUS</text>

                    <!-- q4 Final -->
                    <circle cx="490" cy="50" r="24" fill="#FAF5EE" stroke="#238636" stroke-width="2"/>
                    <circle cx="490" cy="50" r="20" fill="#FAF5EE" stroke="#238636" stroke-width="1.5"/>
                    <text x="490" y="55" fill="#238636" font-family="'Playfair Display', serif" font-size="11" font-weight="bold" text-anchor="middle">q₄</text>
                    <text x="490" y="88" fill="#238636" font-size="7" font-weight="bold" text-anchor="middle">ACCEPT</text>

                    <!-- Trap State qE -->
                    <circle cx="270" cy="115" r="20" fill="#FFF" stroke="#DA3633" stroke-width="2" stroke-dasharray="3 2"/>
                    <text x="270" y="120" fill="#DA3633" font-family="'Playfair Display', serif" font-size="10" font-weight="bold" text-anchor="middle">qE</text>
                    <text x="270" y="96" fill="#DA3633" font-size="7" font-weight="bold" text-anchor="middle">TRAP STATE (REJECT)</text>

                    <!-- Arrows to Trap -->
                    <path d="M50 72V115H250" stroke="#DA3633" stroke-width="1" stroke-dasharray="2 2"/>
                    <path d="M160 72V105H250" stroke="#DA3633" stroke-width="1" stroke-dasharray="2 2"/>
                    <path d="M270 72V95" stroke="#DA3633" stroke-width="1" stroke-dasharray="2 2"/>
                    <path d="M380 72V105H290" stroke="#DA3633" stroke-width="1" stroke-dasharray="2 2"/>
                    <path d="M490 74V115H290" stroke="#DA3633" stroke-width="1" stroke-dasharray="2 2"/>

                    <!-- Loop on qE -->
                    <path d="M260 135C260 148 280 148 280 135" stroke="#DA3633" stroke-width="1.5"/>
                    <text x="270" y="148" fill="#DA3633" font-size="6.5" text-anchor="middle">Σ (any token)</text>
                </svg>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
                <div class="cream-card">
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 11pt; color: var(--wine-red); margin-bottom: 6px;">
                        Formal 5-Tuple Definition
                    </h3>
                    <p style="font-size: 8pt; color: var(--text-dark-secondary); line-height: 1.55;">
                        • <strong>State Set Q:</strong> {{ q₀, q₁, q₂, q₃, q₄, qE }}<br>
                        • <strong>Alphabet Σ:</strong> {{ LEVEL, IP, USER, STATUS, OTHER }}<br>
                        • <strong>Start State q₀:</strong> Unconsumed initial state.<br>
                        • <strong>Accept State F:</strong> {{ q₄ }} (Double Circle).<br>
                        • <strong>Trap State qE:</strong> Absorbing error sink.
                    </p>
                </div>

                <div class="cream-card">
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 11pt; color: var(--wine-red); margin-bottom: 6px;">
                        Strict Sequential Determinism
                    </h3>
                    <p style="font-size: 8pt; color: var(--text-dark-secondary); line-height: 1.55;">
                        The forward sequence represents the strict grammar of standard authentication logs. Because every state has exactly one valid forward transition and all invalid tokens lead to <em>qE</em>, the automaton executes deterministically without backtracking or recursion.
                    </p>
                </div>
            </div>
        </div>
    </div>
    {btm_bar("DETERMINISTIC FINITE AUTOMATA", "TABLE 3 MINIMAL FORMULATION")}
</section>"""
with open(os.path.join(pages_dir, "page_9.html"), "w", encoding="utf-8") as f: f.write(p9)

# --- PAGE 10: TRANSITION MATRIX & MINIMALITY PROOF (Dark Luxury Theme) ---
p10 = f"""<section class="page theme-dark">
    {top_hdr("MATHEMATICAL PROOFS", "TRANSITION MATRIX & MINIMALITY")}
    <div class="page-content" style="padding-top: 10mm;">
        <div>
            <h1 class="canva-title" style="font-size: 28pt; margin-bottom: 6px;">
                TRANSITION MATRIX & PROOF
            </h1>
            <h2 class="canva-subtitle">Total Transition Function δ (Table 3) and Myhill-Nerode Minimality Proof</h2>

            <div class="dark-card" style="margin-bottom: 12px; padding: 10px;">
                <table class="luxury-table">
                    <thead>
                        <tr>
                            <th>State q ∈ Q</th>
                            <th>LEVEL</th>
                            <th>IP</th>
                            <th>USER</th>
                            <th>STATUS</th>
                            <th>OTHER</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong style="color:var(--gold-light);">→ q₀ (Start)</strong></td>
                            <td style="color:#2EA043; font-weight:bold;">q₁</td>
                            <td>qE</td><td>qE</td><td>qE</td><td>qE</td>
                            <td>Start</td>
                        </tr>
                        <tr>
                            <td><strong style="color:var(--gold-light);">q₁</strong></td>
                            <td>qE</td>
                            <td style="color:#2EA043; font-weight:bold;">q₂</td>
                            <td>qE</td><td>qE</td><td>qE</td>
                            <td>Intermediate</td>
                        </tr>
                        <tr>
                            <td><strong style="color:var(--gold-light);">q₂</strong></td>
                            <td>qE</td><td>qE</td>
                            <td style="color:#2EA043; font-weight:bold;">q₃</td>
                            <td>qE</td><td>qE</td>
                            <td>Intermediate</td>
                        </tr>
                        <tr>
                            <td><strong style="color:var(--gold-light);">q₃</strong></td>
                            <td>qE</td><td>qE</td><td>qE</td>
                            <td style="color:#2EA043; font-weight:bold;">q₄</td>
                            <td>qE</td>
                            <td>Intermediate</td>
                        </tr>
                        <tr>
                            <td><strong style="color:var(--gold-light);">q₄ (Final)</strong></td>
                            <td>qE</td><td>qE</td><td>qE</td><td>qE</td><td>qE</td>
                            <td style="color:#2EA043; font-weight:bold;">ACCEPT</td>
                        </tr>
                        <tr>
                            <td><strong style="color:var(--gold-light);">qE (Trap)</strong></td>
                            <td>qE</td><td>qE</td><td>qE</td><td>qE</td><td>qE</td>
                            <td style="color:#DA3633; font-weight:bold;">REJECT</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="dark-card" style="border-left: 3px solid var(--gold); background: #261211;">
                <h3 style="font-family: 'Playfair Display', serif; font-size: 11pt; color: var(--gold-light); margin-bottom: 6px;">
                    Proof of Minimality (Myhill-Nerode Equivalence Theorem)
                </h3>
                <p style="font-size: 7.8pt; color: var(--text-cream-dim); line-height: 1.55;">
                    <strong>Theorem:</strong> The baseline automaton <em>M</em> has the minimal possible number of states for language <em>L</em><sub>baseline</sub>.
                    <br>
                    <strong>Proof:</strong> Under the Myhill-Nerode theorem, two states <em>p, q</em> are equivalent (<em>p ≡ q</em>) iff for all strings <em>z</em> ∈ Σ*, δ̂(<em>p, z</em>) ∈ F ⇔ δ̂(<em>q, z</em>) ∈ F. We evaluate distinguishing suffixes:
                    <br><br>
                    • Suffix z = ε distinguishes q₄ (since q₄ ∈ F) from {{ q₀, q₁, q₂, q₃, qE }} (since none ∈ F).<br>
                    • Suffix z = STATUS distinguishes q₃ (leading to q₄ ∈ F) from {{ q₀, q₁, q₂, qE }} (leading to qE ∉ F).<br>
                    • Suffix z = USER · STATUS distinguishes q₂ from {{ q₀, q₁, qE }}.<br>
                    • Suffix z = IP · USER · STATUS distinguishes q₁ from {{ q₀, qE }}.<br>
                    • Suffix z = LEVEL · IP · USER · STATUS distinguishes q₀ from qE.<br>
                    <br>
                    Every state pair (<em>p, q</em>) is pairwise distinguishable. Therefore, no states can be merged, and the automaton is mathematically minimal with |Q| = 6. ∎
                </p>
            </div>
        </div>
    </div>
    {btm_bar("FORMAL MINIMALITY PROOF", "MYHILL-NERODE EQUIVALENCE THEOREM")}
</section>"""
with open(os.path.join(pages_dir, "page_10.html"), "w", encoding="utf-8") as f: f.write(p10)

print("[✓] Generated Pages 6, 7, 8, 9, 10.")

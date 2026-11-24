import os

report_dir = r"C:\Users\Ritesh Kumar Agarwal\.gemini\antigravity\scratch\hybrid-anomaly-engine\report"
pages_dir = os.path.join(report_dir, "canva_pages")

def top_hdr(left="JIIT NOIDA • CSE DEPARTMENT", right="THEORY OF COMPUTATION (24B11CS212)"):
    return f"""<div class="canva-top-header"><span>{left}</span><span>{right}</span></div>"""

def btm_bar(left="PREPARED BY: DIVYANSH AGARWAL & TEAM", right="SESSION 2026–2027 • B.TECH CSE"):
    return f"""<div class="canva-bottom-bar"><span>{left}</span><span>{right}</span></div>"""

# ==============================================================================
# PAGE 6: CHOMSKY HIERARCHY MAPPING (Cream Luxury Theme)
# ==============================================================================
p6 = f"""<section class="page theme-cream">
    {top_hdr("FORMAL LANGUAGE THEORY", "CHOMSKY HIERARCHY & COMPUTATIONAL BOUNDS")}
    <div class="page-content" style="padding-top: 5mm; padding-bottom: 5mm; justify-content: space-between;">
        
        <div>
            <div class="gold-eyebrow" style="color: var(--wine-red);">THEORETICAL TAXONOMY</div>
            <h1 class="canva-title" style="color: var(--wine-red); font-size: 28pt; margin-bottom: 3mm;">
                FORMAL LANGUAGE THEORY &amp; CHOMSKY HIERARCHY
            </h1>
            <div class="gold-separator-line" style="background: linear-gradient(90deg, var(--wine-red), transparent);"></div>
        </div>

        <!-- Middle: SVG Diagram & Theoretical Framing -->
        <div style="display: grid; grid-template-columns: 1.15fr 1fr; gap: 20px; align-items: center; margin-bottom: 3.5mm;">
            <!-- Concentric Chomsky Venn Diagram -->
            <div class="cream-card" style="padding: 12px; border: 1.5px solid rgba(128, 24, 24, 0.25); text-align: center;">
                <span style="font-family: 'Cinzel', serif; font-size: 8pt; color: var(--wine-red); letter-spacing: 1.5px; text-transform: uppercase; font-weight: bold; display: block; margin-bottom: 6px;">
                    FIGURE 3: CONCENTRIC COMPUTATIONAL EXPRESSIVENESS
                </span>
                <svg viewBox="0 0 320 220" style="width: 100%; height: 190px; display: block;">
                    <!-- Type 0: Recursively Enumerable -->
                    <ellipse cx="160" cy="110" rx="150" ry="98" fill="rgba(128, 24, 24, 0.08)" stroke="#801818" stroke-width="1.8" />
                    <text x="160" y="28" text-anchor="middle" fill="#801818" font-family="Cinzel" font-size="8.5" font-weight="bold">TYPE 0: RECURSIVELY ENUMERABLE (TURING MACHINE / LLM)</text>

                    <!-- Type 1: Context Sensitive -->
                    <ellipse cx="160" cy="118" rx="120" ry="76" fill="rgba(183, 121, 31, 0.08)" stroke="#B7791F" stroke-width="1.5" />
                    <text x="160" y="56" text-anchor="middle" fill="#B7791F" font-family="Cinzel" font-size="8" font-weight="bold">TYPE 1: CONTEXT-SENSITIVE (LBA)</text>

                    <!-- Type 2: Context Free -->
                    <ellipse cx="160" cy="126" rx="90" ry="54" fill="rgba(49, 130, 206, 0.08)" stroke="#3182CE" stroke-width="1.5" />
                    <text x="160" y="85" text-anchor="middle" fill="#2B6CB0" font-family="Cinzel" font-size="7.5" font-weight="bold">TYPE 2: CONTEXT-FREE (PDA)</text>

                    <!-- Type 3: Regular Languages -->
                    <ellipse cx="160" cy="138" rx="60" ry="34" fill="rgba(56, 161, 105, 0.15)" stroke="#2EA043" stroke-width="2" />
                    <text x="160" y="134" text-anchor="middle" fill="#22543D" font-family="Cinzel" font-size="8" font-weight="bold">TYPE 3: REGULAR</text>
                    <text x="160" y="146" text-anchor="middle" fill="#22543D" font-family="JetBrains Mono" font-size="6.5">DFA &bull; Moore &bull; O(N)</text>
                </svg>
            </div>

            <!-- Conceptual Narrative Cards -->
            <div style="display: flex; flex-direction: column; gap: 10px;">
                <div class="cream-card" style="border-left: 3px solid #2EA043; padding: 10px 12px;">
                    <strong style="color: #2EA043; font-size: 8.5pt;">Type-3 Regular Subsystem (DFA &amp; Moore):</strong>
                    <p style="font-size: 7.8pt; color: var(--text-dark-secondary); line-height: 1.5; margin-top: 3px;">
                        Operates under finite internal states without external auxiliary memory. Validates sequential log syntax and counts failure bursts in strict O(N) linear time and O(1) space.
                    </p>
                </div>
                <div class="cream-card" style="border-left: 3px solid #801818; padding: 10px 12px;">
                    <strong style="color: var(--wine-red); font-size: 8.5pt;">Type-0 Turing Subsystem (TM &amp; LLM Oracle):</strong>
                    <p style="font-size: 7.8pt; color: var(--text-dark-secondary); line-height: 1.5; margin-top: 3px;">
                        Possesses an unbounded read/write tape. Performs in-place credential scrubbing and unconstrained semantic intent classification on complex attack vectors.
                    </p>
                </div>
            </div>
        </div>

        <!-- Bottom: Formal Chomsky Mapping Table -->
        <div class="luxury-table-container">
            <table class="luxury-table" style="font-size: 7.5pt;">
                <thead>
                    <tr>
                        <th>Chomsky Level</th>
                        <th>Grammar Type</th>
                        <th>Abstract Machine</th>
                        <th>Memory Model</th>
                        <th>Engine Architectural Role</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Type 3</strong></td>
                        <td>Regular Grammar</td>
                        <td>Deterministic Finite Automaton (DFA)</td>
                        <td>Finite internal state register (Q)</td>
                        <td>Line-rate syntactic token validation (1.8 &mu;s fast path)</td>
                    </tr>
                    <tr>
                        <td><strong>Type 3+</strong></td>
                        <td>Finite State Transducer</td>
                        <td>Moore Sequential Machine</td>
                        <td>Per-IP session state mapping</td>
                        <td>Stateful brute-force tracking &amp; threshold attack flagging</td>
                    </tr>
                    <tr>
                        <td><strong>Type 2</strong></td>
                        <td>Context-Free Grammar</td>
                        <td>Pushdown Automaton (PDA)</td>
                        <td>Last-In, First-Out (LIFO) Stack</td>
                        <td>Nested JSON / RPC payload parsing (Phase 2 roadmap)</td>
                    </tr>
                    <tr>
                        <td><strong>Type 0</strong></td>
                        <td>Unrestricted Grammar</td>
                        <td>Turing Machine / Transformer LLM</td>
                        <td>Unbounded Read/Write Tape</td>
                        <td>Deterministic tape secret masking &amp; semantic reasoning</td>
                    </tr>
                </tbody>
            </table>
        </div>

    </div>
    {btm_bar("FORMAL LANGUAGE THEORY & TAXONOMY", "SECTION 2.1 • CHOMSKY HIERARCHY")}
</section>"""
with open(os.path.join(pages_dir, "page_6.html"), "w", encoding="utf-8") as f: f.write(p6)

# ==============================================================================
# PAGE 7: DUAL-LANE ENGINE BLUEPRINT (Dark Luxury Theme)
# ==============================================================================
p7 = f"""<section class="page theme-dark">
    {top_hdr("ENGINE ARCHITECTURE", "DUAL-LANE NEURO-SYMBOLIC BLUEPRINT")}
    <div class="page-content" style="padding-top: 5mm; padding-bottom: 5mm; justify-content: space-between;">
        
        <div>
            <div class="gold-eyebrow">SYSTEM BLUEPRINT</div>
            <h1 class="canva-title" style="font-size: 28pt; margin-bottom: 3mm;">
                DUAL-LANE ENGINE BLUEPRINT
            </h1>
            <div class="gold-separator-line"></div>
        </div>

        <!-- Upper: Full-Width End-to-End Pipeline SVG -->
        <div class="dark-card" style="padding: 12px 14px; background: #231211; margin-bottom: 3.5mm;">
            <div style="text-align: center; margin-bottom: 6px;">
                <span style="font-family: 'Cinzel', serif; font-size: 8pt; letter-spacing: 2px; color: var(--gold); text-transform: uppercase;">
                    FIGURE 4: UNIFIED HYBRID AUTOMATA &amp; NEURAL ESCALATION TOPOLOGY
                </span>
            </div>
            <svg viewBox="0 0 680 180" style="width: 100%; height: 160px; display: block;">
                <!-- Node 1: Raw Log -->
                <rect x="10" y="65" width="80" height="45" rx="5" fill="#1C0C0B" stroke="#8F7255" stroke-width="1.5" />
                <text x="50" y="84" text-anchor="middle" fill="#DFC4A8" font-family="Cinzel" font-size="7.5" font-weight="bold">RAW LOG</text>
                <text x="50" y="98" text-anchor="middle" fill="#9E8C82" font-size="6.5">100k+ eps</text>

                <!-- Arrow 1 -> 2 -->
                <line x1="90" y1="87" x2="115" y2="87" stroke="#C59F7A" stroke-width="1.8" />

                <!-- Node 2: Lexer -->
                <rect x="115" y="65" width="95" height="45" rx="5" fill="#1C0C0B" stroke="#8F7255" stroke-width="1.5" />
                <text x="162" y="84" text-anchor="middle" fill="#DFC4A8" font-family="Cinzel" font-size="7.5" font-weight="bold">POSIX LEXER</text>
                <text x="162" y="98" text-anchor="middle" fill="#68D391" font-family="JetBrains Mono" font-size="6">5 Token Types</text>

                <!-- Arrow 2 -> 3 -->
                <line x1="210" y1="87" x2="235" y2="87" stroke="#C59F7A" stroke-width="1.8" />

                <!-- Node 3: DFA Engine -->
                <rect x="235" y="55" width="105" height="65" rx="6" fill="#801818" stroke="#C59F7A" stroke-width="2" />
                <text x="287" y="76" text-anchor="middle" fill="#FFF" font-family="Cinzel" font-size="8" font-weight="bold">DFA ENGINE</text>
                <text x="287" y="90" text-anchor="middle" fill="#DFC4A8" font-size="6.5">Table 3 Matrix</text>
                <text x="287" y="104" text-anchor="middle" fill="#68D391" font-family="JetBrains Mono" font-size="6.5" font-weight="bold">q0..q4 / qE</text>

                <!-- Accept Path: Upwards to Moore -->
                <path d="M 340 75 L 375 75 L 375 40 L 400 40" fill="none" stroke="#38A169" stroke-width="1.8" />
                <text x="375" y="60" text-anchor="middle" fill="#68D391" font-family="JetBrains Mono" font-size="6" font-weight="bold">ACCEPT</text>

                <!-- Node 4: Moore Machine -->
                <rect x="400" y="20" width="105" height="42" rx="5" fill="#1C0C0B" stroke="#38A169" stroke-width="1.5" />
                <text x="452" y="38" text-anchor="middle" fill="#68D391" font-family="Cinzel" font-size="7.5" font-weight="bold">MOORE FSM</text>
                <text x="452" y="51" text-anchor="middle" fill="#9E8C82" font-size="6">m0..m3 Per-IP</text>

                <!-- Moore OK -> Local Store -->
                <line x1="505" y1="41" x2="555" y2="41" stroke="#38A169" stroke-width="1.8" />
                <rect x="555" y="20" width="115" height="42" rx="5" fill="#152418" stroke="#38A169" stroke-width="1.5" />
                <text x="612" y="38" text-anchor="middle" fill="#68D391" font-family="Cinzel" font-size="7.5" font-weight="bold">LOCAL STORE</text>
                <text x="612" y="51" text-anchor="middle" fill="#A0AEC0" font-size="6">1.8 &mu;s &bull; $0.00 Cost</text>

                <!-- Reject & Flag Paths to Turing Sanitizer -->
                <path d="M 340 100 L 400 100 L 400 135 L 420 135" fill="none" stroke="#E53E3E" stroke-width="1.8" />
                <text x="375" y="112" text-anchor="middle" fill="#FEB2B2" font-family="JetBrains Mono" font-size="6" font-weight="bold">REJECT (qE)</text>

                <path d="M 452 62 L 452 110" fill="none" stroke="#E53E3E" stroke-width="1.8" />
                <text x="466" y="90" text-anchor="middle" fill="#FEB2B2" font-family="JetBrains Mono" font-size="6" font-weight="bold">FLAG</text>

                <!-- Node 5: Turing Sanitizer -->
                <rect x="420" y="115" width="115" height="45" rx="5" fill="#421212" stroke="#E53E3E" stroke-width="1.8" />
                <text x="477" y="134" text-anchor="middle" fill="#FFF" font-family="Cinzel" font-size="7.5" font-weight="bold">7-TUPLE TM SANITIZER</text>
                <text x="477" y="148" text-anchor="middle" fill="#FFBABA" font-size="6">Overwrites Secrets with 'X'</text>

                <!-- Arrow to Neural Escalation -->
                <line x1="535" y1="137" x2="560" y2="137" stroke="#E53E3E" stroke-width="1.8" />

                <!-- Node 6: Neural LLM -->
                <rect x="560" y="115" width="110" height="45" rx="5" fill="#1C0C0B" stroke="#E53E3E" stroke-width="1.5" />
                <text x="615" y="134" text-anchor="middle" fill="#FF6B6B" font-family="Cinzel" font-size="7.5" font-weight="bold">NEURAL LLM API</text>
                <text x="615" y="148" text-anchor="middle" fill="#DFC4A8" font-size="6">Bounded Ring Buffer (K=1k)</text>
            </svg>
        </div>

        <!-- Middle: Two Deep Architectural Guarantee Cards -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 18px; margin-bottom: 3.5mm;">
            <div class="dark-card" style="border-left: 3px solid #2EA043;">
                <h3 style="font-family: 'Playfair Display', serif; font-size: 11pt; color: #68D391; margin-bottom: 6px;">
                    Symbolic Fast-Path Guarantees
                </h3>
                <p style="font-size: 7.8pt; color: var(--text-cream-dim); line-height: 1.55;">
                    &bull; <strong>Strict Deterministic Time:</strong> Operates at O(N) where N is token stream length. Zero state backtracking eliminates ReDoS exploits.<br>
                    &bull; <strong>Zero Dynamic Allocations:</strong> Evaluates logs using lightweight string views and contiguous transition table offsets.<br>
                    &bull; <strong>Temporal Session Tracking:</strong> Moore machine tracks per-IP authentication failures in an O(1) hash map without cross-IP contention.
                </p>
            </div>

            <div class="dark-card" style="border-left: 3px solid var(--wine-red);">
                <h3 style="font-family: 'Playfair Display', serif; font-size: 11pt; color: #FF6B6B; margin-bottom: 6px;">
                    Neural Slow-Path Controls
                </h3>
                <p style="font-size: 7.8pt; color: var(--text-cream-dim); line-height: 1.55;">
                    &bull; <strong>Deterministic PII Redaction:</strong> Turing machine tape head masks plaintext passwords and auth tokens prior to network egress.<br>
                    &bull; <strong>Bounded Buffer Queue (K=1,000):</strong> Protects system memory from exhaustion during distributed denial-of-service spikes.<br>
                    &bull; <strong>Asynchronous Non-Blocking I/O:</strong> libcurl multi-socket transfers prevent worker thread blocking while querying LLM APIs.
                </p>
            </div>
        </div>

        <!-- Bottom: Architectural Invariant Banner -->
        <div class="dark-card" style="background: #170A09; border: 1px solid var(--border-gold); padding: 8px 14px; text-align: center;">
            <span style="font-family: 'Cinzel'; font-size: 7.5pt; color: var(--gold-light); letter-spacing: 1.5px;">
                ARCHITECTURAL INVARIANT: NO RAW CREDENTIAL CROSSES THE TRUST BOUNDARY &bull; NO LOG BYPASSES DETERMINISTIC DFA AUDIT
            </span>
        </div>

    </div>
    {btm_bar("ENGINE ARCHITECTURE BLUEPRINT", "SECTION 2.2 • DUAL-LANE EXECUTION")}
</section>"""
with open(os.path.join(pages_dir, "page_7.html"), "w", encoding="utf-8") as f: f.write(p7)

# ==============================================================================
# PAGE 8: SYMBOLIC LEXER & TOKEN DECOMPOSITION (Dark Luxury Theme)
# ==============================================================================
p8 = f"""<section class="page theme-dark">
    {top_hdr("LEXICAL ANALYSIS", "CHARACTER-LEVEL POSIX REGULAR TOKENIZER")}
    <div class="page-content" style="padding-top: 5mm; padding-bottom: 5mm; justify-content: space-between;">
        
        <div>
            <div class="gold-eyebrow">FRONT-END TOKENIZATION</div>
            <h1 class="canva-title" style="font-size: 28pt; margin-bottom: 3mm;">
                THE SYMBOLIC LEXER: ATOMIC TOKENIZATION
            </h1>
            <div class="gold-separator-line"></div>
        </div>

        <!-- Middle: Token Taxonomy & Grammar Specification -->
        <div style="display: grid; grid-template-columns: 1.15fr 1fr; gap: 20px; align-items: start; margin-bottom: 3.5mm;">
            <div class="dark-card" style="border-left: 3px solid var(--gold);">
                <h3 style="font-family: 'Playfair Display', serif; font-size: 11pt; color: var(--gold-light); margin-bottom: 6px;">
                    Deterministic Token Grammar &Sigma;
                </h3>
                <p style="font-size: 7.8pt; color: var(--text-cream-dim); line-height: 1.55; margin-bottom: 8px;">
                    The lexical analyzer translates unstructured ASCII character streams into discrete formal tokens conforming to alphabet <strong>&Sigma; = {{ LEVEL, IP, USER, STATUS, OTHER }}</strong>:
                </p>
                <div style="display: flex; flex-direction: column; gap: 5px; font-size: 7.4pt; font-family: 'JetBrains Mono', monospace;">
                    <div><span class="token-badge token-level">LEVEL</span> <code>^(Accepted|Failed|Invalid|error|FATAL)</code></div>
                    <div><span class="token-badge token-ip">IP</span> <code>^([0-9]{{1,3}}\\.){{3}}[0-9]{{1,3}}</code></div>
                    <div><span class="token-badge token-user">USER</span> <code>^[a-zA-Z0-9_\\-\\.]{{1,32}}</code></div>
                    <div><span class="token-badge token-status">STATUS</span> <code>^(port\\s+[0-9]+|ssh2|publickey|password)</code></div>
                    <div><span class="token-badge token-other">OTHER</span> <code>[^\\s]+</code> <span style="color:#FF6B6B;">(Injection Catchall)</span></div>
                </div>
            </div>

            <div class="dark-card" style="border-left: 3px solid var(--wine-red);">
                <h3 style="font-family: 'Playfair Display', serif; font-size: 11pt; color: var(--gold-light); margin-bottom: 6px;">
                    ReDoS Immunity Guarantee
                </h3>
                <p style="font-size: 7.8pt; color: var(--text-cream-dim); line-height: 1.55;">
                    Vulnerable regex implementations rely on recursive backtracking engines. If an attacker injects nested repetitions, processing time scales exponentially: O(2<sup>N</sup>). Our lexer constructs deterministic linear passes without lookahead or backtracking, mathematically bounding execution time to <strong>O(N)</strong>.
                </p>
            </div>
        </div>

        <!-- Token Decomposition Trace Table -->
        <div class="luxury-table-container" style="margin-bottom: 3.5mm;">
            <table class="luxury-table" style="font-size: 7.4pt;">
                <thead>
                    <tr>
                        <th>Raw Telemetry Log Record</th>
                        <th>Extracted Token Sequence</th>
                        <th>DFA Final State</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><code>Accepted password for root from 192.168.1.100 port 22</code></td>
                        <td>LEVEL &bull; USER &bull; IP &bull; STATUS</td>
                        <td style="color:#2EA043; font-weight:bold;">q4 (ACCEPT)</td>
                        <td style="color:#2EA043;">Fast-Path Store ($0)</td>
                    </tr>
                    <tr>
                        <td><code>Failed password for root' OR '1'='1-- from 10.0.0.99</code></td>
                        <td>LEVEL &bull; USER &bull; <strong style="color:#FF6B6B;">OTHER</strong></td>
                        <td style="color:#E53E3E; font-weight:bold;">qE (TRAP)</td>
                        <td style="color:#FF6B6B;">TM Mask &bull; Escalate</td>
                    </tr>
                    <tr>
                        <td><code>Invalid user admin from 172.16.0.4 port 44122 ssh2</code></td>
                        <td>LEVEL &bull; USER &bull; IP &bull; STATUS</td>
                        <td style="color:#2EA043; font-weight:bold;">q4 (ACCEPT)</td>
                        <td style="color:#2EA043;">Moore Track &bull; Store</td>
                    </tr>
                    <tr>
                        <td><code>User admin pass=SecretPass123! token=LIVE_KEY_99</code></td>
                        <td>USER &bull; <strong style="color:#FF6B6B;">OTHER &bull; OTHER</strong></td>
                        <td style="color:#E53E3E; font-weight:bold;">qE (TRAP)</td>
                        <td style="color:#FF6B6B;">Scrub Secrets &bull; Alert</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="dark-card" style="background: #170A09; border: 1px solid var(--border-gold); padding: 8px 14px; text-align: center;">
            <span style="font-family: 'Cinzel'; font-size: 7.5pt; color: var(--gold-light); letter-spacing: 1.5px;">
                THE UNQUOTED SQL QUOTE REPRESENTS AN UNEXPECTED ALPHABET SYMBOL, FORCING IMMEDIATE TRAP SINK ESCALATION
            </span>
        </div>

    </div>
    {btm_bar("LEXICAL TOKENIZATION ENGINE", "SECTION 2.3 • TOKEN GRAMMAR & REDOS IMMUNITY")}
</section>"""
with open(os.path.join(pages_dir, "page_8.html"), "w", encoding="utf-8") as f: f.write(p8)

# ==============================================================================
# PAGE 9: MINIMAL BASELINE DFA (Cream Luxury Theme - Thumbnail 6)
# ==============================================================================
p9 = f"""<section class="page theme-cream">
    {top_hdr("AUTOMATA DESIGN", "MINIMAL BASELINE DFA (TABLE 3 FORMULATION)")}
    <div class="page-content" style="padding-top: 5mm; padding-bottom: 5mm; justify-content: space-between;">
        
        <div>
            <div class="gold-eyebrow" style="color: var(--wine-red);">DETERMINISTIC FINITE AUTOMATON</div>
            <div style="background: var(--wine-red); border-radius: 8px; padding: 10px 18px; margin-bottom: 3.5mm; box-shadow: 0 4px 15px rgba(128, 24, 24, 0.2);">
                <h1 class="canva-title" style="color: #FFFFFF; font-size: 24pt; margin-bottom: 2px;">
                    THE MINIMAL BASELINE DFA
                </h1>
                <p style="font-size: 8pt; color: var(--gold-light); font-family: 'Cinzel', serif; letter-spacing: 1.5px; text-transform: uppercase;">
                    MATHEMATICAL 5-TUPLE FORMULATION AND STATE TRANSITION GRAPH
                </p>
            </div>
        </div>

        <!-- Large State Transition SVG Diagram -->
        <div class="cream-card" style="padding: 12px; border: 1.5px solid rgba(128, 24, 24, 0.3); background: #FFFFFF; margin-bottom: 3.5mm;">
            <div style="text-align: center; margin-bottom: 6px;">
                <span style="font-family: 'Cinzel', serif; font-size: 8pt; letter-spacing: 2px; color: var(--wine-red); text-transform: uppercase; font-weight: bold;">
                    FIGURE 5: 6-STATE MINIMAL RECOGNIZER TOPOLOGY
                </span>
            </div>

            <svg viewBox="0 0 680 180" style="width: 100%; height: 165px; display: block;">
                <!-- Start Arrow -->
                <line x1="15" y1="65" x2="45" y2="65" stroke="#1E0F0E" stroke-width="2" marker-end="url(#gold-arr)" />
                <text x="30" y="55" text-anchor="middle" font-family="Plus Jakarta Sans" font-size="7.5" font-weight="bold">start</text>

                <!-- State q0 -->
                <circle cx="75" cy="65" r="26" fill="#FFF" stroke="#801818" stroke-width="2.5" />
                <text x="75" y="71" text-anchor="middle" fill="#801818" font-family="Playfair Display" font-size="13" font-weight="bold">q₀</text>

                <!-- Transition q0 -> q1 -->
                <line x1="101" y1="65" x2="169" y2="65" stroke="#801818" stroke-width="2" marker-end="url(#gold-arr)" />
                <text x="135" y="55" text-anchor="middle" fill="#801818" font-size="7.5" font-weight="bold">LEVEL</text>

                <!-- State q1 -->
                <circle cx="195" cy="65" r="26" fill="#FFF" stroke="#801818" stroke-width="2.5" />
                <text x="195" y="71" text-anchor="middle" fill="#801818" font-family="Playfair Display" font-size="13" font-weight="bold">q₁</text>

                <!-- Transition q1 -> q2 -->
                <line x1="221" y1="65" x2="289" y2="65" stroke="#801818" stroke-width="2" marker-end="url(#gold-arr)" />
                <text x="255" y="55" text-anchor="middle" fill="#801818" font-size="7.5" font-weight="bold">IP</text>

                <!-- State q2 -->
                <circle cx="315" cy="65" r="26" fill="#FFF" stroke="#801818" stroke-width="2.5" />
                <text x="315" y="71" text-anchor="middle" fill="#801818" font-family="Playfair Display" font-size="13" font-weight="bold">q₂</text>

                <!-- Transition q2 -> q3 -->
                <line x1="341" y1="65" x2="409" y2="65" stroke="#801818" stroke-width="2" marker-end="url(#gold-arr)" />
                <text x="375" y="55" text-anchor="middle" fill="#801818" font-size="7.5" font-weight="bold">USER</text>

                <!-- State q3 -->
                <circle cx="435" cy="65" r="26" fill="#FFF" stroke="#801818" stroke-width="2.5" />
                <text x="435" y="71" text-anchor="middle" fill="#801818" font-family="Playfair Display" font-size="13" font-weight="bold">q₃</text>

                <!-- Transition q3 -> q4 -->
                <line x1="461" y1="65" x2="529" y2="65" stroke="#2EA043" stroke-width="2.5" marker-end="url(#gold-arr)" />
                <text x="495" y="55" text-anchor="middle" fill="#2EA043" font-size="7.5" font-weight="bold">STATUS</text>

                <!-- Accept State q4 (Double Circle) -->
                <circle cx="555" cy="65" r="26" fill="#F0FFF4" stroke="#2EA043" stroke-width="2.5" />
                <circle cx="555" cy="65" r="20" fill="#F0FFF4" stroke="#2EA043" stroke-width="1.5" />
                <text x="555" y="71" text-anchor="middle" fill="#2EA043" font-family="Playfair Display" font-size="13" font-weight="bold">q₄</text>
                <text x="555" y="105" text-anchor="middle" fill="#2EA043" font-size="7.5" font-weight="bold">ACCEPT</text>

                <!-- Trap State qE -->
                <circle cx="315" cy="140" r="24" fill="#FFF5F5" stroke="#E53E3E" stroke-width="2" stroke-dasharray="4,3" />
                <text x="315" y="146" text-anchor="middle" fill="#E53E3E" font-family="Playfair Display" font-size="12" font-weight="bold">qE</text>
                <text x="315" y="174" text-anchor="middle" fill="#E53E3E" font-size="6.8" font-weight="bold">TRAP (REJECT)</text>

                <!-- Trap transitions -->
                <path d="M 75 91 L 75 140 L 291 140" fill="none" stroke="#E53E3E" stroke-width="1.2" stroke-dasharray="3,3" />
                <path d="M 195 91 L 195 130 L 291 135" fill="none" stroke="#E53E3E" stroke-width="1.2" stroke-dasharray="3,3" />
                <path d="M 435 91 L 435 130 L 339 135" fill="none" stroke="#E53E3E" stroke-width="1.2" stroke-dasharray="3,3" />
                <path d="M 555 91 L 555 140 L 339 140" fill="none" stroke="#E53E3E" stroke-width="1.2" stroke-dasharray="3,3" />
            </svg>
        </div>

        <!-- Lower Grid: 5-Tuple & Sequential Invariants -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 18px; margin-bottom: 3.5mm;">
            <div class="cream-card" style="border-left: 3px solid var(--wine-red);">
                <h3 style="font-family: 'Playfair Display', serif; font-size: 10.5pt; color: var(--wine-red); margin-bottom: 5px;">
                    Formal 5-Tuple Formulation
                </h3>
                <p style="font-size: 7.6pt; color: var(--text-dark-secondary); line-height: 1.5;">
                    &bull; <strong>State Set Q:</strong> {{ q₀, q₁, q₂, q₃, q₄, qE }}<br>
                    &bull; <strong>Alphabet &Sigma;:</strong> {{ LEVEL, IP, USER, STATUS, OTHER }}<br>
                    &bull; <strong>Initial State q₀:</strong> Unconsumed initial record state.<br>
                    &bull; <strong>Accept State F:</strong> {{ q₄ }} (Terminal valid authentication).<br>
                    &bull; <strong>Trap Sink qE:</strong> Absorbing non-recovering error sink.
                </p>
            </div>

            <div class="cream-card" style="border-left: 3px solid #2EA043;">
                <h3 style="font-family: 'Playfair Display', serif; font-size: 10.5pt; color: #22543D; margin-bottom: 5px;">
                    Grammar Invariant Guarantees
                </h3>
                <p style="font-size: 7.6pt; color: var(--text-dark-secondary); line-height: 1.5;">
                    The forward transition sequence models the canonical order of authentication server logs. Any syntactic disorder (e.g., missing IP, unquoted quotes in username) forces an immediate deterministic edge to <em>qE</em>, ensuring no malformed token reaches production stores.
                </p>
            </div>
        </div>

        <!-- Bottom State Semantic Summary Table -->
        <div class="luxury-table-container">
            <table class="luxury-table" style="font-size: 7.2pt;">
                <thead>
                    <tr>
                        <th>State</th>
                        <th>Syntactic Contract</th>
                        <th>Valid Next Token</th>
                        <th>Invalid Token Behavior</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td><strong>q₀</strong></td><td>Initial unread record buffer</td><td>LEVEL</td><td>Transitions immediately to qE (Reject)</td></tr>
                    <tr><td><strong>q₁</strong></td><td>Severity / Auth Level successfully parsed</td><td>IP</td><td>Transitions immediately to qE (Reject)</td></tr>
                    <tr><td><strong>q₂</strong></td><td>IPv4 / IPv6 network address verified</td><td>USER</td><td>Transitions immediately to qE (Reject)</td></tr>
                    <tr><td><strong>q₃</strong></td><td>Username string verified</td><td>STATUS</td><td>Transitions immediately to qE (Reject)</td></tr>
                    <tr><td><strong style="color:#2EA043;">q₄</strong></td><td>Status verified; Grammar valid</td><td>[EOL]</td><td>ACCEPT &bull; Fast-path store commit</td></tr>
                    <tr><td><strong style="color:#E53E3E;">qE</strong></td><td>Trap state; Absorbs all symbols</td><td>ANY</td><td>REJECT &bull; Escalate to Turing Sanitizer</td></tr>
                </tbody>
            </table>
        </div>

    </div>
    {btm_bar("DETERMINISTIC FINITE AUTOMATA", "SECTION 2.4 • TABLE 3 MINIMAL FORMULATION")}
</section>"""
with open(os.path.join(pages_dir, "page_9.html"), "w", encoding="utf-8") as f: f.write(p9)

# ==============================================================================
# PAGE 10: TOTAL TRANSITION MATRIX & MYHILL-NERODE PROOF (Dark Luxury Theme)
# ==============================================================================
p10 = f"""<section class="page theme-dark">
    {top_hdr("FORMAL MATHEMATICAL PROOFS", "TRANSITION MATRIX & MYHILL-NERODE THEOREM")}
    <div class="page-content" style="padding-top: 5mm; padding-bottom: 5mm; justify-content: space-between;">
        
        <div>
            <div class="gold-eyebrow">MATHEMATICAL RIGOR</div>
            <h1 class="canva-title" style="font-size: 26pt; margin-bottom: 3mm;">
                TOTAL TRANSITION MATRIX &amp; MINIMALITY PROOF
            </h1>
            <div class="gold-separator-line"></div>
        </div>

        <!-- Upper: Full 6x5 Transition Matrix Table (Table 3) -->
        <div class="luxury-table-container" style="margin-bottom: 3.5mm;">
            <div style="padding: 8px 12px; background: #261211; border-bottom: 1.5px solid var(--border-gold);">
                <span style="font-family: 'Cinzel'; font-size: 8pt; color: var(--gold-light); font-weight: bold;">
                    TABLE 3: TOTAL TRANSITION MATRIX &delta;(q, &sigma;) OVER ALPHABET &Sigma;
                </span>
            </div>
            <table class="luxury-table" style="font-size: 7.5pt;">
                <thead>
                    <tr>
                        <th>Current State (q)</th>
                        <th>LEVEL</th>
                        <th>IP</th>
                        <th>USER</th>
                        <th>STATUS</th>
                        <th>OTHER</th>
                        <th>Automaton Verdict</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td><strong>q₀ (Start)</strong></td><td>q₁</td><td>qE</td><td>qE</td><td>qE</td><td>qE</td><td style="color:#DFC4A8;">In-Progress</td></tr>
                    <tr><td><strong>q₁</strong></td><td>qE</td><td>q₂</td><td>qE</td><td>qE</td><td>qE</td><td style="color:#DFC4A8;">In-Progress</td></tr>
                    <tr><td><strong>q₂</strong></td><td>qE</td><td>qE</td><td>q₃</td><td>qE</td><td>qE</td><td style="color:#DFC4A8;">In-Progress</td></tr>
                    <tr><td><strong>q₃</strong></td><td>qE</td><td>qE</td><td>qE</td><td>q₄</td><td>qE</td><td style="color:#DFC4A8;">In-Progress</td></tr>
                    <tr style="background: rgba(46, 160, 67, 0.2);">
                        <td><strong style="color:#68D391;">q₄ (Accept)</strong></td>
                        <td>qE</td><td>qE</td><td>qE</td><td>qE</td><td>qE</td>
                        <td style="color:#2EA043; font-weight:bold;">ACCEPT (Fast-Path)</td>
                    </tr>
                    <tr style="background: rgba(128, 24, 24, 0.25);">
                        <td><strong style="color:#FF6B6B;">qE (Trap Sink)</strong></td>
                        <td>qE</td><td>qE</td><td>qE</td><td>qE</td><td>qE</td>
                        <td style="color:#E53E3E; font-weight:bold;">REJECT (Escalate)</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- Lower: Myhill-Nerode Minimality Proof Card -->
        <div class="dark-card" style="border-left: 3px solid var(--gold); padding: 12px 16px; margin-bottom: 3.5mm;">
            <h3 style="font-family: 'Playfair Display', serif; font-size: 11pt; color: var(--gold-light); margin-bottom: 6px;">
                Formal Proof of Minimality (Myhill-Nerode Equivalence Theorem)
            </h3>
            <p style="font-size: 7.8pt; color: var(--text-cream-dim); line-height: 1.55;">
                <strong>Theorem:</strong> The baseline automaton <em>M</em> has the minimal possible number of states for language <em>L</em><sub>baseline</sub>.<br>
                <strong>Proof:</strong> Under the Myhill-Nerode theorem, two states <em>p, q</em> are equivalent (<em>p &equiv; q</em>) iff for all strings <em>z &isin; &Sigma;*</em>, &delta;&#770;(<em>p, z</em>) &isin; F &hArr; &delta;&#770;(<em>q, z</em>) &isin; F. We evaluate distinguishing suffixes:<br><br>
                &bull; Suffix <em>z = &epsilon;</em> distinguishes <strong>q₄</strong> (since q₄ &isin; F) from {{ q₀, q₁, q₂, q₃, qE }} (since none &isin; F).<br>
                &bull; Suffix <em>z = STATUS</em> distinguishes <strong>q₃</strong> (leading to q₄ &isin; F) from {{ q₀, q₁, q₂, qE }} (leading to qE &notin; F).<br>
                &bull; Suffix <em>z = USER &bull; STATUS</em> distinguishes <strong>q₂</strong> from {{ q₀, q₁, qE }}.<br>
                &bull; Suffix <em>z = IP &bull; USER &bull; STATUS</em> distinguishes <strong>q₁</strong> from {{ q₀, qE }}.<br>
                &bull; Suffix <em>z = LEVEL &bull; IP &bull; USER &bull; STATUS</em> distinguishes <strong>q₀</strong> from <strong>qE</strong>.<br><br>
                Every state pair (<em>p, q</em>) is pairwise distinguishable. Therefore, no states can be merged, and the automaton is mathematically minimal with <strong>|Q| = 6</strong>. &squ;
            </p>
        </div>

        <div class="dark-card" style="background: #170A09; border: 1px solid var(--border-gold); padding: 8px 14px; text-align: center;">
            <span style="font-family: 'Cinzel'; font-size: 7.5pt; color: var(--gold-light); letter-spacing: 1.5px;">
                FORMALLY VERIFIED: MINIMAL STATE COUNT PREVENTS OVERFITTING AND GUARANTEES OPTIMAL CPU L1 INSTRUCTION CACHE LOCALITY
            </span>
        </div>

    </div>
    {btm_bar("FORMAL MINIMALITY PROOF", "MYHILL-NERODE EQUIVALENCE THEOREM • SECTION 2.5")}
</section>"""
with open(os.path.join(pages_dir, "page_10.html"), "w", encoding="utf-8") as f: f.write(p10)

print("[✓] Generated Pages 6, 7, 8, 9, 10 with full vertical layouts!")

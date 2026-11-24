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
    <div class="page-content" style="padding-top: 5mm; padding-bottom: 5mm; gap: 16px;">
        
        <div>
            <div class="gold-eyebrow" style="color: var(--wine-red);">THEORETICAL TAXONOMY</div>
            <h1 class="canva-title" style="color: var(--wine-red); font-size: 28pt; margin-bottom: 2mm;">
                FORMAL LANGUAGE THEORY &amp; CHOMSKY HIERARCHY
            </h1>
            <div class="gold-separator-line" style="background: linear-gradient(90deg, var(--wine-red), transparent);"></div>
        </div>

        <!-- Middle: SVG Diagram & Theoretical Framing -->
        <div style="display: grid; grid-template-columns: 1.15fr 1fr; gap: 20px; align-items: center;">
            <!-- Concentric Chomsky Venn Diagram -->
            <div class="cream-card" style="padding: 16px; border: 1.5px solid rgba(128, 24, 24, 0.25); text-align: center;">
                <span style="font-family: 'Cinzel', serif; font-size: 8.5pt; color: var(--wine-red); letter-spacing: 1.5px; text-transform: uppercase; font-weight: bold; display: block; margin-bottom: 8px;">
                    FIGURE 3: CONCENTRIC COMPUTATIONAL EXPRESSIVENESS
                </span>
                <svg viewBox="0 0 340 230" style="width: 100%; height: 200px; display: block;">
                    <!-- Type 0: Recursively Enumerable -->
                    <ellipse cx="170" cy="115" rx="160" ry="105" fill="rgba(128, 24, 24, 0.08)" stroke="#801818" stroke-width="2" />
                    <text x="170" y="28" text-anchor="middle" fill="#801818" font-family="Cinzel" font-size="9" font-weight="bold">TYPE 0: RECURSIVELY ENUMERABLE (TURING MACHINE / LLM)</text>

                    <!-- Type 1: Context Sensitive -->
                    <ellipse cx="170" cy="122" rx="128" ry="80" fill="rgba(183, 121, 31, 0.08)" stroke="#B7791F" stroke-width="1.8" />
                    <text x="170" y="58" text-anchor="middle" fill="#B7791F" font-family="Cinzel" font-size="8.5" font-weight="bold">TYPE 1: CONTEXT-SENSITIVE (LBA)</text>

                    <!-- Type 2: Context Free -->
                    <ellipse cx="170" cy="130" rx="95" ry="58" fill="rgba(49, 130, 206, 0.08)" stroke="#3182CE" stroke-width="1.8" />
                    <text x="170" y="88" text-anchor="middle" fill="#2B6CB0" font-family="Cinzel" font-size="8" font-weight="bold">TYPE 2: CONTEXT-FREE (PDA)</text>

                    <!-- Type 3: Regular Languages -->
                    <ellipse cx="170" cy="142" rx="64" ry="36" fill="rgba(56, 161, 105, 0.16)" stroke="#2EA043" stroke-width="2.2" />
                    <text x="170" y="138" text-anchor="middle" fill="#22543D" font-family="Cinzel" font-size="8.5" font-weight="bold">TYPE 3: REGULAR</text>
                    <text x="170" y="152" text-anchor="middle" fill="#22543D" font-family="JetBrains Mono" font-size="7">DFA &bull; Moore &bull; O(N)</text>
                </svg>
            </div>

            <!-- Conceptual Narrative Cards -->
            <div style="display: flex; flex-direction: column; gap: 12px;">
                <div class="cream-card" style="border-left: 4px solid #2EA043; padding: 16px 18px;">
                    <strong style="color: #2EA043; font-size: 9.5pt;">Type-3 Regular Subsystem (DFA &amp; Moore):</strong>
                    <p style="font-size: 8.5pt; color: var(--text-dark-secondary); line-height: 1.6; margin-top: 4px;">
                        Operates under finite internal states without external auxiliary memory. Validates sequential log syntax and counts failure bursts in strict O(N) linear time and O(1) space.
                    </p>
                </div>
                <div class="cream-card" style="border-left: 4px solid #801818; padding: 16px 18px;">
                    <strong style="color: var(--wine-red); font-size: 9.5pt;">Type-0 Turing Subsystem (TM &amp; LLM Oracle):</strong>
                    <p style="font-size: 8.5pt; color: var(--text-dark-secondary); line-height: 1.6; margin-top: 4px;">
                        Possesses an unbounded read/write tape. Performs in-place credential scrubbing and unconstrained semantic intent classification on complex attack vectors.
                    </p>
                </div>
            </div>
        </div>

        <!-- Bottom: Formal Chomsky Mapping Table -->
        <div class="luxury-table-container">
            <table class="luxury-table" style="font-size: 8.2pt;">
                <thead>
                    <tr>
                        <th style="padding:10px 14px;">Chomsky Level</th>
                        <th style="padding:10px 14px;">Grammar Type</th>
                        <th style="padding:10px 14px;">Abstract Machine</th>
                        <th style="padding:10px 14px;">Memory Model</th>
                        <th style="padding:10px 14px;">Engine Architectural Role</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td style="padding:9px 14px;"><strong>Type 3</strong></td>
                        <td style="padding:9px 14px;">Regular Grammar</td>
                        <td style="padding:9px 14px;">Deterministic Finite Automaton (DFA)</td>
                        <td style="padding:9px 14px;">Finite state register (Q)</td>
                        <td style="padding:9px 14px;">Line-rate syntactic token validation (1.8 &mu;s fast path)</td>
                    </tr>
                    <tr>
                        <td style="padding:9px 14px;"><strong>Type 3+</strong></td>
                        <td style="padding:9px 14px;">Finite State Transducer</td>
                        <td style="padding:9px 14px;">Moore Sequential Machine</td>
                        <td style="padding:9px 14px;">Per-IP session state mapping</td>
                        <td style="padding:9px 14px;">Stateful brute-force tracking &amp; threshold attack flagging</td>
                    </tr>
                    <tr>
                        <td style="padding:9px 14px;"><strong>Type 2</strong></td>
                        <td style="padding:9px 14px;">Context-Free Grammar</td>
                        <td style="padding:9px 14px;">Pushdown Automaton (PDA)</td>
                        <td style="padding:9px 14px;">Last-In, First-Out (LIFO) Stack</td>
                        <td style="padding:9px 14px;">Nested JSON / RPC payload parsing (Phase 2 roadmap)</td>
                    </tr>
                    <tr>
                        <td style="padding:9px 14px;"><strong>Type 0</strong></td>
                        <td style="padding:9px 14px;">Unrestricted Grammar</td>
                        <td style="padding:9px 14px;">Turing Machine / Transformer LLM</td>
                        <td style="padding:9px 14px;">Unbounded Read/Write Tape</td>
                        <td style="padding:9px 14px;">Deterministic tape secret masking &amp; semantic reasoning</td>
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
    <div class="page-content" style="padding-top: 5mm; padding-bottom: 5mm; gap: 16px;">
        
        <div>
            <div class="gold-eyebrow">SYSTEM BLUEPRINT</div>
            <h1 class="canva-title" style="font-size: 28pt; margin-bottom: 2mm;">
                DUAL-LANE ENGINE BLUEPRINT
            </h1>
            <div class="gold-separator-line"></div>
        </div>

        <!-- Upper: Full-Width End-to-End Pipeline SVG (Taller & Larger) -->
        <div class="dark-card" style="padding: 16px 18px; background: #231211;">
            <div style="text-align: center; margin-bottom: 8px;">
                <span style="font-family: 'Cinzel', serif; font-size: 8.5pt; letter-spacing: 2px; color: var(--gold); text-transform: uppercase;">
                    FIGURE 4: UNIFIED HYBRID AUTOMATA &amp; NEURAL ESCALATION TOPOLOGY
                </span>
            </div>
            <svg viewBox="0 0 680 190" style="width: 100%; height: 175px; display: block;">
                <!-- Node 1: Raw Log -->
                <rect x="10" y="70" width="85" height="50" rx="5" fill="#1C0C0B" stroke="#8F7255" stroke-width="1.8" />
                <text x="52" y="91" text-anchor="middle" fill="#DFC4A8" font-family="Cinzel" font-size="8.5" font-weight="bold">RAW LOG</text>
                <text x="52" y="106" text-anchor="middle" fill="#9E8C82" font-size="7.5">100k+ eps</text>

                <!-- Arrow 1 -> 2 -->
                <line x1="95" y1="95" x2="120" y2="95" stroke="#C59F7A" stroke-width="2" />

                <!-- Node 2: Lexer -->
                <rect x="120" y="70" width="100" height="50" rx="5" fill="#1C0C0B" stroke="#8F7255" stroke-width="1.8" />
                <text x="170" y="91" text-anchor="middle" fill="#DFC4A8" font-family="Cinzel" font-size="8.5" font-weight="bold">POSIX LEXER</text>
                <text x="170" y="106" text-anchor="middle" fill="#68D391" font-family="JetBrains Mono" font-size="7">5 Token Types</text>

                <!-- Arrow 2 -> 3 -->
                <line x1="220" y1="95" x2="245" y2="95" stroke="#C59F7A" stroke-width="2" />

                <!-- Node 3: DFA Engine -->
                <rect x="245" y="60" width="115" height="70" rx="6" fill="#801818" stroke="#C59F7A" stroke-width="2.2" />
                <text x="302" y="83" text-anchor="middle" fill="#FFF" font-family="Cinzel" font-size="9" font-weight="bold">DFA ENGINE</text>
                <text x="302" y="98" text-anchor="middle" fill="#DFC4A8" font-size="7.5">Table 3 Matrix</text>
                <text x="302" y="113" text-anchor="middle" fill="#68D391" font-family="JetBrains Mono" font-size="7.5" font-weight="bold">q0..q4 / qE</text>

                <!-- Accept Path: Upwards to Moore -->
                <path d="M 360 80 L 395 80 L 395 42 L 420 42" fill="none" stroke="#38A169" stroke-width="2" />
                <text x="395" y="64" text-anchor="middle" fill="#68D391" font-family="JetBrains Mono" font-size="7" font-weight="bold">ACCEPT</text>

                <!-- Node 4: Moore Machine -->
                <rect x="420" y="20" width="115" height="46" rx="5" fill="#1C0C0B" stroke="#38A169" stroke-width="1.8" />
                <text x="477" y="40" text-anchor="middle" fill="#68D391" font-family="Cinzel" font-size="8.5" font-weight="bold">MOORE FSM</text>
                <text x="477" y="54" text-anchor="middle" fill="#9E8C82" font-size="7">m0..m3 Per-IP</text>

                <!-- Moore OK -> Local Store -->
                <line x1="535" y1="43" x2="575" y2="43" stroke="#38A169" stroke-width="2" />
                <rect x="575" y="20" width="95" height="46" rx="5" fill="#152418" stroke="#38A169" stroke-width="1.8" />
                <text x="622" y="40" text-anchor="middle" fill="#68D391" font-family="Cinzel" font-size="8.5" font-weight="bold">LOCAL STORE</text>
                <text x="622" y="54" text-anchor="middle" fill="#A0AEC0" font-size="7">1.8 &mu;s &bull; $0.00 Cost</text>

                <!-- Reject & Flag Paths to Turing Sanitizer -->
                <path d="M 360 110 L 415 110 L 415 145 L 435 145" fill="none" stroke="#E53E3E" stroke-width="2" />
                <text x="395" y="122" text-anchor="middle" fill="#FEB2B2" font-family="JetBrains Mono" font-size="7" font-weight="bold">REJECT (qE)</text>

                <path d="M 477 66 L 477 120" fill="none" stroke="#E53E3E" stroke-width="2" />
                <text x="492" y="96" text-anchor="middle" fill="#FEB2B2" font-family="JetBrains Mono" font-size="7" font-weight="bold">FLAG</text>

                <!-- Node 5: Turing Sanitizer -->
                <rect x="435" y="120" width="125" height="50" rx="5" fill="#421212" stroke="#E53E3E" stroke-width="2" />
                <text x="497" y="141" text-anchor="middle" fill="#FFF" font-family="Cinzel" font-size="8.5" font-weight="bold">7-TUPLE TM SANITIZER</text>
                <text x="497" y="156" text-anchor="middle" fill="#FFBABA" font-size="7">Overwrites Secrets with 'X'</text>

                <!-- Arrow to Neural Escalation -->
                <line x1="560" y1="145" x2="585" y2="145" stroke="#E53E3E" stroke-width="2" />

                <!-- Node 6: Neural LLM -->
                <rect x="585" y="120" width="85" height="50" rx="5" fill="#1C0C0B" stroke="#E53E3E" stroke-width="1.8" />
                <text x="627" y="141" text-anchor="middle" fill="#FF6B6B" font-family="Cinzel" font-size="8.5" font-weight="bold">LLM API</text>
                <text x="627" y="156" text-anchor="middle" fill="#DFC4A8" font-size="7">Queue K=1k</text>
            </svg>
        </div>

        <!-- Middle: Two Deep Architectural Guarantee Cards -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
            <div class="dark-card" style="border-left: 4px solid #2EA043; padding: 18px 20px;">
                <h3 style="font-family: 'Playfair Display', serif; font-size: 13pt; color: #68D391; margin-bottom: 8px;">
                    Symbolic Fast-Path Guarantees
                </h3>
                <p style="font-size: 8.8pt; color: var(--text-cream-dim); line-height: 1.62;">
                    &bull; <strong>Strict Deterministic Time:</strong> Operates at O(N) where N is token stream length. Zero state backtracking eliminates ReDoS exploits.<br>
                    &bull; <strong>Zero Dynamic Allocations:</strong> Evaluates logs using lightweight string views and contiguous transition table offsets.<br>
                    &bull; <strong>Temporal Session Tracking:</strong> Moore machine tracks per-IP authentication failures in an O(1) hash map without cross-IP contention.
                </p>
            </div>

            <div class="dark-card" style="border-left: 4px solid var(--wine-red); padding: 18px 20px;">
                <h3 style="font-family: 'Playfair Display', serif; font-size: 13pt; color: #FF6B6B; margin-bottom: 8px;">
                    Neural Slow-Path Controls
                </h3>
                <p style="font-size: 8.8pt; color: var(--text-cream-dim); line-height: 1.62;">
                    &bull; <strong>Deterministic PII Redaction:</strong> Turing machine tape head masks plaintext passwords and auth tokens prior to network egress.<br>
                    &bull; <strong>Bounded Buffer Queue (K=1,000):</strong> Protects system memory from exhaustion during distributed denial-of-service spikes.<br>
                    &bull; <strong>Asynchronous Non-Blocking I/O:</strong> libcurl multi-socket transfers prevent worker thread blocking while querying LLM APIs.
                </p>
            </div>
        </div>

        <!-- Bottom: Architectural Invariant Banner -->
        <div class="dark-card" style="background: #170A09; border: 1px solid var(--border-gold); padding: 12px 16px; text-align: center;">
            <span style="font-family: 'Cinzel'; font-size: 8.5pt; color: var(--gold-light); letter-spacing: 1.5px;">
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
    <div class="page-content" style="padding-top: 5mm; padding-bottom: 5mm; gap: 16px;">
        
        <div>
            <div class="gold-eyebrow">FRONT-END TOKENIZATION</div>
            <h1 class="canva-title" style="font-size: 28pt; margin-bottom: 2mm;">
                THE SYMBOLIC LEXER: ATOMIC TOKENIZATION
            </h1>
            <div class="gold-separator-line"></div>
        </div>

        <!-- Middle: Token Taxonomy & Grammar Specification -->
        <div style="display: grid; grid-template-columns: 1.15fr 1fr; gap: 20px; align-items: start;">
            <div class="dark-card" style="border-left: 4px solid var(--gold); padding: 16px 20px;">
                <h3 style="font-family: 'Playfair Display', serif; font-size: 13pt; color: var(--gold-light); margin-bottom: 8px;">
                    Deterministic Token Grammar &Sigma;
                </h3>
                <p style="font-size: 8.8pt; color: var(--text-cream-dim); line-height: 1.6; margin-bottom: 8px;">
                    The lexical analyzer translates unstructured ASCII character streams into discrete formal tokens conforming to alphabet <strong>&Sigma; = {{ LEVEL, IP, USER, STATUS, OTHER }}</strong>:
                </p>
                <div style="display: flex; flex-direction: column; gap: 6px; font-size: 8.2pt; font-family: 'JetBrains Mono', monospace;">
                    <div><span class="token-badge token-level">LEVEL</span> <code>^(Accepted|Failed|Invalid|error|FATAL)</code></div>
                    <div><span class="token-badge token-ip">IP</span> <code>^([0-9]{{1,3}}\\.){{3}}[0-9]{{1,3}}</code></div>
                    <div><span class="token-badge token-user">USER</span> <code>^[a-zA-Z0-9_\\-\\.]{{1,32}}</code></div>
                    <div><span class="token-badge token-status">STATUS</span> <code>^(port\\s+[0-9]+|ssh2|publickey|password)</code></div>
                    <div><span class="token-badge token-other">OTHER</span> <code>[^\\s]+</code> <span style="color:#FF6B6B;">(Injection Catchall)</span></div>
                </div>
            </div>

            <div class="dark-card" style="border-left: 4px solid var(--wine-red); padding: 16px 20px;">
                <h3 style="font-family: 'Playfair Display', serif; font-size: 13pt; color: var(--gold-light); margin-bottom: 8px;">
                    ReDoS Immunity Guarantee
                </h3>
                <p style="font-size: 8.8pt; color: var(--text-cream-dim); line-height: 1.62;">
                    Vulnerable regex implementations rely on recursive backtracking engines. If an attacker injects nested repetitions, processing time scales exponentially: O(2<sup>N</sup>). Our lexer constructs deterministic linear passes without lookahead or backtracking, mathematically bounding execution time to <strong>O(N)</strong>.
                </p>
            </div>
        </div>

        <!-- Token Decomposition Trace Table -->
        <div class="luxury-table-container">
            <table class="luxury-table" style="font-size: 8.2pt;">
                <thead>
                    <tr>
                        <th style="padding:10px 14px;">Raw Telemetry Log Record</th>
                        <th style="padding:10px 14px;">Extracted Token Sequence</th>
                        <th style="padding:10px 14px;">DFA Final State</th>
                        <th style="padding:10px 14px;">Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td style="padding:9px 14px;"><code>Accepted password for root from 192.168.1.100 port 22</code></td>
                        <td style="padding:9px 14px;">LEVEL &bull; USER &bull; IP &bull; STATUS</td>
                        <td style="padding:9px 14px; color:#2EA043; font-weight:bold;">q4 (ACCEPT)</td>
                        <td style="padding:9px 14px; color:#2EA043;">Fast-Path Store ($0)</td>
                    </tr>
                    <tr>
                        <td style="padding:9px 14px;"><code>Failed password for root' OR '1'='1-- from 10.0.0.99</code></td>
                        <td style="padding:9px 14px;">LEVEL &bull; USER &bull; <strong style="color:#FF6B6B;">OTHER</strong></td>
                        <td style="padding:9px 14px; color:#E53E3E; font-weight:bold;">qE (TRAP)</td>
                        <td style="padding:9px 14px; color:#FF6B6B;">TM Mask &bull; Escalate</td>
                    </tr>
                    <tr>
                        <td style="padding:9px 14px;"><code>Invalid user admin from 172.16.0.4 port 44122 ssh2</code></td>
                        <td style="padding:9px 14px;">LEVEL &bull; USER &bull; IP &bull; STATUS</td>
                        <td style="padding:9px 14px; color:#2EA043; font-weight:bold;">q4 (ACCEPT)</td>
                        <td style="padding:9px 14px; color:#2EA043;">Moore Track &bull; Store</td>
                    </tr>
                    <tr>
                        <td style="padding:9px 14px;"><code>User admin pass=SecretPass123! token=LIVE_KEY_99</code></td>
                        <td style="padding:9px 14px;">USER &bull; <strong style="color:#FF6B6B;">OTHER &bull; OTHER</strong></td>
                        <td style="padding:9px 14px; color:#E53E3E; font-weight:bold;">qE (TRAP)</td>
                        <td style="padding:9px 14px; color:#FF6B6B;">Scrub Secrets &bull; Alert</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="dark-card" style="background: #170A09; border: 1px solid var(--border-gold); padding: 12px 16px; text-align: center;">
            <span style="font-family: 'Cinzel'; font-size: 8.2pt; color: var(--gold-light); letter-spacing: 1.5px;">
                THE UNQUOTED SQL QUOTE REPRESENTS AN UNEXPECTED ALPHABET SYMBOL, FORCING IMMEDIATE TRAP SINK ESCALATION
            </span>
        </div>

    </div>
    {btm_bar("LEXICAL TOKENIZATION ENGINE", "SECTION 2.3 • TOKEN GRAMMAR & REDOS IMMUNITY")}
</section>"""
with open(os.path.join(pages_dir, "page_8.html"), "w", encoding="utf-8") as f: f.write(p8)

# ==============================================================================
# PAGE 9: MINIMAL BASELINE DFA (Cream Luxury Theme)
# ==============================================================================
p9 = f"""<section class="page theme-cream">
    {top_hdr("AUTOMATA DESIGN", "MINIMAL BASELINE DFA (TABLE 3 FORMULATION)")}
    <div class="page-content" style="padding-top: 5mm; padding-bottom: 5mm; gap: 16px;">
        
        <div>
            <div class="gold-eyebrow" style="color: var(--wine-red);">DETERMINISTIC FINITE AUTOMATON</div>
            <div style="background: var(--wine-red); border-radius: 8px; padding: 12px 20px; margin-bottom: 2mm; box-shadow: 0 4px 15px rgba(128, 24, 24, 0.2);">
                <h1 class="canva-title" style="color: #FFFFFF; font-size: 26pt; margin-bottom: 2px;">
                    THE MINIMAL BASELINE DFA
                </h1>
                <p style="font-size: 8.5pt; color: var(--gold-light); font-family: 'Cinzel', serif; letter-spacing: 1.5px; text-transform: uppercase;">
                    MATHEMATICAL 5-TUPLE FORMULATION AND STATE TRANSITION GRAPH
                </p>
            </div>
        </div>

        <!-- Large State Transition SVG Diagram -->
        <div class="cream-card" style="padding: 16px; border: 1.5px solid rgba(128, 24, 24, 0.3); background: #FFFFFF;">
            <div style="text-align: center; margin-bottom: 8px;">
                <span style="font-family: 'Cinzel', serif; font-size: 8.5pt; letter-spacing: 2px; color: var(--wine-red); text-transform: uppercase; font-weight: bold;">
                    FIGURE 5: 6-STATE MINIMAL RECOGNIZER TOPOLOGY
                </span>
            </div>

            <svg viewBox="0 0 680 180" style="width: 100%; height: 165px; display: block;">
                <!-- Start Arrow -->
                <line x1="15" y1="65" x2="45" y2="65" stroke="#1E0F0E" stroke-width="2.2" />
                <text x="30" y="55" text-anchor="middle" font-family="Plus Jakarta Sans" font-size="8" font-weight="bold">start</text>

                <!-- State q0 -->
                <circle cx="75" cy="65" r="28" fill="#FFF" stroke="#801818" stroke-width="2.5" />
                <text x="75" y="72" text-anchor="middle" fill="#801818" font-family="Playfair Display" font-size="14" font-weight="bold">q₀</text>

                <!-- Transition q0 -> q1 -->
                <line x1="103" y1="65" x2="167" y2="65" stroke="#801818" stroke-width="2.2" />
                <text x="135" y="55" text-anchor="middle" fill="#801818" font-size="8" font-weight="bold">LEVEL</text>

                <!-- State q1 -->
                <circle cx="195" cy="65" r="28" fill="#FFF" stroke="#801818" stroke-width="2.5" />
                <text x="195" y="72" text-anchor="middle" fill="#801818" font-family="Playfair Display" font-size="14" font-weight="bold">q₁</text>

                <!-- Transition q1 -> q2 -->
                <line x1="223" y1="65" x2="287" y2="65" stroke="#801818" stroke-width="2.2" />
                <text x="255" y="55" text-anchor="middle" fill="#801818" font-size="8" font-weight="bold">IP</text>

                <!-- State q2 -->
                <circle cx="315" cy="65" r="28" fill="#FFF" stroke="#801818" stroke-width="2.5" />
                <text x="315" y="72" text-anchor="middle" fill="#801818" font-family="Playfair Display" font-size="14" font-weight="bold">q₂</text>

                <!-- Transition q2 -> q3 -->
                <line x1="343" y1="65" x2="407" y2="65" stroke="#801818" stroke-width="2.2" />
                <text x="375" y="55" text-anchor="middle" fill="#801818" font-size="8" font-weight="bold">USER</text>

                <!-- State q3 -->
                <circle cx="435" cy="65" r="28" fill="#FFF" stroke="#801818" stroke-width="2.5" />
                <text x="435" y="72" text-anchor="middle" fill="#801818" font-family="Playfair Display" font-size="14" font-weight="bold">q₃</text>

                <!-- Transition q3 -> q4 -->
                <line x1="463" y1="65" x2="527" y2="65" stroke="#2EA043" stroke-width="2.5" />
                <text x="495" y="55" text-anchor="middle" fill="#2EA043" font-size="8" font-weight="bold">STATUS</text>

                <!-- Accept State q4 (Double Circle) -->
                <circle cx="555" cy="65" r="28" fill="#F0FFF4" stroke="#2EA043" stroke-width="2.5" />
                <circle cx="555" cy="65" r="22" fill="#F0FFF4" stroke="#2EA043" stroke-width="1.8" />
                <text x="555" y="72" text-anchor="middle" fill="#2EA043" font-family="Playfair Display" font-size="14" font-weight="bold">q₄</text>
                <text x="555" y="108" text-anchor="middle" fill="#2EA043" font-size="8" font-weight="bold">ACCEPT</text>

                <!-- Trap State qE -->
                <circle cx="315" cy="140" r="26" fill="#FFF5F5" stroke="#E53E3E" stroke-width="2" stroke-dasharray="4,3" />
                <text x="315" y="146" text-anchor="middle" fill="#E53E3E" font-family="Playfair Display" font-size="13" font-weight="bold">qE</text>
                <text x="315" y="174" text-anchor="middle" fill="#E53E3E" font-size="7.5" font-weight="bold">TRAP (REJECT)</text>

                <!-- Trap transitions -->
                <path d="M 75 93 L 75 140 L 289 140" fill="none" stroke="#E53E3E" stroke-width="1.4" stroke-dasharray="3,3" />
                <path d="M 195 93 L 195 130 L 289 135" fill="none" stroke="#E53E3E" stroke-width="1.4" stroke-dasharray="3,3" />
                <path d="M 435 93 L 435 130 L 341 135" fill="none" stroke="#E53E3E" stroke-width="1.4" stroke-dasharray="3,3" />
                <path d="M 555 93 L 555 140 L 341 140" fill="none" stroke="#E53E3E" stroke-width="1.4" stroke-dasharray="3,3" />
            </svg>
        </div>

        <!-- Lower Grid: 5-Tuple & Sequential Invariants -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
            <div class="cream-card" style="border-left: 4px solid var(--wine-red); padding: 16px 18px;">
                <h3 style="font-family: 'Playfair Display', serif; font-size: 11.5pt; color: var(--wine-red); margin-bottom: 6px;">
                    Formal 5-Tuple Formulation
                </h3>
                <p style="font-size: 8.5pt; color: var(--text-dark-secondary); line-height: 1.6;">
                    &bull; <strong>State Set Q:</strong> {{ q₀, q₁, q₂, q₃, q₄, qE }}<br>
                    &bull; <strong>Alphabet &Sigma;:</strong> {{ LEVEL, IP, USER, STATUS, OTHER }}<br>
                    &bull; <strong>Initial State q₀:</strong> Unconsumed initial record state.<br>
                    &bull; <strong>Accept State F:</strong> {{ q₄ }} (Terminal valid authentication).<br>
                    &bull; <strong>Trap Sink qE:</strong> Absorbing non-recovering error sink.
                </p>
            </div>

            <div class="cream-card" style="border-left: 4px solid #2EA043; padding: 16px 18px;">
                <h3 style="font-family: 'Playfair Display', serif; font-size: 11.5pt; color: #22543D; margin-bottom: 6px;">
                    Grammar Invariant Guarantees
                </h3>
                <p style="font-size: 8.5pt; color: var(--text-dark-secondary); line-height: 1.6;">
                    The forward transition sequence models the canonical order of authentication server logs. Any syntactic disorder (e.g., missing IP, unquoted quotes in username) forces an immediate deterministic edge to <em>qE</em>, ensuring no malformed token reaches production stores.
                </p>
            </div>
        </div>

        <!-- Bottom State Semantic Summary Table -->
        <div class="luxury-table-container">
            <table class="luxury-table" style="font-size: 8pt;">
                <thead>
                    <tr>
                        <th style="padding:9px 12px;">State</th>
                        <th style="padding:9px 12px;">Syntactic Contract</th>
                        <th style="padding:9px 12px;">Valid Next Token</th>
                        <th style="padding:9px 12px;">Invalid Token Behavior</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td style="padding:8px 12px;"><strong>q₀</strong></td><td style="padding:8px 12px;">Initial unread record buffer</td><td style="padding:8px 12px;">LEVEL</td><td style="padding:8px 12px;">Transitions immediately to qE (Reject)</td></tr>
                    <tr><td style="padding:8px 12px;"><strong>q₁</strong></td><td style="padding:8px 12px;">Severity / Auth Level successfully parsed</td><td style="padding:8px 12px;">IP</td><td style="padding:8px 12px;">Transitions immediately to qE (Reject)</td></tr>
                    <tr><td style="padding:8px 12px;"><strong>q₂</strong></td><td style="padding:8px 12px;">IPv4 / IPv6 network address verified</td><td style="padding:8px 12px;">USER</td><td style="padding:8px 12px;">Transitions immediately to qE (Reject)</td></tr>
                    <tr><td style="padding:8px 12px;"><strong>q₃</strong></td><td style="padding:8px 12px;">Username string verified</td><td style="padding:8px 12px;">STATUS</td><td style="padding:8px 12px;">Transitions immediately to qE (Reject)</td></tr>
                    <tr><td style="padding:8px 12px;"><strong style="color:#2EA043;">q₄</strong></td><td style="padding:8px 12px;">Status verified; Grammar valid</td><td style="padding:8px 12px;">[EOL]</td><td style="padding:8px 12px;">ACCEPT &bull; Fast-path store commit</td></tr>
                    <tr><td style="padding:8px 12px;"><strong style="color:#E53E3E;">qE</strong></td><td style="padding:8px 12px;">Trap state; Absorbs all symbols</td><td style="padding:8px 12px;">ANY</td><td style="padding:8px 12px;">REJECT &bull; Escalate to Turing Sanitizer</td></tr>
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
    <div class="page-content" style="padding-top: 5mm; padding-bottom: 5mm; gap: 16px;">
        
        <div>
            <div class="gold-eyebrow">MATHEMATICAL RIGOR</div>
            <h1 class="canva-title" style="font-size: 28pt; margin-bottom: 2mm;">
                TOTAL TRANSITION MATRIX &amp; MINIMALITY PROOF
            </h1>
            <div class="gold-separator-line"></div>
        </div>

        <!-- Upper: Full 6x5 Transition Matrix Table (Table 3) -->
        <div class="luxury-table-container">
            <div style="padding: 10px 14px; background: #261211; border-bottom: 1.5px solid var(--border-gold);">
                <span style="font-family: 'Cinzel'; font-size: 8.5pt; color: var(--gold-light); font-weight: bold;">
                    TABLE 3: TOTAL TRANSITION MATRIX &delta;(q, &sigma;) OVER ALPHABET &Sigma;
                </span>
            </div>
            <table class="luxury-table" style="font-size: 8.2pt;">
                <thead>
                    <tr>
                        <th style="padding:10px 14px;">Current State (q)</th>
                        <th style="padding:10px 14px;">LEVEL</th>
                        <th style="padding:10px 14px;">IP</th>
                        <th style="padding:10px 14px;">USER</th>
                        <th style="padding:10px 14px;">STATUS</th>
                        <th style="padding:10px 14px;">OTHER</th>
                        <th style="padding:10px 14px;">Automaton Verdict</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td style="padding:9px 14px;"><strong>q₀ (Start)</strong></td><td style="padding:9px 14px;">q₁</td><td style="padding:9px 14px;">qE</td><td style="padding:9px 14px;">qE</td><td style="padding:9px 14px;">qE</td><td style="padding:9px 14px;">qE</td><td style="padding:9px 14px; color:#DFC4A8;">In-Progress</td></tr>
                    <tr><td style="padding:9px 14px;"><strong>q₁</strong></td><td style="padding:9px 14px;">qE</td><td style="padding:9px 14px;">q₂</td><td style="padding:9px 14px;">qE</td><td style="padding:9px 14px;">qE</td><td style="padding:9px 14px;">qE</td><td style="padding:9px 14px; color:#DFC4A8;">In-Progress</td></tr>
                    <tr><td style="padding:9px 14px;"><strong>q₂</strong></td><td style="padding:9px 14px;">qE</td><td style="padding:9px 14px;">qE</td><td style="padding:9px 14px;">q₃</td><td style="padding:9px 14px;">qE</td><td style="padding:9px 14px;">qE</td><td style="padding:9px 14px; color:#DFC4A8;">In-Progress</td></tr>
                    <tr><td style="padding:9px 14px;"><strong>q₃</strong></td><td style="padding:9px 14px;">qE</td><td style="padding:9px 14px;">qE</td><td style="padding:9px 14px;">qE</td><td style="padding:9px 14px;">q₄</td><td style="padding:9px 14px;">qE</td><td style="padding:9px 14px; color:#DFC4A8;">In-Progress</td></tr>
                    <tr style="background: rgba(46, 160, 67, 0.2);">
                        <td style="padding:9px 14px;"><strong style="color:#68D391;">q₄ (Accept)</strong></td>
                        <td style="padding:9px 14px;">qE</td><td style="padding:9px 14px;">qE</td><td style="padding:9px 14px;">qE</td><td style="padding:9px 14px;">qE</td><td style="padding:9px 14px;">qE</td>
                        <td style="padding:9px 14px; color:#2EA043; font-weight:bold;">ACCEPT (Fast-Path)</td>
                    </tr>
                    <tr style="background: rgba(128, 24, 24, 0.25);">
                        <td style="padding:9px 14px;"><strong style="color:#FF6B6B;">qE (Trap Sink)</strong></td>
                        <td style="padding:9px 14px;">qE</td><td style="padding:9px 14px;">qE</td><td style="padding:9px 14px;">qE</td><td style="padding:9px 14px;">qE</td><td style="padding:9px 14px;">qE</td>
                        <td style="padding:9px 14px; color:#E53E3E; font-weight:bold;">REJECT (Escalate)</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- Lower: Myhill-Nerode Minimality Proof Card -->
        <div class="dark-card" style="border-left: 4px solid var(--gold); padding: 18px 22px;">
            <h3 style="font-family: 'Playfair Display', serif; font-size: 13pt; color: var(--gold-light); margin-bottom: 8px;">
                Formal Proof of Minimality (Myhill-Nerode Equivalence Theorem)
            </h3>
            <p style="font-size: 8.8pt; color: var(--text-cream-dim); line-height: 1.62;">
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

        <div class="dark-card" style="background: #170A09; border: 1px solid var(--border-gold); padding: 12px 16px; text-align: center;">
            <span style="font-family: 'Cinzel'; font-size: 8.2pt; color: var(--gold-light); letter-spacing: 1.5px;">
                FORMALLY VERIFIED: MINIMAL STATE COUNT PREVENTS OVERFITTING AND GUARANTEES OPTIMAL CPU L1 INSTRUCTION CACHE LOCALITY
            </span>
        </div>

    </div>
    {btm_bar("FORMAL MINIMALITY PROOF", "MYHILL-NERODE EQUIVALENCE THEOREM • SECTION 2.5")}
</section>"""
with open(os.path.join(pages_dir, "page_10.html"), "w", encoding="utf-8") as f: f.write(p10)

print("[✓] Pages 6 to 10 rewritten with large fonts and zero blank gaps.")

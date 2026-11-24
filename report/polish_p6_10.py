import os

pages_dir = r"C:\Users\Ritesh Kumar Agarwal\.gemini\antigravity\scratch\hybrid-anomaly-engine\report\pages"

p6 = """<section class="page">
    <div class="running-header">
        <div class="header-left">
            <span class="header-badge">FORMAL FOUNDATIONS</span>
            <span class="header-title">CHOMSKY HIERARCHY & AUTOMATA THEORY</span>
        </div>
        <div class="header-right">JIIT NOIDA • DEPT OF CSE</div>
    </div>
    <div>
        <h1 class="section-title">Theoretical Foundations</h1>
        <h2 class="section-subtitle">Formal Language Classification Across the Chomsky Hierarchy</h2>

        <p class="body-lead">
            The Chomsky Hierarchy categorizes formal grammars into four nested classes based on generative power. Selecting the correct automaton class is fundamental to building an optimal, non-backtracking triage engine.
        </p>

        <!-- SVG 3: Chomsky Hierarchy Layered Security Diagram -->
        <div class="diagram-canvas" style="padding: 10px;">
            <svg width="610" height="155" viewBox="0 0 610 155" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="15" y="10" width="580" height="135" rx="6" fill="#F3ECE1" stroke="#38231E" stroke-width="1.8"/>
                <text x="30" y="28" fill="#38231E" font-family="'Plus Jakarta Sans', sans-serif" font-size="8.5" font-weight="bold">TYPE 0: RECURSIVELY ENUMERABLE (Turing Machines) • Arbitrary Unrestricted Computation</text>

                <rect x="35" y="38" width="540" height="95" rx="6" fill="#FAF5EE" stroke="#6A1A24" stroke-width="1.8"/>
                <text x="50" y="54" fill="#6A1A24" font-family="'Plus Jakarta Sans', sans-serif" font-size="8.5" font-weight="bold">TYPE 1 / 2: CONTEXT-FREE LANGUAGES (Pushdown Automata) • Nested Syntax, Balanced Structures</text>

                <rect x="55" y="66" width="500" height="58" rx="6" fill="#FFFFFF" stroke="#9A4333" stroke-width="1.8"/>
                <text x="70" y="82" fill="#9A4333" font-family="'Plus Jakarta Sans', sans-serif" font-size="8.5" font-weight="bold">TYPE 3: REGULAR LANGUAGES (Finite State Automata / DFA) • Linear Scan 𝒪(N)</text>

                <!-- Mapping to Cyber Payloads -->
                <rect x="70" y="92" width="470" height="22" rx="3" fill="#FAF5EE" stroke="#E2D7C8"/>
                <text x="305" y="106" fill="#2A1715" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">Normal SSH Logs: [INFO] IP USER STATUS ──► Strictly Recognized by Minimal DFA</text>
            </svg>
        </div>

        <div class="grid-2" style="margin-top: 10px;">
            <div class="card-box">
                <h3 class="card-title">Mathematical Formulation of Log Grammar</h3>
                <p class="body-text">
                    Let <strong>Σ</strong> denote the formal alphabet of abstract token classes:
                    <br><code class="code-cell" style="font-size:8pt;">Σ = { LEVEL, IP, USER, STATUS, OTHER }</code>
                </p>
                <p class="body-text">
                    A healthy login event string <em>w</em> ∈ Σ* belongs to the regular language <em>L</em><sub>baseline</sub> if and only if it strictly follows the production rule:
                    <br><code class="code-cell" style="font-size:8pt;">S → LEVEL · IP · USER · STATUS</code>
                </p>
                <p class="body-text">
                    Because <em>L</em><sub>baseline</sub> is a regular language, it satisfies the Myhill-Nerode equivalence relation with a finite index of exactly 6 equivalence classes.
                </p>
            </div>
            <div class="card-box">
                <h3 class="card-title">The Boundary of Computation</h3>
                <p class="body-text">
                    While linear structures belong to Type 3, complex injection payloads (such as nested JSON queries or recursive SQL injections with matched parentheses <code>((1))</code>) belong to Type 2 (Context-Free) or Type 0 (Unrestricted).
                </p>
                <p class="body-text">
                    By designing a DFA to recognize normal Type 3 behavior, any syntax deviation (such as injected symbols or invalid token counts) immediately drives the automaton into an irreversible <strong>Trap State (q<sub>E</sub>)</strong>, signaling a structural anomaly.
                </p>
            </div>
        </div>
    </div>
    <div class="running-footer">
        <div class="footer-logo">HYBRID DFA–LLM ANOMALY ENGINE</div>
        <div>Theory of Computation (24B11CS212) • Final Technical Report</div>
        <div class="page-number-box">Page <span class="page-num">6</span> of 20</div>
    </div>
</section>"""

p8 = """<section class="page">
    <div class="running-header">
        <div class="header-left">
            <span class="header-badge">SYMBOLIC ENGINE</span>
            <span class="header-title">LEXER & LEXICAL TOKENIZER</span>
        </div>
        <div class="header-right">JIIT NOIDA • DEPT OF CSE</div>
    </div>
    <div>
        <h1 class="section-title">The Symbolic Fast Path: Lexer</h1>
        <h2 class="section-subtitle">Character-Level Regular Expressions and Abstract Token Mapping</h2>

        <p class="body-lead">
            The Lexer decomposes raw ASCII telemetry into discrete lexemes and classifies each into a formal token class over alphabet Σ = { LEVEL, IP, USER, STATUS, OTHER }.
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
                    Notice that IP address validation is not merely a naive digit check; it enforces mathematical bounding [0, 255] for each octet. An input such as <code>999.1.1.1</code> is automatically rejected and classified as <strong>OTHER</strong>, immediately exposing spoofed payloads.
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
                    The resulting token array ⟨ LEVEL, IP, OTHER, OTHER, STATUS ⟩ is transferred directly to the DFA input buffer.
                </p>
            </div>
        </div>
    </div>
    <div class="running-footer">
        <div class="footer-logo">HYBRID DFA–LLM ANOMALY ENGINE</div>
        <div>Theory of Computation (24B11CS212) • Final Technical Report</div>
        <div class="page-number-box">Page <span class="page-num">8</span> of 20</div>
    </div>
</section>"""

p9 = """<section class="page">
    <div class="running-header">
        <div class="header-left">
            <span class="header-badge">AUTOMATA THEORY</span>
            <span class="header-title">THE MINIMAL BASELINE DFA</span>
        </div>
        <div class="header-right">JIIT NOIDA • DEPT OF CSE</div>
    </div>
    <div>
        <h1 class="section-title">The Minimal Baseline DFA</h1>
        <h2 class="section-subtitle">Mathematical 5-Tuple Formulation and State Dynamics</h2>

        <p class="body-lead">
            The baseline structure recognizer is formally defined as a Deterministic Finite Automaton (DFA) 5-tuple:
            <br><code class="code-cell" style="font-size:9pt; font-weight:bold;">M = (Q, Σ, δ, q₀, F)</code>
        </p>

        <div class="grid-2">
            <div class="card-box">
                <h3 class="card-title">Formal 5-Tuple Specification</h3>
                <p class="body-text">
                    • <strong>State Set Q:</strong> { q₀, q₁, q₂, q₃, q₄, q<sub>E</sub> }<br>
                    • <strong>Alphabet Σ:</strong> { LEVEL, IP, USER, STATUS, OTHER }<br>
                    • <strong>Start State q₀:</strong> The initial state prior to consuming tokens.<br>
                    • <strong>Final / Accept State F:</strong> { q₄ } (Double Circle).<br>
                    • <strong>Trap / Dead State q<sub>E</sub>:</strong> An absorbing state representing rejection.
                </p>
            </div>
            <div class="card-box">
                <h3 class="card-title">Semantic State Interpretation</h3>
                <p class="body-text">
                    • <strong>q₁:</strong> Successfully parsed and validated <code>LEVEL</code> token.<br>
                    • <strong>q₂:</strong> Successfully parsed and validated <code>IP</code> token.<br>
                    • <strong>q₃:</strong> Successfully parsed and validated <code>USER</code> token.<br>
                    • <strong>q₄:</strong> Successfully parsed <code>STATUS</code> (Grammar satisfied).<br>
                    • <strong>q<sub>E</sub>:</strong> Irreversible trap state entered on unexpected token.
                </p>
            </div>
        </div>

        <!-- SVG 5: Minimal DFA State Transition Graph -->
        <div class="diagram-canvas" style="margin-top: 10px; padding: 10px;">
            <svg width="610" height="155" viewBox="0 0 610 155" fill="none" xmlns="http://www.w3.org/2000/svg">
                <!-- q0 -->
                <circle cx="50" cy="55" r="22" fill="#FAF5EE" stroke="#6A1A24" stroke-width="2"/>
                <text x="50" y="60" fill="#6A1A24" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold" text-anchor="middle">q₀</text>
                <path d="M15 55H28" stroke="#38231E" stroke-width="2"/>
                <polygon points="28,55 22,52 22,58" fill="#38231E"/>
                <text x="20" y="48" fill="#38231E" font-size="7" font-weight="bold">start</text>

                <!-- q0 -> q1 -->
                <path d="M72 55H138" stroke="#6A1A24" stroke-width="2"/>
                <polygon points="138,55 132,52 132,58" fill="#6A1A24"/>
                <text x="105" y="48" fill="#6A1A24" font-size="7.5" font-weight="bold" text-anchor="middle">LEVEL</text>

                <!-- q1 -->
                <circle cx="160" cy="55" r="22" fill="#FAF5EE" stroke="#6A1A24" stroke-width="2"/>
                <text x="160" y="60" fill="#6A1A24" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold" text-anchor="middle">q₁</text>

                <!-- q1 -> q2 -->
                <path d="M182 55H248" stroke="#6A1A24" stroke-width="2"/>
                <polygon points="248,55 242,52 242,58" fill="#6A1A24"/>
                <text x="215" y="48" fill="#6A1A24" font-size="7.5" font-weight="bold" text-anchor="middle">IP</text>

                <!-- q2 -->
                <circle cx="270" cy="55" r="22" fill="#FAF5EE" stroke="#6A1A24" stroke-width="2"/>
                <text x="270" y="60" fill="#6A1A24" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold" text-anchor="middle">q₂</text>

                <!-- q2 -> q3 -->
                <path d="M292 55H358" stroke="#6A1A24" stroke-width="2"/>
                <polygon points="358,55 352,52 352,58" fill="#6A1A24"/>
                <text x="325" y="48" fill="#6A1A24" font-size="7.5" font-weight="bold" text-anchor="middle">USER</text>

                <!-- q3 -->
                <circle cx="380" cy="55" r="22" fill="#FAF5EE" stroke="#6A1A24" stroke-width="2"/>
                <text x="380" y="60" fill="#6A1A24" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold" text-anchor="middle">q₃</text>

                <!-- q3 -> q4 -->
                <path d="M402 55H468" stroke="#238636" stroke-width="2"/>
                <polygon points="468,55 462,52 462,58" fill="#238636"/>
                <text x="435" y="48" fill="#238636" font-size="7.5" font-weight="bold" text-anchor="middle">STATUS</text>

                <!-- q4 (Final State) -->
                <circle cx="490" cy="55" r="24" fill="#FAF5EE" stroke="#238636" stroke-width="2"/>
                <circle cx="490" cy="55" r="20" fill="#FAF5EE" stroke="#238636" stroke-width="1.5"/>
                <text x="490" y="60" fill="#238636" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold" text-anchor="middle">q₄</text>
                <text x="490" y="94" fill="#238636" font-size="7" font-weight="bold" text-anchor="middle">ACCEPT</text>

                <!-- Trap State qE -->
                <circle cx="270" cy="120" r="20" fill="#FFF" stroke="#DA3633" stroke-width="2" stroke-dasharray="3 2"/>
                <text x="270" y="125" fill="#DA3633" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold" text-anchor="middle">q<sub>E</sub></text>
                <text x="315" y="125" fill="#DA3633" font-size="7" font-weight="bold">TRAP (REJECT)</text>

                <!-- Arrows to Trap -->
                <path d="M50 77V120H250" stroke="#DA3633" stroke-width="1" stroke-dasharray="2 2"/>
                <path d="M160 77V110H250" stroke="#DA3633" stroke-width="1" stroke-dasharray="2 2"/>
                <path d="M270 77V100" stroke="#DA3633" stroke-width="1" stroke-dasharray="2 2"/>
                <path d="M380 77V110H290" stroke="#DA3633" stroke-width="1" stroke-dasharray="2 2"/>
                <path d="M490 79V120H290" stroke="#DA3633" stroke-width="1" stroke-dasharray="2 2"/>

                <!-- Loop on qE -->
                <path d="M260 140C260 152 280 152 280 140" stroke="#DA3633" stroke-width="1.5"/>
                <text x="270" y="152" fill="#DA3633" font-size="6.5" text-anchor="middle">Σ (any token)</text>
            </svg>
        </div>
    </div>
    <div class="running-footer">
        <div class="footer-logo">HYBRID DFA–LLM ANOMALY ENGINE</div>
        <div>Theory of Computation (24B11CS212) • Final Technical Report</div>
        <div class="page-number-box">Page <span class="page-num">9</span> of 20</div>
    </div>
</section>"""

p10 = """<section class="page">
    <div class="running-header">
        <div class="header-left">
            <span class="header-badge">FORMAL PROOFS</span>
            <span class="header-title">TRANSITION MATRIX & MINIMALITY PROOF</span>
        </div>
        <div class="header-right">JIIT NOIDA • DEPT OF CSE</div>
    </div>
    <div>
        <h1 class="section-title">Total Transition Function</h1>
        <h2 class="section-subtitle">Full State Matrix Definition (Table 3) and Minimality Proof</h2>

        <p class="body-lead">
            To guarantee deterministic execution, the transition function <strong>δ: Q × Σ → Q</strong> is mathematically total across all |Q| × |Σ| = 6 × 5 = 30 state-token combinations.
        </p>

        <table class="editorial-table">
            <thead>
                <tr>
                    <th>State q ∈ Q</th>
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
                    <td><strong>→ q₀ (Start)</strong></td>
                    <td class="code-cell" style="font-weight:bold; color:#238636;">q₁</td>
                    <td class="code-cell">q<sub>E</sub></td>
                    <td class="code-cell">q<sub>E</sub></td>
                    <td class="code-cell">q<sub>E</sub></td>
                    <td class="code-cell">q<sub>E</sub></td>
                    <td>Non-final</td>
                </tr>
                <tr>
                    <td><strong>q₁</strong></td>
                    <td class="code-cell">q<sub>E</sub></td>
                    <td class="code-cell" style="font-weight:bold; color:#238636;">q₂</td>
                    <td class="code-cell">q<sub>E</sub></td>
                    <td class="code-cell">q<sub>E</sub></td>
                    <td class="code-cell">q<sub>E</sub></td>
                    <td>Non-final</td>
                </tr>
                <tr>
                    <td><strong>q₂</strong></td>
                    <td class="code-cell">q<sub>E</sub></td>
                    <td class="code-cell">q<sub>E</sub></td>
                    <td class="code-cell" style="font-weight:bold; color:#238636;">q₃</td>
                    <td class="code-cell">q<sub>E</sub></td>
                    <td class="code-cell">q<sub>E</sub></td>
                    <td>Non-final</td>
                </tr>
                <tr>
                    <td><strong>q₃</strong></td>
                    <td class="code-cell">q<sub>E</sub></td>
                    <td class="code-cell">q<sub>E</sub></td>
                    <td class="code-cell">q<sub>E</sub></td>
                    <td class="code-cell" style="font-weight:bold; color:#238636;">q₄</td>
                    <td class="code-cell">q<sub>E</sub></td>
                    <td>Non-final</td>
                </tr>
                <tr>
                    <td><strong>q₄ (Final)</strong></td>
                    <td class="code-cell">q<sub>E</sub></td>
                    <td class="code-cell">q<sub>E</sub></td>
                    <td class="code-cell">q<sub>E</sub></td>
                    <td class="code-cell">q<sub>E</sub></td>
                    <td class="code-cell">q<sub>E</sub></td>
                    <td><strong style="color:#238636;">ACCEPT (Double Circle)</strong></td>
                </tr>
                <tr>
                    <td><strong>q<sub>E</sub> (Trap)</strong></td>
                    <td class="code-cell">q<sub>E</sub></td>
                    <td class="code-cell">q<sub>E</sub></td>
                    <td class="code-cell">q<sub>E</sub></td>
                    <td class="code-cell">q<sub>E</sub></td>
                    <td class="code-cell">q<sub>E</sub></td>
                    <td><strong style="color:#DA3633;">REJECT (Absorbing)</strong></td>
                </tr>
            </tbody>
        </table>

        <div class="card-box accent-burgundy" style="margin-top: 10px;">
            <h3 class="card-title">Proof of Minimality (Myhill-Nerode Equivalence Theorem)</h3>
            <p class="body-text">
                <strong>Theorem:</strong> The baseline automaton <em>M</em> has the minimum possible number of states for regular language <em>L</em><sub>baseline</sub>.
            </p>
            <p class="body-text">
                <strong>Proof:</strong> Under the Myhill-Nerode theorem, two states <em>p, q</em> are equivalent (<em>p ≡ q</em>) iff for all strings <em>z</em> ∈ Σ*, δ̂(<em>p, z</em>) ∈ F ⇔ δ̂(<em>q, z</em>) ∈ F. Consider distinguishing suffixes <em>z</em>:
            </p>
            <p class="body-text" style="font-family: 'JetBrains Mono', monospace; font-size: 7.5pt; color: #6A1A24; line-height:1.5;">
                • Suffix z = ε distinguishes q₄ (since q₄ ∈ F) from all {q₀, q₁, q₂, q₃, q<sub>E</sub>} (since none ∈ F).<br>
                • Suffix z = STATUS distinguishes q₃ (leading to q₄ ∈ F) from {q₀, q₁, q₂, q<sub>E</sub>} (all leading to q<sub>E</sub> ∉ F).<br>
                • Suffix z = USER · STATUS distinguishes q₂ from {q₀, q₁, q<sub>E</sub>}.<br>
                • Suffix z = IP · USER · STATUS distinguishes q₁ from {q₀, q<sub>E</sub>}.<br>
                • Suffix z = LEVEL · IP · USER · STATUS distinguishes q₀ from q<sub>E</sub>.<br>
            </p>
            <p class="body-text">
                Every pair of states (<em>p, q</em>) in <em>Q</em> is pairwise distinguishable. Therefore, no two states can be merged, and the automaton of Table 3 is already mathematically minimal with |Q| = 6. ∎
            </p>
        </div>
    </div>
    <div class="running-footer">
        <div class="footer-logo">HYBRID DFA–LLM ANOMALY ENGINE</div>
        <div>Theory of Computation (24B11CS212) • Final Technical Report</div>
        <div class="page-number-box">Page <span class="page-num">10</span> of 20</div>
    </div>
</section>"""

with open(os.path.join(pages_dir, "page_6.html"), "w", encoding="utf-8") as f: f.write(p6)
with open(os.path.join(pages_dir, "page_8.html"), "w", encoding="utf-8") as f: f.write(p8)
with open(os.path.join(pages_dir, "page_9.html"), "w", encoding="utf-8") as f: f.write(p9)
with open(os.path.join(pages_dir, "page_10.html"), "w", encoding="utf-8") as f: f.write(p10)

print("[✓] Polished pages 6, 8, 9, 10.")

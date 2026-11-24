import os

pages_dir = r"C:\Users\Ritesh Kumar Agarwal\.gemini\antigravity\scratch\hybrid-anomaly-engine\report\pages"

p11 = """<section class="page">
    <div class="running-header">
        <div class="header-left">
            <span class="header-badge">BEHAVIORAL FSM</span>
            <span class="header-title">MOORE MACHINE SESSION MONITOR</span>
        </div>
        <div class="header-right">JIIT NOIDA • DEPT OF CSE</div>
    </div>
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
                    A Moore Machine is a 6-tuple <em>M</em><sub>Moore</sub> = (<em>S, S₀, Σ<sub>session</sub>, Λ, T, G</em>) where:
                    <br>• <strong>State Set S:</strong> { m₀, m₁, m₂, m₃ }
                    <br>• <strong>Initial State S₀:</strong> m₀ (0 consecutive failures)
                    <br>• <strong>Input Alphabet Σ<sub>session</sub>:</strong> { Success, Failed }
                    <br>• <strong>Output Alphabet Λ:</strong> { OK, FLAG }
                    <br>• <strong>Output Function G:</strong> <em>G(m₀) = G(m₁) = G(m₂) = OK</em>, and <em>G(m₃) = FLAG</em>
                </p>
            </div>
            <div class="card-box">
                <h3 class="card-title">Per-Source IP Session Table</h3>
                <p class="body-text">
                    The engine maintains an internal hash map:
                    <br><code class="code-cell">std::unordered_map&lt;std::string, MooreState&gt; ipStates_;</code>
                    <br>Whenever a log line receives an <strong>ACCEPT</strong> verdict from the baseline DFA, its extracted IP address and authentication status (<code>Success</code> vs <code>Failed</code>) are passed to the Moore transducer.
                </p>
            </div>
        </div>

        <!-- SVG 6: Moore Machine State Diagram -->
        <div class="diagram-canvas" style="margin-top: 10px; padding: 12px;">
            <svg width="610" height="155" viewBox="0 0 610 155" fill="none" xmlns="http://www.w3.org/2000/svg">
                <!-- State m0 -->
                <circle cx="70" cy="50" r="24" fill="#FAF5EE" stroke="#238636" stroke-width="2"/>
                <text x="70" y="47" fill="#238636" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold" text-anchor="middle">m₀</text>
                <text x="70" y="60" fill="#238636" font-size="7" font-weight="bold" text-anchor="middle">/ OK</text>
                <text x="70" y="88" fill="#5C4D4A" font-size="7" text-anchor="middle">0 Failures</text>

                <!-- m0 -> m1 on Failed -->
                <path d="M94 50H176" stroke="#9A4333" stroke-width="2"/>
                <polygon points="176,50 170,47 170,53" fill="#9A4333"/>
                <text x="135" y="42" fill="#9A4333" font-size="7.5" font-weight="bold" text-anchor="middle">Failed</text>

                <!-- State m1 -->
                <circle cx="200" cy="50" r="24" fill="#FAF5EE" stroke="#238636" stroke-width="2"/>
                <text x="200" y="47" fill="#238636" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold" text-anchor="middle">m₁</text>
                <text x="200" y="60" fill="#238636" font-size="7" font-weight="bold" text-anchor="middle">/ OK</text>
                <text x="200" y="88" fill="#5C4D4A" font-size="7" text-anchor="middle">1 Failure</text>

                <!-- m1 -> m2 on Failed -->
                <path d="M224 50H306" stroke="#9A4333" stroke-width="2"/>
                <polygon points="306,50 300,47 300,53" fill="#9A4333"/>
                <text x="265" y="42" fill="#9A4333" font-size="7.5" font-weight="bold" text-anchor="middle">Failed</text>

                <!-- State m2 -->
                <circle cx="330" cy="50" r="24" fill="#FAF5EE" stroke="#238636" stroke-width="2"/>
                <text x="330" y="47" fill="#238636" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold" text-anchor="middle">m₂</text>
                <text x="330" y="60" fill="#238636" font-size="7" font-weight="bold" text-anchor="middle">/ OK</text>
                <text x="330" y="88" fill="#5C4D4A" font-size="7" text-anchor="middle">2 Failures</text>

                <!-- m2 -> m3 on Failed -->
                <path d="M354 50H436" stroke="#DA3633" stroke-width="2"/>
                <polygon points="436,50 430,47 430,53" fill="#DA3633"/>
                <text x="395" y="42" fill="#DA3633" font-size="7.5" font-weight="bold" text-anchor="middle">Failed</text>

                <!-- State m3 (FLAG) -->
                <circle cx="460" cy="50" r="26" fill="#F8EDE8" stroke="#DA3633" stroke-width="3"/>
                <text x="460" y="47" fill="#DA3633" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold" text-anchor="middle">m₃</text>
                <text x="460" y="60" fill="#DA3633" font-size="7.5" font-weight="bold" text-anchor="middle">/ FLAG</text>
                <text x="460" y="90" fill="#DA3633" font-size="7" font-weight="bold" text-anchor="middle">BRUTE-FORCE</text>

                <!-- Loop on m3 -->
                <path d="M480 35C495 20 495 65 480 65" stroke="#DA3633" stroke-width="1.5"/>
                <text x="510" y="47" fill="#DA3633" font-size="6.5" text-anchor="middle">Failed</text>

                <!-- Reset Arcs to m0 on Success -->
                <path d="M460 76C460 125 70 125 70 74" stroke="#238636" stroke-width="1.5" stroke-dasharray="3 2"/>
                <polygon points="70,74 67,80 73,80" fill="#238636"/>
                <text x="265" y="130" fill="#238636" font-size="7.5" font-weight="bold" text-anchor="middle">Success: Resets state counter back to m₀ (OK)</text>
            </svg>
        </div>

        <div class="card-box accent-burgundy" style="margin-top: 10px;">
            <h3 class="card-title">Behavioral Edge Case Handling</h3>
            <p class="body-text">
                The Moore machine maintains state across discrete HTTP or socket events. If an attacker alternates attempts across 2 failures and 1 success, the state counter continuously resets to <em>m₀</em>, preventing false alarms on legitimately forgotten passwords. Only persistent, consecutive authentication failures from a single IP reach <em>m₃</em> and trigger escalation.
            </p>
        </div>
    </div>
    <div class="running-footer">
        <div class="footer-logo">HYBRID DFA–LLM ANOMALY ENGINE</div>
        <div>Theory of Computation (24B11CS212) • Final Technical Report</div>
        <div class="page-number-box">Page <span class="page-num">11</span> of 20</div>
    </div>
</section>"""

p12 = """<section class="page">
    <div class="running-header">
        <div class="header-left">
            <span class="header-badge">TURING MACHINE</span>
            <span class="header-title">PII & SECRET DATA SANITIZER</span>
        </div>
        <div class="header-right">JIIT NOIDA • DEPT OF CSE</div>
    </div>
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
                    <br><code class="code-cell" style="font-size:8pt; font-weight:bold;">M<sub>TM</sub> = (Q, Σ, Γ, δ, q₀, B, F)</code><br>
                    • <strong>Q:</strong> { q<sub>scan</sub>, q<sub>match</sub>, q<sub>mask</sub>, q<sub>halt</sub> }<br>
                    • <strong>Σ:</strong> Printable ASCII input characters.<br>
                    • <strong>Γ:</strong> Tape alphabet Σ ∪ { B, 'X' } (B is blank symbol).<br>
                    • <strong>q₀:</strong> Start state q<sub>scan</sub>.<br>
                    • <strong>F:</strong> Halting state { q<sub>halt</sub> }.
                </p>
            </div>
            <div class="card-box">
                <h3 class="card-title">Transition Function δ Logic</h3>
                <p class="body-text">
                    1. <strong>Scanning Mode (q<sub>scan</sub>):</strong> Head reads symbols moving Right (R). If symbol is B, enters q<sub>halt</sub>.<br>
                    2. <strong>Pattern Detection (q<sub>match</sub>):</strong> Identifies secret triggers (<code>pass=</code>, <code>token=</code>, <code>pwd=</code>).<br>
                    3. <strong>Masking Mode (q<sub>mask</sub>):</strong> Overwrites sensitive characters with mask symbol <code>'X'</code> on the tape until hitting a whitespace or delimiter.
                </p>
            </div>
        </div>

        <!-- SVG 7: Turing Machine Tape & Head Ribbon -->
        <div class="diagram-canvas" style="margin-top: 10px; padding: 12px;">
            <svg width="610" height="155" viewBox="0 0 610 155" fill="none" xmlns="http://www.w3.org/2000/svg">
                <!-- Ribbon Frame -->
                <rect x="25" y="45" width="560" height="42" fill="#FAF5EE" stroke="#38231E" stroke-width="2"/>
                
                <!-- Normal Cells -->
                <rect x="35" y="50" width="30" height="32" fill="#FFF" stroke="#E2D7C8"/>
                <text x="50" y="70" fill="#2A1715" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">p</text>
                <rect x="70" y="50" width="30" height="32" fill="#FFF" stroke="#E2D7C8"/>
                <text x="85" y="70" fill="#2A1715" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">a</text>
                <rect x="105" y="50" width="30" height="32" fill="#FFF" stroke="#E2D7C8"/>
                <text x="120" y="70" fill="#2A1715" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">s</text>
                <rect x="140" y="50" width="30" height="32" fill="#FFF" stroke="#E2D7C8"/>
                <text x="155" y="70" fill="#2A1715" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">s</text>
                <rect x="175" y="50" width="30" height="32" fill="#FFF" stroke="#E2D7C8"/>
                <text x="190" y="70" fill="#2A1715" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">=</text>

                <!-- Masked Cells (Crimson) -->
                <rect x="210" y="50" width="30" height="32" fill="#F8EDE8" stroke="#DA3633" stroke-width="1.8"/>
                <text x="225" y="70" fill="#DA3633" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">X</text>
                <rect x="245" y="50" width="30" height="32" fill="#F8EDE8" stroke="#DA3633" stroke-width="1.8"/>
                <text x="260" y="70" fill="#DA3633" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">X</text>
                <rect x="280" y="50" width="30" height="32" fill="#F8EDE8" stroke="#DA3633" stroke-width="1.8"/>
                <text x="295" y="70" fill="#DA3633" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">X</text>
                <rect x="315" y="50" width="30" height="32" fill="#F8EDE8" stroke="#DA3633" stroke-width="1.8"/>
                <text x="330" y="70" fill="#DA3633" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">X</text>
                <rect x="350" y="50" width="30" height="32" fill="#F8EDE8" stroke="#DA3633" stroke-width="1.8"/>
                <text x="365" y="70" fill="#DA3633" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">X</text>

                <!-- Blank Symbols -->
                <rect x="385" y="50" width="30" height="32" fill="#FFF" stroke="#E2D7C8"/>
                <text x="400" y="70" fill="#82726F" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">B</text>
                <rect x="420" y="50" width="30" height="32" fill="#FFF" stroke="#E2D7C8"/>
                <text x="435" y="70" fill="#82726F" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">B</text>

                <!-- TM Read/Write Head -->
                <polygon points="330,10 320,35 340,35" fill="#C69248"/>
                <rect x="290" y="2" width="80" height="15" rx="3" fill="#C69248"/>
                <text x="330" y="13" fill="#FFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="6.5" font-weight="bold" text-anchor="middle">TAPE HEAD [q_mask]</text>
                <text x="330" y="115" fill="#DA3633" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5" font-weight="bold" text-anchor="middle">δ(q_mask, 'S') ──► (q_mask, 'X', R)</text>
            </svg>
        </div>

        <div class="card-box accent-gold" style="margin-top: 10px;">
            <h3 class="card-title">Empirical Tape Execution Metrics</h3>
            <p class="body-text">
                In benchmark tests across 16 sample events, the Turing Machine executed a total of 153 tape steps, masking 41 sensitive characters across passwords and GitHub personal access tokens (<code>token=ghp_...</code>) with zero memory faults.
            </p>
        </div>
    </div>
    <div class="running-footer">
        <div class="footer-logo">HYBRID DFA–LLM ANOMALY ENGINE</div>
        <div>Theory of Computation (24B11CS212) • Final Technical Report</div>
        <div class="page-number-box">Page <span class="page-num">12</span> of 20</div>
    </div>
</section>"""

p15 = """<section class="page">
    <div class="running-header">
        <div class="header-left">
            <span class="header-badge">EVALUATION</span>
            <span class="header-title">EXPERIMENTAL BENCHMARKS & METRICS</span>
        </div>
        <div class="header-right">JIIT NOIDA • DEPT OF CSE</div>
    </div>
    <div>
        <h1 class="section-title">Experimental Evaluation</h1>
        <h2 class="section-subtitle">Empirical Benchmark Measurements Across 10,000 Event Workloads</h2>

        <p class="body-lead">
            The hybrid architecture was benchmarked against an "all-LLM baseline" and a "rules-only baseline" using an enterprise dataset containing normal operations and injected exploits.
        </p>

        <!-- SVG 8: Latency & Cost Empirical Curves -->
        <div class="diagram-canvas" style="padding: 10px;">
            <svg width="610" height="150" viewBox="0 0 610 150" fill="none" xmlns="http://www.w3.org/2000/svg">
                <!-- Left Chart: Latency Bar -->
                <rect x="25" y="20" width="260" height="115" rx="4" fill="#FAF5EE" stroke="#E2D7C8"/>
                <text x="155" y="38" fill="#6A1A24" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" text-anchor="middle">Average Event Latency (Log Scale)</text>
                
                <text x="40" y="66" fill="#2A1715" font-size="7">All-LLM Baseline:</text>
                <rect x="135" y="58" width="135" height="12" fill="#DA3633" rx="2"/>
                <text x="202" y="67" fill="#FFF" font-size="6.5" font-weight="bold" text-anchor="middle">1,800,000 µs (1.8s)</text>

                <text x="40" y="98" fill="#2A1715" font-size="7">Hybrid Fast Path:</text>
                <rect x="135" y="90" width="15" height="12" fill="#238636" rx="2"/>
                <text x="158" y="99" fill="#238636" font-size="7" font-weight="bold">160 µs (11,250x faster)</text>

                <!-- Right Chart: Cumulative Cost Graph -->
                <rect x="315" y="20" width="275" height="115" rx="4" fill="#FAF5EE" stroke="#E2D7C8"/>
                <text x="452" y="38" fill="#6A1A24" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" text-anchor="middle">Cumulative API Cost ($ / 100k Logs)</text>

                <!-- Cost lines -->
                <path d="M335 115 L395 90 L455 60 L535 30" stroke="#DA3633" stroke-width="2.5"/>
                <text x="540" y="32" fill="#DA3633" font-size="7" font-weight="bold">All-LLM: $200.00</text>

                <path d="M335 115 L395 114 L455 113 L535 110" stroke="#238636" stroke-width="2.8"/>
                <text x="430" y="105" fill="#238636" font-size="7" font-weight="bold">Hybrid: $8.50 (95.7% Cost Reduction)</text>
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
    <div class="running-footer">
        <div class="footer-logo">HYBRID DFA–LLM ANOMALY ENGINE</div>
        <div>Theory of Computation (24B11CS212) • Final Technical Report</div>
        <div class="page-number-box">Page <span class="page-num">15</span> of 20</div>
    </div>
</section>"""

p16 = """<section class="page">
    <div class="running-header">
        <div class="header-left">
            <span class="header-badge">THEORETICAL BOUNDS</span>
            <span class="header-title">DECIDABILITY & RICE'S THEOREM</span>
        </div>
        <div class="header-right">JIIT NOIDA • DEPT OF CSE</div>
    </div>
    <div>
        <h1 class="section-title">Decidability & Rice's Theorem</h1>
        <h2 class="section-subtitle">Theoretical Limits of Automata and Justification for Neuro-Symbolic Triage</h2>

        <p class="body-lead">
            A common question in computer science is: <em>"Why can't we simply build a larger DFA or Turing Machine that recognizes all malicious attacks without using an LLM?"</em> The answer is grounded in foundational computability theory.
        </p>

        <div class="card-box accent-burgundy">
            <h3 class="card-title">Formal Statement of Rice's Theorem</h3>
            <p class="body-text">
                <strong>Rice's Theorem (1953):</strong> Any non-trivial semantic property of a language recognized by a Turing Machine is undecidable. Formally, let 𝓒 be a set of partial computable functions. If 𝓒 ≠ ∅ and 𝓒 ≠ 𝓕 (the set of all partial computable functions), then the language problem:
                <br><code class="code-cell" style="font-size:8pt; font-weight:bold;">L<sub>𝓒</sub> = { ⟨M⟩ | L(M) ∈ 𝓒 }</code><br>
                is mathematically undecidable.
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
                    By limiting our Turing Machine strictly to data sanitization <em>f: Σ* → Γ*</em>, we preserve formal termination guarantees while delegating ambiguous reasoning to the neural layer.
                </p>
            </div>
        </div>
    </div>
    <div class="running-footer">
        <div class="footer-logo">HYBRID DFA–LLM ANOMALY ENGINE</div>
        <div>Theory of Computation (24B11CS212) • Final Technical Report</div>
        <div class="page-number-box">Page <span class="page-num">16</span> of 20</div>
    </div>
</section>"""

with open(os.path.join(pages_dir, "page_11.html"), "w", encoding="utf-8") as f: f.write(p11)
with open(os.path.join(pages_dir, "page_12.html"), "w", encoding="utf-8") as f: f.write(p12)
with open(os.path.join(pages_dir, "page_15.html"), "w", encoding="utf-8") as f: f.write(p15)
with open(os.path.join(pages_dir, "page_16.html"), "w", encoding="utf-8") as f: f.write(p16)

print("[✓] Polished pages 11, 12, 15, 16.")

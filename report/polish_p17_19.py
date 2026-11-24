import os

pages_dir = r"C:\Users\Ritesh Kumar Agarwal\.gemini\antigravity\scratch\hybrid-anomaly-engine\report\pages"

p17 = """<section class="page">
    <div class="running-header">
        <div class="header-left">
            <span class="header-badge">IMPLEMENTATION</span>
            <span class="header-title">PRESENTATION WEB DASHBOARD</span>
        </div>
        <div class="header-right">JIIT NOIDA • DEPT OF CSE</div>
    </div>
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
                    • <strong>Reactive Nodes:</strong> Nodes q₀ … q₄, q<sub>E</sub> animate with teal/red glowing halos as tokens are consumed.<br>
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
                        [1] DFA VERDICT: <span style="color:#2EA043;">[ACCEPT]</span> Path: q₀ → q₁ → q₂ → q₃ → q₄<br>
                        [2] MOORE MONITOR: State m₀ (OK) | Failures: 0
                    </div>
                    <div style="border:1px solid #30363D; padding:6px; border-radius:4px;">
                        [3] TAPE: [INFO] 192.168.1.75 pass=<span style="color:#F85149;">XXXXXXXXX</span> Failed<br>
                        [4] ROUTE: LOCAL FAST PATH (Latency: 160 µs, Cost: $0.00)
                    </div>
                </div>
            </div>
        </div>

        <div class="card-box accent-gold" style="margin-top: 10px;">
            <h3 class="card-title">Live Viva Demonstration Readiness</h3>
            <p class="body-text">
                The visual dashboard allows evaluators to click preset buttons (Case A, B, C, D) or type arbitrary log lines. State transitions, token classifications, and tape head movements animate in real-time, providing an intuitive defense of the underlying theoretical machinery.
            </p>
        </div>
    </div>
    <div class="running-footer">
        <div class="footer-logo">HYBRID DFA–LLM ANOMALY ENGINE</div>
        <div>Theory of Computation (24B11CS212) • Final Technical Report</div>
        <div class="page-number-box">Page <span class="page-num">17</span> of 20</div>
    </div>
</section>"""

p18 = """<section class="page">
    <div class="running-header">
        <div class="header-left">
            <span class="header-badge">SECURITY HARDENING</span>
            <span class="header-title">THREAT MODEL & ADVERSARIAL HARDENING</span>
        </div>
        <div class="header-right">JIIT NOIDA • DEPT OF CSE</div>
    </div>
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
                    <td>Pre-compiled DFA state tables guarantee 𝒪(N) without backtracking.</td>
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
    <div class="running-footer">
        <div class="footer-logo">HYBRID DFA–LLM ANOMALY ENGINE</div>
        <div>Theory of Computation (24B11CS212) • Final Technical Report</div>
        <div class="page-number-box">Page <span class="page-num">18</span> of 20</div>
    </div>
</section>"""

p19 = """<section class="page">
    <div class="running-header">
        <div class="header-left">
            <span class="header-badge">ROADMAP</span>
            <span class="header-title">ENTERPRISE SCALING & FUTURE DIRECTIONS</span>
        </div>
        <div class="header-right">JIIT NOIDA • DEPT OF CSE</div>
    </div>
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
                    Extending the alphabet Σ to model AWS IAM assume-role transitions and Kubernetes API audit logs, flagging privilege escalation via structural grammar violations.
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
    <div class="running-footer">
        <div class="footer-logo">HYBRID DFA–LLM ANOMALY ENGINE</div>
        <div>Theory of Computation (24B11CS212) • Final Technical Report</div>
        <div class="page-number-box">Page <span class="page-num">19</span> of 20</div>
    </div>
</section>"""

with open(os.path.join(pages_dir, "page_17.html"), "w", encoding="utf-8") as f: f.write(p17)
with open(os.path.join(pages_dir, "page_18.html"), "w", encoding="utf-8") as f: f.write(p18)
with open(os.path.join(pages_dir, "page_19.html"), "w", encoding="utf-8") as f: f.write(p19)

print("[✓] Polished pages 17, 18, 19.")

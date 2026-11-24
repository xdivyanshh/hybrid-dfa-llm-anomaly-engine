# Hybrid DFA–LLM Anomaly Engine with Turing Machine Sanitizer
**A Neuro-Symbolic Log Triage System Using Deterministic Finite Automata and Large Language Models**

* **Institution:** Jaypee Institute of Information Technology (JIIT), Noida
* **Department:** Computer Science & Engineering and Information Technology
* **Course:** Theory of Computation (24B11CS212)
* **Team Members:** Abhishek Bansal (2501030123), Divyansh Agarwal (2501030124), Arjun Bhardwaj (2501030134), Anirudh Sharma (2501030135)

---

## 📌 Architecture Overview

```
[Raw SSH Log Line]
       │
       ▼
[Lexer / Tokenizer] ──(Tokens: LEVEL, IP, USER, STATUS, OTHER)
       │
       ▼
[DFA Engine]
   ├── ACCEPT (q4) ──► [Moore Machine]
   │                      ├── OK ──► [Local Log Store] (Fast path, ~0 cost)
   │                      └── FLAG ─┐
   └── REJECT (qE) ─────────────────┤
                                    ▼
                     [TURING MACHINE SANITIZER]
                     • 7-tuple: M = (Q, Σ, Γ, δ, q0, B, F)
                     • Head scans tape & overwrites PII/secrets with 'X'
                     • Delivers clean sanitized payload
                                    │
                                    ▼
                          [Escalation Queue]
                                    │
                                    ▼
                         [LLM API via libcurl]
                                    │
                                    ▼
                          [Analyst Dashboard]
```

---

## 🧠 Theory of Computation Concepts Implemented

1. **Deterministic Finite Automaton (DFA)**:
   * 5-tuple: $M = (Q, \Sigma, \delta, q_0, F)$
   * $Q = \{q_0, q_1, q_2, q_3, q_4, q_E\}$
   * $\Sigma = \{\text{LEVEL, IP, USER, STATUS, OTHER}\}$
   * Start: $q_0$, Final: $F = \{q_4\}$, Trap state: $q_E$
   * Verifies log structure in $\mathcal{O}(N)$ linear time without catastrophic backtracking (ReDoS).

2. **Moore Machine (Finite State Transducer)**:
   * Behavioral session monitor tracking consecutive failed logins per source IP.
   * States: $m_0, m_1, m_2 \to \text{Output: OK}$; $m_3 \to \text{Output: FLAG}$.
   * Success resets state back to $m_0$.

3. **Turing Machine Sanitizer ($M_{TM}$)**:
   * 7-tuple: $M_{TM} = (Q, \Sigma, \Gamma, \delta, q_0, B, F)$
   * Tape alphabet $\Gamma = \Sigma \cup \{B, 'X'\}$.
   * Head scans the memory tape, transitions to $q_{\text{mask}}$ when sensitive credentials (e.g. `pass=`, `token=`) appear, overwrites them with `X` until delimiter, and halts at blank $B$.

4. **Decidability & Rice's Theorem**:
   * Explains why an automaton alone cannot detect all arbitrary malware (semantic properties are undecidable). The DFA enforces normal structure; the neural LLM provides contextual evidence.

---

## 🚀 How to Build and Run

### 1. Compile and Run the C++ Engine
```powershell
# From the project directory:
g++ -std=c++14 -O2 -I include src/lexer.cpp src/dfa.cpp src/moore.cpp src/turing_machine.cpp src/engine.cpp src/main.cpp -o anomaly_engine.exe
.\anomaly_engine.exe
```

### 2. Run the Automata Unit Test Suite
```powershell
g++ -std=c++14 -O2 -I include src/lexer.cpp src/dfa.cpp src/moore.cpp src/turing_machine.cpp tests/test_automata.cpp -o test_runner.exe
.\test_runner.exe
```

### 3. Open the Interactive Visual Web Dashboard
Simply double click or open in any web browser:
```text
web/index.html
```
Or serve locally via Python:
```powershell
python -m http.server 8000 --directory web
# Open http://localhost:8000 in your browser
```

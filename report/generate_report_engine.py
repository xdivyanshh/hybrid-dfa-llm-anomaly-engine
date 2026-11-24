import os
import subprocess

html_path = r"C:\Users\Ritesh Kumar Agarwal\.gemini\antigravity\scratch\hybrid-anomaly-engine\report\report.html"
pdf_path = r"C:\Users\Ritesh Kumar Agarwal\.gemini\antigravity\scratch\hybrid-anomaly-engine\report\Hybrid_DFA_LLM_Anomaly_Engine_Report.pdf"

# We will construct all 20 pages programmatically and write report.html
pages = []

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
        <div class="footer-logo">HYBRID DFA–LLM ENGINE</div>
        <div>Theory of Computation (24B11CS212) • Final Technical Report</div>
        <div class="page-number-box">Page <span class="page-num">{page_num}</span> of 20</div>
    </div>
    """

# ---------------- PAGE 1: COVER PAGE ----------------
page1 = """
<section class="page cover-page" style="background: radial-gradient(circle at 50% 20%, #FAF5EE 0%, #F3ECE1 100%); justify-content: space-between; border: 8px double #6A1A24; padding: 20mm;">
    <div style="text-align: center; border-bottom: 2px solid #C69248; padding-bottom: 12px;">
        <p style="font-family: 'Cinzel', serif; font-size: 11pt; letter-spacing: 2px; color: #6A1A24; font-weight: 700; margin-bottom: 4px;">JAYPEE INSTITUTE OF INFORMATION TECHNOLOGY, NOIDA</p>
        <p style="font-size: 8.5pt; color: #5C4D4A; letter-spacing: 1px; text-transform: uppercase;">Department of Computer Science & Engineering and Information Technology</p>
    </div>

    <div style="text-align: center; margin: 20px 0;">
        <div style="display: inline-block; background: #6A1A24; color: #FFF; font-size: 8.5pt; font-weight: 700; letter-spacing: 2px; padding: 4px 14px; border-radius: 20px; text-transform: uppercase; margin-bottom: 18px;">
            Course Project Report • Session 2026–2027
        </div>
        <h1 style="font-family: 'Playfair Display', serif; font-size: 27pt; line-height: 1.15; color: #2A1715; font-weight: 900; margin-bottom: 12px;">
            HYBRID DFA–LLM<br><span style="color: #6A1A24; font-style: italic;">ANOMALY ENGINE</span>
        </h1>
        <p style="font-size: 11pt; color: #9A4333; font-weight: 600; letter-spacing: 0.8px; max-width: 90%; margin: 0 auto; text-transform: uppercase;">
            A Neuro-Symbolic Log Triage System Using Deterministic Finite Automata, Moore Machines, and Large Language Models
        </p>
        <div style="width: 80px; height: 3px; background: #C69248; margin: 18px auto;"></div>
    </div>

    <!-- Formal Crest / Geometric Badge SVG -->
    <div style="text-align: center; margin: 10px 0;">
        <svg width="140" height="140" viewBox="0 0 140 140" fill="none" xmlns="http://www.w3.org/2000/svg">
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

# ---------------- PAGE 2: EXECUTIVE SUMMARY & CONTROL ----------------
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

# Write test setup to verify script runs cleanly
with open(html_path, "w", encoding="utf-8") as f:
    f.write("<!DOCTYPE html><html><head><style>" + css + "</style></head><body><div class='report-container'>" + page1 + page2 + "</div></body></html>")

print("[✓] First 2 pages generated. Proceeding to build full 20-page document...")

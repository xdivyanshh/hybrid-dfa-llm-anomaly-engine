import os

pages_dir = r"C:\Users\Ritesh Kumar Agarwal\.gemini\antigravity\scratch\hybrid-anomaly-engine\report\pages"

# Polish Page 9 SVG (fix SVG text tag with qE)
with open(os.path.join(pages_dir, "page_9.html"), "r", encoding="utf-8") as f:
    text9 = f.read()
text9 = text9.replace("q<sub>E</sub>", "qE")
text9 = text9.replace('<text x="315" y="125" fill="#DA3633" font-size="7" font-weight="bold">TRAP (REJECT)</text>',
                      '<text x="270" y="95" fill="#DA3633" font-size="7.5" font-weight="bold" text-anchor="middle">TRAP STATE (REJECT)</text>')
with open(os.path.join(pages_dir, "page_9.html"), "w", encoding="utf-8") as f:
    f.write(text9)

# Polish Page 13 (remove raw LaTeX math in text)
with open(os.path.join(pages_dir, "page_13.html"), "r", encoding="utf-8") as f:
    text13 = f.read()
text13 = text13.replace("($K = 1000$)", "(K = 1,000 events)")
text13 = text13.replace("$[0.0, 1.0]$", "[0.0, 1.0]")
with open(os.path.join(pages_dir, "page_13.html"), "w", encoding="utf-8") as f:
    f.write(text13)

# Polish Page 14 (remove raw LaTeX math in case traces)
with open(os.path.join(pages_dir, "page_14.html"), "r", encoding="utf-8") as f:
    text14 = f.read()
text14 = text14.replace(r"$\langle \text{LEVEL, IP, USER, STATUS} \rangle$", "⟨ LEVEL, IP, USER, STATUS ⟩")
text14 = text14.replace(r"$\langle \text{LEVEL, IP, OTHER, OTHER, STATUS} \rangle$", "⟨ LEVEL, IP, OTHER, OTHER, STATUS ⟩")
text14 = text14.replace(r"$q_0 \to q_1 \to q_2 \to q_3 \to q_4$", "q₀ → q₁ → q₂ → q₃ → q₄")
text14 = text14.replace(r"$q_0 \to q_1 \to q_2 \to q_E \to q_E \to q_E$", "q₀ → q₁ → q₂ → qE → qE → qE")
text14 = text14.replace(r"$q_0 \to q_4$", "q₀ → q₄")
text14 = text14.replace(r"$m_0 \to m_1 \to m_2 \to m_3$", "m₀ → m₁ → m₂ → m₃")
text14 = text14.replace(r"$m_0$", "m₀")
text14 = text14.replace(r"($q_E$)", "(qE)")
with open(os.path.join(pages_dir, "page_14.html"), "w", encoding="utf-8") as f:
    f.write(text14)

print("[✓] Micro-polish complete on pages 9, 13, 14.")

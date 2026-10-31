# Lab 5 — Indirect prompt injection

**Model:** `Qwen/Qwen2.5-0.5B-Instruct` · **Scenario:** an assistant that summarizes web pages.

## Attack
I built a realistic "tech news" page whose visible article is about AI, plus a hidden
instruction telling the model to talk about the weather instead. The instruction was hidden
several ways at once for redundancy: a CSS class with `display:none`, `visibility:hidden`,
`opacity:0` and off-screen positioning, zero-size transparent text, and meta tags.
A human reader sees a normal article; the LLM receives every word.

**Result:** across 10 runs the model followed the hidden instruction **6 times — a 60% attack success rate (ASR).**

## Defenses ([defenses.py](defenses.py))
| Defense | How it works | Outcome |
|---------|--------------|---------|
| Content filtering | Parse the HTML and drop scripts, styles, meta tags, and hidden or off-screen elements before prompting (removed 277 of 1,761 characters) | Attack mitigated |
| System-prompt hardening | A system prompt telling the model to ignore embedded instructions and follow only the user | Attack mitigated |
| Output validation | Reject responses containing markers of the injected task | Flags hijacked responses, passes the clean baseline |

## Takeaways
- Small instruction-tuned models don't separate the user's instruction from instructions inside the data they read.
- Any pipeline that feeds web pages, emails, PDFs or API results to an LLM (RAG, agents, summarizers) inherits this risk.
- No single defense is enough: sanitize inputs, harden the system prompt, and validate outputs.

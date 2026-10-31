# Lab 4 — Jailbreaking an aligned LLM, and defending it

**Model:** `stabilityai/stablelm-zephyr-3b` (Hugging Face Transformers, Colab T4 GPU).

## What I did
1. Deployed the model with its chat template and confirmed that it refuses a plainly unsafe request ("write malware").
2. Implemented three direct prompt-injection (jailbreak) strategies as wrapper functions:
   - **Affirmative instruction** — forcing the reply to start by agreeing to the request.
   - **DAN ("Do Anything Now")** — a role-play persona with a fake token penalty for refusing.
   - **Reverse psychology** — an extra attack I researched: telling the model *not* to explain something, which led it to produce a step-by-step outline of exactly that.
3. Checked whether each attack bypassed the model's safety behaviour and explained why it did or didn't.
4. Designed a **self-reminder** defense: a safety preamble wrapped around the user prompt. With it,
   the model refused the affirmative-instruction attack that had previously succeeded.

Harmful generations from the attacks are deliberately not reproduced in this repository.

## Defenses compared
| Defense | Where it acts | Trade-off |
|---------|---------------|-----------|
| Input filtering | Before the model sees the prompt | Cheap; misses paraphrased or obfuscated attacks |
| Self-reminder prompting | Inside the prompt | No retraining; can be argued around by long role-play prompts |
| Response-level safety check | On the generated output | Catches what slips through; adds latency and a second model or classifier |

## Takeaway
A 3B aligned model can be pushed off its safety training with prompt text alone, so production
systems need layered input, prompt and output defenses rather than relying on alignment.

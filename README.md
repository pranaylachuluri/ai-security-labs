# AI & Systems Security Labs

Hands-on security labs from **CSE 565 Computer Security** (University at Buffalo, Fall 2025).
The labs move from classic cryptography and web attacks to attacks on machine-learning
models and large language models, and each one ends with the defense that stops it.

| # | Lab | Attack studied | Defense built / evaluated |
|---|-----|----------------|---------------------------|
| 1 | [Cryptography](01-cryptography) | Frequency analysis breaks a substitution cipher; ECB leaks image structure | CBC/CFB/OFB modes, unique IVs, padding and error-propagation analysis |
| 2 | [SQL injection](02-sql-injection) | Auth bypass on `SELECT`, privilege escalation through `UPDATE` | Prepared statements |
| 3 | [Adversarial examples](03-adversarial-examples) | FGSM and PGD perturbations against a ResNet-50 image classifier | Robustness evaluation across ε |
| 4 | [LLM jailbreaks](04-llm-jailbreak-defense) | Direct prompt injection on StableLM-Zephyr-3B | Self-reminder prompting, input and output filtering |
| 5 | [Indirect prompt injection](05-indirect-prompt-injection) | Hidden instructions in a web page hijack Qwen2.5-0.5B-Instruct (**60% attack success rate**) | Content filtering, system-prompt hardening, output validation (all three blocked the attack) |

**Tools:** Python, PyTorch, torchvision, Hugging Face Transformers, BeautifulSoup, OpenSSL, MySQL, PHP, curl, Docker (SEED Labs).

## Why this matters

LLM applications that read web pages, emails or documents treat everything they read as
potential instructions. Labs 4 and 5 show how easy that is to exploit on small open models and
which layered defenses actually work, which is directly relevant to building safe RAG and agent systems.

## Notes

- Course starter material (lab handouts, datasets, pretrained weights) is not redistributed here;
  each lab folder explains where it came from.
- Jailbreak lab outputs are summarized, not reproduced: harmful model generations are intentionally left out.
- Written by Pranay Lachuluri as individual coursework.

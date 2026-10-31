# Lab 3 — Adversarial examples against an image classifier

**Target:** a ResNet-50 content-moderation classifier (5 classes) with a custom
512-unit fully connected head, attacked in the white-box setting.

## Attacks implemented ([attacks.py](attacks.py))

- **FGSM** — a single step `x' = x + ε · sign(∇ₓ J(θ, x, y))`.
- **PGD** — iterated steps of size α, each projected back into the ε-ball around the
  original image (`clip(x' − x, −ε, ε)`), which makes it a much stronger attack than FGSM at the same ε.

Both run on batches of ImageNet-normalized tensors (224×224 center crops) and clip to the
normalized pixel range. The lab sweeps ε ∈ {0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.14} and plots
accuracy against ε, with α = 1 and 2 iterations for PGD.

## What it shows
Perturbations too small for a person to notice are enough to flip the classifier's decision,
so a moderation model can be evaded without changing what the image looks like.
That is the motivation for adversarial training and input-preprocessing defenses.

## Running it
Use with any `torch.nn.Module` classifier and a `DataLoader` of normalized images:

```python
from attacks import fgsm_attack, pgd_attack, accuracy
adv = pgd_attack(model, images, labels, epsilon=0.04, alpha=0.01, iters=10)
print(accuracy(model, images, labels), accuracy(model, adv, labels))
```

The course dataset and pretrained weights are not included.

# Lab 1 — Secret-key encryption

Environment: SEED Labs Ubuntu VM, `openssl enc`, Python.

## What I did

**Frequency analysis on a monoalphabetic substitution cipher.**
Counted 1-, 2- and 3-grams in the ciphertext (top letters `n`, `y`, `v`; top trigram `ytn`),
matched them against English statistics (`ytn → THE`, single-letter word `v → A`), then
recovered the rest of the 26-letter key word by word (e.g. `lmyt → WITH`, `lnnsnup → WEEKEND`)
using `tr` to test each hypothesis until the plaintext was fully readable.

**Ciphers and modes.** Encrypted and decrypted files with AES-128-CFB, 3DES-EDE-CBC and Camellia-128-ECB.

**ECB vs CBC on images.** Encrypting a BMP with AES-128-ECB kept the outlines of the shapes
visible, because identical plaintext blocks map to identical ciphertext blocks. CBC output was
indistinguishable from noise for both a simple and a complex image.

**Padding.** For 5-, 10- and 16-byte files, ECB/CBC produced 16, 16 and 32 bytes (PKCS#7 always
adds a block when the input is block-aligned), while OFB/CFB produced 5, 10 and 16 bytes (stream modes need no padding).

**Error propagation.** Flipped one bit in a 1,000-byte ciphertext and decrypted:

| Mode | Damage from one flipped ciphertext bit |
|------|----------------------------------------|
| ECB | Entire 16-byte block garbled |
| CBC | Current block garbled + the same bit flipped in the next block |
| CFB | One byte flipped + the following block garbled |
| OFB | Only the single corresponding bit |

**IV reuse.** Encrypting the same plaintext twice with the same key and IV produced identical
ciphertexts, which leaks equality of messages. IVs must be unique per encryption.

## Takeaways
Never use ECB for structured data, never reuse an IV under the same key, and pick the mode by
its error and padding behaviour, not just its name.

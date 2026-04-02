# Cryptography_cia
Implementation of  a Cipher along with hash function

# Running Key Cipher + SDBM Hash

**Cipher assigned:** Running Key Cipher (Roll no. mod 10 = 5)  
**Language:** Python 3  
**Hash chosen:** SDBM Hash (implemented from scratch)

---

## Files

| File | Purpose |
|------|---------|
| `main.py` | Running Key Cipher (encrypt + decrypt) + user input + imports hash |
| `hash_function.py` | SDBM hash function implemented from scratch |
| `test_roundtrip.py` | Tests the full encrypt → hash → decrypt pipeline |

---

## Running Key Cipher - Theory

The running key cipher is a polyalphabetic substitution cipher. Instead of a short repeating keyword like in Vigenere, it uses a long piece of text (like a book passage) as the key. Each letter of the plaintext is shifted by the corresponding letter of the key.

**Encryption:**
```
C = (P + K) mod 26
```

**Decryption:**
```
P = (C - K + 26) mod 26
```

Where P, K, C are the alphabet positions of the plaintext, key, and ciphertext letters (A=0, B=1 ... Z=25). The +26 in decryption prevents negative values.

Since the key is as long as the plaintext and never repeats, the Kasiski test cannot be used to find the key length. This makes it harder to break than Vigenere with a short key.

---

## SDBM Hash - Theory

SDBM hash is a simple non-cryptographic hash function originally used in the sdbm database library. I chose it because I could understand and implement it completely from scratch.

**Formula (for each character):**
```
hash = char + (hash << 6) + (hash << 16) - hash
```

This is mathematically the same as `hash * 65599 + char`. The number 65599 distributes bits well and gives fewer collisions than simpler multipliers like 31 or 37. Output is a 32-bit value shown as an 8-character hex string.

I did not use MD5 or SHA because I wanted to actually understand what I was implementing.

---

## How to Run

No extra packages needed - just Python 3.

```bash
# Run the main program (shows examples + interactive input)
python main.py

# Run just the hash function
python hash_function.py

# Run the round-trip tests
python test_roundtrip.py
```

---

## Worked Examples

Running key used: *"To be or not to be that is the question whether tis nobler in the mind..."* (Hamlet)

### Example 1

| Field | Value |
|-------|-------|
| Plaintext | `HELLO` |
| Key letters | `TOBEO` |
| Ciphertext | `ASMPC` |
| SDBM Hash | `7af48aee` |
| Decrypted | `HELLO` ✓ |

Manual check for first letter:
- H = 7, T = 19 → (7 + 19) mod 26 = 0 → **A** ✓

### Example 2

| Field | Value |
|-------|-------|
| Plaintext | `NETWORKSECURITY` |
| Key letters | `TOBEORNOTTOBETH` |
| Ciphertext | `GSUACIXGXVISMMF` |
| SDBM Hash | `a69a1bd1` |
| Decrypted | `NETWORKSECURITY` ✓ |

---

## References

- Stinson, D.R. - Cryptography: Theory and Practice
- https://en.wikipedia.org/wiki/Running_key_cipher
- SDBM hash: http://www.cse.yorku.ca/~oz/hash.html

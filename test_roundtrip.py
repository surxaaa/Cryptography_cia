# test_roundtrip.py
# Tests the full pipeline: encrypt -> hash -> decrypt
# Checks that decrypted output matches original plaintext

from main import encrypt, decrypt, clean, RUNNING_KEY
from hash_function import sdbm_hash

def run_test(label, plaintext):
    p = clean(plaintext)
    enc = encrypt(plaintext, RUNNING_KEY)
    h   = sdbm_hash(enc)
    dec = decrypt(enc, RUNNING_KEY)

    passed = (dec == p)

    print(f"\nTest: {label}")
    print(f"  Plaintext   : {p}")
    print(f"  Ciphertext  : {enc}")
    print(f"  SDBM Hash   : {h}")
    print(f"  Decrypted   : {dec}")
    print(f"  Round-trip  : {'PASS' if passed else 'FAIL'}")
    return passed


print("=" * 50)
print("  Round-Trip Tests: Encrypt -> Hash -> Decrypt")
print("=" * 50)

results = []
results.append(run_test("Simple word",        "HELLO"))
results.append(run_test("With spaces",        "NETWORK SECURITY"))
results.append(run_test("Full phrase",        "CRYPTOGRAPHY IS FUN"))
results.append(run_test("Single letter",      "A"))
results.append(run_test("Repeated letters",   "AAAA"))

# tamper detection - show hash changes if ciphertext is modified
print("\n--- Tamper Detection ---")
enc_orig   = encrypt("HELLO", RUNNING_KEY)
tampered   = enc_orig[:-1] + ('B' if enc_orig[-1] != 'B' else 'C')
hash_orig  = sdbm_hash(enc_orig)
hash_tamp  = sdbm_hash(tampered)
print(f"  Original ciphertext : {enc_orig}  ->  hash: {hash_orig}")
print(f"  Tampered ciphertext : {tampered}  ->  hash: {hash_tamp}")
print(f"  Tamper detected     : {hash_orig != hash_tamp}")

print(f"\n{'=' * 50}")
print(f"  Results: {sum(results)}/{len(results)} tests passed")
print(f"{'=' * 50}")

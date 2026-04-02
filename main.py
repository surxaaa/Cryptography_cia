# main.py
# Running Key Cipher - Encryption and Decryption
# Uses a long piece of text as the key (one letter of key per letter of plaintext)
# Imports sdbm_hash from hash_function.py to hash the ciphertext

from hash_function import sdbm_hash

# the running key - using a passage from Hamlet
# must be longer than any message we want to encrypt
RUNNING_KEY = "To be or not to be that is the question whether tis nobler in the mind to suffer the slings and arrows of outrageous fortune or to take arms against a sea of troubles and by opposing end them to die to sleep no more and by a sleep to say we end the heartache"


def clean(text):
    # strips spaces and symbols, converts to uppercase
    result = ""
    for ch in text:
        if ch.isalpha():
            result += ch.upper()
    return result


def encrypt(plaintext, key):
    p = clean(plaintext)
    k = clean(key)

    if len(k) < len(p):
        print("Key is too short! Please use a longer running key.")
        return None

    ciphertext = ""
    for i in range(len(p)):
        p_val = ord(p[i]) - ord('A')    # A=0, B=1 ... Z=25
        k_val = ord(k[i]) - ord('A')
        c_val = (p_val + k_val) % 26
        ciphertext += chr(c_val + ord('A'))

    return ciphertext


def decrypt(ciphertext, key):
    c = clean(ciphertext)
    k = clean(key)

    if len(k) < len(c):
        print("Key is too short!")
        return None

    plaintext = ""
    for i in range(len(c)):
        c_val = ord(c[i]) - ord('A')
        k_val = ord(k[i]) - ord('A')
        p_val = (c_val - k_val + 26) % 26    # +26 so we dont get negatives
        plaintext += chr(p_val + ord('A'))

    return plaintext


def show_worked_example(label, plaintext, key):
    p = clean(plaintext)
    k = clean(key)
    print(f"\n--- {label} ---")
    print(f"Plaintext   : {p}")
    print(f"Key used    : {k[:len(p)]}")
    enc = encrypt(plaintext, key)
    h   = sdbm_hash(enc)
    dec = decrypt(enc, key)
    print(f"Ciphertext  : {enc}")
    print(f"SDBM Hash   : {h}")
    print(f"Decrypted   : {dec}")


def main():
    print("=" * 50)
    print("   Running Key Cipher")
    print("=" * 50)
    print("\nRunning Key (Hamlet excerpt):")
    print(f"  \"{RUNNING_KEY[:60]}...\"")

    # two worked examples shown automatically
    show_worked_example("Example 1", "HELLO", RUNNING_KEY)
    show_worked_example("Example 2", "NETWORK SECURITY", RUNNING_KEY)

    # interactive section - user inputs their own message
    print("\n" + "=" * 50)
    print("   Try it yourself")
    print("=" * 50)

    while True:
        print("\nOptions:")
        print("  1 - Encrypt a message")
        print("  2 - Decrypt a message")
        print("  3 - Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            msg = input("Enter plaintext: ").strip()
            if not msg:
                print("Nothing entered.")
                continue
            enc = encrypt(msg, RUNNING_KEY)
            if enc:
                h = sdbm_hash(enc)
                print(f"Ciphertext : {enc}")
                print(f"SDBM Hash  : {h}")

        elif choice == "2":
            msg = input("Enter ciphertext: ").strip()
            if not msg:
                print("Nothing entered.")
                continue
            dec = decrypt(msg, RUNNING_KEY)
            if dec:
                print(f"Decrypted  : {dec}")

        elif choice == "3":
            print("Exiting.")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()

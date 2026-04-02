# hash_function.py
# SDBM Hash - implemented from scratch
# 
# I chose SDBM hash because I could actually understand and implement it line by line.
# The formula is: hash = char + (hash << 6) + (hash << 16) - hash
# which is equivalent to multiplying by 65599 and adding the character value.
# 65599 was found experimentally to give good distribution with fewer collisions.
# Output is a 32-bit value displayed as an 8 character hex string.
# Originally used in the sdbm database library (hence the name).

def sdbm_hash(text):
    if type(text) != str:
        text = str(text)

    hash_val = 0

    for ch in text:
        # core sdbm formula
        hash_val = ord(ch) + (hash_val << 6) + (hash_val << 16) - hash_val

    # keep it within 32 bits
    hash_val = hash_val & 0xFFFFFFFF

    return format(hash_val, '08x')

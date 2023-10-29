def encrypt(k, m):
    """
    For sake of simplicity we use 2-bit key and plaintext blocks.
    
    Args:
    - k (int): A demo 2-bit encryption key. 
    - m (list of ints): A list of 2-bit integers as plaintext blocks.

    Returns:
    - list of ints: The encrypted ciphertext blocks.
    """
    
    # 1. Generate IV
    r_0 = 0b10  # A mock 2-bit IV for simplicity
    c_0 = r_0
    ciphertext = [c_0] # Add initial IV to ciphertext which will be returned.

    r_prev = r_0 # r_i buffer
    for i in m:
        # 3. (a) ri = "E(k, mi)", for sake of simplicity just XOR with key. Our Encryption box will just XOR m_i with key.
        r_i = i ^ k
        
        # 3. (b) ci = ri ⊕ ri−1
        c_i = r_i ^ r_prev

        ciphertext.append(c_i)

        r_prev = r_i

    # 4. return c0||c1||...||cn
    return ciphertext

def decrypt(k, c):
    """
    Decrypts a list of 2-bit ciphertext blocks using the provided 2-bit key.

    Args:
    - k (int): A demo decryption key.
    - c (list of ints): A list of 2-bit integers as ciphertext blocks.

    Returns:
    - list of ints: The decrypted plaintext blocks.
    """
    
    r_0 = c[0]  # A mock 2-bit IV for simplicity
    plaintext = []

    r_prev = r_0
    for i in range(1, len(c)):
        r_i = c[i] ^ r_prev # XOR ciphertext with corresponding r.

        m_i = r_i ^ k # We use XOR here because we XOR-ed also in encryption box.

        plaintext.append(m_i)
        r_prev = r_i

    return plaintext

# Example usage:
key = 0b01  # A mock/demo 2-bit key
print("Key:", '{0:02b}'.format(key))

plaintext = [0b10, 0b11, 0b00] # Some random 3 blocks of 2-bit plaintext
print("Plaintext:", ['{0:02b}'.format(m) for m in plaintext])

ciphertext = encrypt(key, plaintext)
print("Encrypted:", ['{0:02b}'.format(c) for c in ciphertext])

decrypted_text = decrypt(key, ciphertext)
print("Decrypted:", ['{0:02b}'.format(m) for m in decrypted_text])

print(f'Original plaintext should equal to decrypted text:', plaintext == decrypted_text)

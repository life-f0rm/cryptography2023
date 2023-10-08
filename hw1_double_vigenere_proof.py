# Importing the required libraries
from math import gcd

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Function to encrypt using Vigenere cipher
# Reference: https://www.geeksforgeeks.org/vigenere-cipher/
def vigenere_encrypt(plaintext: str, key: str) -> str:
    """
    Encrypts the plaintext using the Vigenere cipher algorithm with the provided key.

    Args:
        plaintext (str): The text to be encrypted.
        key (str): The key to be used for encryption.

    Returns:
        str: The encrypted text.
    """
    encrypted_text = ""
    
    # Iterate over each character in the plaintext
    for i in range(len(plaintext)):
        # Calculate the shift value using the key
        shift = ord(key[i % len(key)]) - ord('A')
        
        # Encrypt the character using the Vigenere cipher algorithm
        encrypted_char = chr(((ord(plaintext[i]) - ord('A') + shift) % 26) + ord('A'))
        
        # Append the encrypted character to the encrypted text
        encrypted_text += encrypted_char
    
    return encrypted_text

# Function to generate the combined key K3 from K1 and K2
def combine_keys(k1, k2, length):
    """
    Combine two keys to create a new key of a specified length.
    
    Args:
        k1 (str): The first key.
        k2 (str): The second key.
        length (int): The length of the new key.
    
    Returns:
        str: The combined key.
    """
    # Initialize an empty string to store the combined key
    k3 = ""
    
    # Iterate over each index in the range of the specified length
    for i in range(length):
        # Calculate the shift for the current character in k1
        shift_k1 = ord(k1[i % len(k1)]) - ord('A')
        
        # Calculate the shift for the current character in k2
        shift_k2 = ord(k2[i % len(k2)]) - ord('A')
        
        # Combine the shifts by taking the sum modulo 26
        combined_shift = (shift_k1 + shift_k2) % 26
        
        # Convert the combined shift back to a character and append it to k3
        k3 += chr(combined_shift + ord('A'))
    
    # Return the combined key
    return k3

# Example keys and message
k1 = "ABC"
k2 = "DEFG"
message = "CRYPTOGRAPHY IS FUN"

# Calculate LCM of the lengths of K1 and K2
length_lcm = lcm(len(k1), len(k2))

# Generate the combined key K3
k3 = combine_keys(k1, k2, length_lcm)

# Encrypt the message using K1 and then K2
first_encryption = vigenere_encrypt(message, k1)
second_encryption = vigenere_encrypt(first_encryption, k2)

# Encrypt the message directly using K3
single_encryption = vigenere_encrypt(message, k3)

print(f"""RESULTS:

First key: '{k1}' with length of: {len(k1)}
Second key: '{k2}' with length of: {len(k2)}
Combined key: '{k3}' with length of: {len(k3)}
Length of LCM(k1, k2) = len(k3): {length_lcm}
Plaintext message: '{message}'
First ciphertext(k1): '{first_encryption}'
Second ciphertext(k2): '{second_encryption}'
Third ciphertext(k3): '{single_encryption}'
Are Combined and Third ciphertexts equal?: {second_encryption == single_encryption}

END OF RESULTS!""")

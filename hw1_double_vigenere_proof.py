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



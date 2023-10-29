# Function to encrypt using Vigenere cipher
# Reference: https://www.geeksforgeeks.org/vigenere-cipher/


def vigenere_encrypt(plaintext: str, key: str) -> str:
    """
    Encrypts the plaintext using the Vigenere cipher algorithm with the provided key.
    To debug use vigenere_debug.py

    Args:
        plaintext (str): The text to be encrypted.
        key (str): The key to be used for encryption.

    Returns:
        str: The encrypted text.
    """
    encrypted_text = ""
    
    # Iterate over each character in the plaintext
    for i in range(len(plaintext)):
        # Calculate the shift value using the key.
        # Ex: if key is "MAGIC" and plaintext is "THEWANDCHOOSESTHEWIZARD"
        # for first round i = 0 modulo len key(5) = 0, Key[0] = 'M', ord('M') = 77 - ord('A') = 12, Shift = 12
        shift = ord(key[i % len(key)]) - ord('A')
        
        # Encrypt the character using the Vigenere cipher algorithm
        # Ex: if i = 0, plaintext[0] = "T", ord('T') - ord('A') + shift = 31 % 26 = 5 + ord('A') = 70 eg char(70) = 'F'
        encrypted_char = chr(((ord(plaintext[i]) - ord('A') + shift) % 26) + ord('A'))
        
        # Append the encrypted character to the encrypted text
        encrypted_text += encrypted_char
    
    return encrypted_text

message = "THEWANDCHOOSESTHEWIZARD"
key = "MAGIC"
ciphertext = vigenere_encrypt(message, key)

print(f"""RESULTS:

Message: '{message}'
Key: '{key}'
Ciphertext: '{ciphertext}'

END OF RESULTS!""")

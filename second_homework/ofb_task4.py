def permute(binary_string: int, key: tuple) -> str:
    """
    Generate a permutation of a binary string based on a key.

    Args:
        binary_string (int): The binary string to permute.
        key (tuple): The key used to determine the permutation.

    Returns:
        str: The permuted binary string.
    
    Example:
        >>> permute('01011', (4, 1, 3, 5, 2)) = '10011'
    """
    return ''.join(binary_string[k - 1] for k in key)

def get_letter_int(letter:str) -> int:
    """
    Calculate the integer value of a given letter.

    Args:
        letter (str): The uppercase letter to convert to an integer.

    Returns:
        int: The integer value of the given letter.
    """
    return ord(letter) - ord('A')

def get_letter_bin(letter:int) -> str:
    """
    Converts an integer representing a letter into a binary string.

    Parameters:
        letter (int): The integer representing the letter.

    Returns:
        str: The binary string representing the letter.
    """
    return '{:05b}'.format(letter)

def encrypt_in_ofb_mode(plaintext, key, iv):
    """
    Encrypts the given plaintext using the Output Feedback (OFB) mode.
    
    Args:
        plaintext (str): The plaintext to be encrypted.
        key (str): The encryption key.
        iv (str): The initialization vector.
    
    Returns:
        str: The encrypted ciphertext.
    """
    z_previous = iv
    ciphertext = ""

    print('Starting Encryption:\n')
    
    for i in range(len(plaintext)):
        # Convert letter to binary representation
        print(f'Round number: {i + 1}')
        x_current = plaintext[i]
        x_current_int = get_letter_int(x_current)
        x_current_bin = get_letter_bin(x_current_int)
        print(f'Current plaintext X_{i}: letter: {x_current}, int: {x_current_int}, bin: {x_current_bin}')
        
        # Compute Zi = EK(Zi-1)
        z_current = permute(z_previous, key)
        z_current_int = int(z_current, 2)
        print(f'Permuting: {z_previous} and {key}, Z_{i} = {z_current}, int: {z_current_int}')
        
        # Compute Yi = Xi XOR Zi
        y_current_int = x_current_int ^ z_current_int
        y_current = '{:05b}'.format(y_current_int)
        print(f'Y_{i} = {x_current_int} ⊕ {z_current_int} = {y_current_int}')
        print(f'Y_{i} = {x_current_bin} ⊕ {z_current} = {y_current}')

        print(f'Appending XOR result to ciphertext {ciphertext} + {y_current}\n')
        
        # Append the current ciphertext block to the overall ciphertext
        ciphertext += y_current
        
        # Update the previous Z value for the next iteration
        z_previous = z_current
    
    print(f'ciphertext binary:', ciphertext)
    
    print('End of Encryption!\n' + '-' * 100)

    return ciphertext

def decrypt_in_ofb_mode(ciphertext, key, iv):
    """
    Decrypts the given ciphertext using the Output Feedback (OFB) mode.

    Args:
        ciphertext (str): The ciphertext to be decrypted.
        key (str): The key used for decryption.
        iv (str): The initialization vector used for encryption.
    """
    z_previous = iv
    plaintext = ""
    plaintext_bits = ""

    print('Starting Decryption:\n')

    # Iterate over the ciphertext blocks
    for i in range(0, len(ciphertext), 5):
        r_nr = i // 5
        print(f'Round number: {r_nr}')
        # Extract the current ciphertext block
        y_current = ciphertext[i:i+5]
        print(f'Y_{r_nr} = {y_current}')

        # Compute Zi = EK(Zi-1)
        z_current = permute(z_previous, key)
        z_current_int = int(z_current, 2)
        print(f'Permuting: {z_previous} and {key}, Z_{r_nr} = {z_current}, int: {z_current_int}')
        
        # Compute Xi = Yi XOR Zi
        x_current_int = int(y_current, 2) ^ int(z_current, 2)
        x_current_bin = '{:05b}'.format(x_current_int)

        plaintext_bits += x_current_bin

        print(f'X_{r_nr} = {y_current} ⊕ {z_current} = {x_current_bin}')
        
        # Convert binary representation back to letter
        x_current_letter = chr(x_current_int + ord('A'))
        print(f'Current letter X_{r_nr}: letter: {x_current_letter}, int: {x_current_int}, bin: {x_current_bin}\n')
        
        # Append the decrypted letter to the plaintext
        plaintext += x_current_letter
        
        # Update the previous Z value for the next iteration
        z_previous = z_current
    
    print(f'message bin: {plaintext_bits}')
    print(f'message    : {plaintext}')
    
    print('End of Decryption!\n' + '-' * 100)

# Parameters
plaintext = "DOG"
key = (4, 1, 3, 5, 2)
iv = "01011"

# Encrypt using OFB mode
result = encrypt_in_ofb_mode(plaintext, key, iv)


modified_result = "100011010011111"
print(f'Modifing result with 5th bit flipped of {result} becoming {modified_result}!!!\n\n')
# Decrypt the ciphertext with 5th bit flipped of result
decrypt_in_ofb_mode(modified_result, key, iv)

# Decrypt the ciphertext with 1th bit flipped of iv
modified_iv = "11011"
print(f'Modifing result with 1th bit flipped of iv {iv} becoming {modified_iv}!!!\n\n')
decrypt_in_ofb_mode(result, key, modified_iv)

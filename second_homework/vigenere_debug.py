def np(num:str) -> str:
    """
    A function that pads a number with a space if it has only one digit.

    Parameters:
        num (str): The number to be padded.

    Returns:
        str: The padded number.
    """
    #Number padding
    return num + ' ' if len(num) == 1 else num

def vigenere_debug(plaintext: str, key: str):
    """
    Generates a debug table for the Vigenere cipher.

    Parameters:
    - `plaintext` (str): The plaintext to be encrypted.
    - `key` (str): The key used for encryption.

    Returns:
    - None
    """
    plain_num = []
    key_txt = []
    key_num = []
    ciph_num = []
    ciph_mod = []
    ciph_txt = []
    for i in range(len(plaintext)):
        key_i = ord(key[i % len(key)])
        plain_i = ord(plaintext[i]) - ord('A')
        c_i = (key_i + plain_i) - ord('A')

        plain_num.append(np(str(plain_i)))
        key_txt.append(key[i % len(key)])
        key_num.append(np(str(ord(key[i % len(key)]) - ord('A'))))
        ciph_num.append(np(str(c_i)))
        ciph_mod.append(np(str(c_i % 26)))
        ciph_txt.append(chr((c_i % 26) + ord('A')))
    
    table_length = (len(plaintext) * 5) + 6

    print(f"-"*table_length)
    print(f"m  : | {'  | '.join(plaintext)}  |")
    print(f"m_i: | {' | '.join(plain_num)} |")
    print(f"k  : | {'  | '.join(key_txt)}  |")
    print(f"k_i: | {' | '.join(key_num)} |")
    print(f"c_i: | {' | '.join(ciph_num)} |")
    print(f"c_m: | {' | '.join(ciph_mod)} |")
    print(f"c  : | {'  | '.join(ciph_txt)}  |")
    print(f"-"*table_length)
    pass


message = "THEWANDCHOOSESTHEWIZARD"
key = "MAGIC"

ciphertext = vigenere_debug(message, key)

# Demo_2
message = "THEWANDCHOOSESTHELIZARD" # One letter in message is changed 'W' -> 'L'
key = "MAGIC"
ciphertext = vigenere_debug(message, key)

# Demo_3
message = "THEWANDCHOOSESTHEWIZARD" # One letter in key is changed 'G' -> 'N'
key = "MANIC"
ciphertext = vigenere_debug(message, key)

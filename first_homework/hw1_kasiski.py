# Reference
# 1. https://github.com/ichantzaras/creamcrackerz
# 2. https://github.com/ichantzaras/creamcrackerz/blob/master/kasiski.py

from collections import defaultdict
from math import gcd
from functools import reduce

def find_repeated_sequences(cipher_text: str, seq_length: int) -> dict:
    """
    Finds repeated sequences in a given cipher text.

    Args:
        cipher_text (str): The cipher text to search for repeated sequences.
        seq_length (int): The length of the sequences to search for.

    Returns:
        dict: A dictionary containing the repeated sequences as keys and their positions as values.
    """
    # Create a dictionary to hold sequences and their positions
    sequences = defaultdict(list)

    # Find repeated sequences and their positions
    for i in range(len(cipher_text) - seq_length + 1): # Exmaple if cipertext is 200 chars - seq is 5 + 1: i = 0 - (201 - 5 + 1) = 197
        seq = cipher_text[i:i+seq_length] # Extract characters from index to index + sequence eq: 0:4 = 5 chars
        sequences[seq].append(i) # Append every character group into dictionary
    
    # Filter out sequences that do not repeat
    repeated_sequences = {k: v for k, v in sequences.items() if len(v) > 1} # Only keep sequences that repeat more than once.

    return repeated_sequences

def find_gcd_of_kasiski(kasiski_seq: dict):
    """
    Find the greatest common divisor (GCD) of a list of numbers.

    Parameters:
        num_list (list): A list of numbers for which the GCD needs to be found.

    Returns:
        int: The greatest common divisor of the numbers in the list.
    """
    gcd_list = kasiski_seq # Copy origanl list to gcd_list
    for item in kasiski_seq: # Iterate through list
        gcd_list[item] = (reduce(gcd, kasiski_seq[item])) # Find gcd of multiple numbers use reduce function ex: [5, 10, 15] = 5
    
    return gcd_list


# Given ciphertext
cipher_text = """
FHKOJASZAFUDTBJQLVMKFHKZKFWGACXWGGUMNGAVKSNWEWWNMPANKWHFHKUIXI
JMFEUJLGZLEBJDOAOJMDUWTKOAEGDEZZAUNMBQAPKVPQAXTATEGLNQSYVKOKCI
UMLCIAEHGXRKTUXQUNZVGIGXGHRITLQDSOVVTEXQITTJQTQCZQQZBABRQEBMUF
HKXQXTKZIQIYBYMSCWTFHZEQXOISGPDUWTEATLCFROKMETGQTOAYMKRYUCOQTN
QOIHKVAAUCMTQLGBGROXKNMSYPGIOATFPRUXYMSZMRMPKZDMSQMVEOTGQGRNMCPP
ATNDUMAHDOSCPPEXGQGRLMGFPKTVKOAEKFHHQVEOLKJMLQWTENKIMGPHMJUNJGQ
GITDKEIHTGSRGAAUXVQEEGVFECXMGOHMWVKOAZEANQ""".replace("\n", "")

# Length of sequence to look for
for seq in range(5, 2, -1):
    kasiski_seq = find_repeated_sequences(cipher_text, seq)
    print(f"For {seq} repeated chars: ", kasiski_seq)
    print(f"For {seq} character group GCD: ", find_gcd_of_kasiski(kasiski_seq))

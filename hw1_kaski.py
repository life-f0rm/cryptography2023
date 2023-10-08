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
    for i in range(len(cipher_text) - seq_length + 1):
        seq = cipher_text[i:i+seq_length]
        sequences[seq].append(i)
    
    # Filter out sequences that do not repeat
    repeated_sequences = {k: v for k, v in sequences.items() if len(v) > 1}

    return repeated_sequences

def find_gcd_of_kaski(kaski_seq: dict):
    """
    Find the greatest common divisor (GCD) of a list of numbers.

    Parameters:
        num_list (list): A list of numbers for which the GCD needs to be found.

    Returns:
        int: The greatest common divisor of the numbers in the list.
    """
    gcd_list = kaski_seq
    for item in kaski_seq:
        gcd_list[item] = (reduce(gcd, kaski_seq[item]))
    
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
    kaski_seq = find_repeated_sequences(cipher_text, seq)
    print(f"For {seq} repeated chars: ", kaski_seq)
    print(f"For {seq} character group GCD: ", find_gcd_of_kaski(kaski_seq))

# Reference
# 1. https://github.com/ichantzaras/creamcrackerz
# 2. https://github.com/ichantzaras/creamcrackerz/blob/master/kasiski.py

from collections import defaultdict

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
    print(f"For {seq} repeated chars: ",find_kaski(cipher_text, seq))

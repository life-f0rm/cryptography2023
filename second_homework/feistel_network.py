
def xor(i_1:int, i_2:int) -> int:
    """
    Calculates the bitwise XOR of two integers.

    Parameters:
        i_1 (int): The first integer.
        i_2 (int): The second integer.

    Returns:
        int: The result of the bitwise XOR operation.
    """
    return i_1 ^ i_2

def ib(i:int) -> str:
    """
    Returns an integer as a beautiful binary string.
    
    Args:
        i (int): The integer to be converted to a binary string.
        
    Returns:
        str: The beautiful binary string representation of the integer.
    """
    return '{:08b}'.format(i)[:4] + ' ' + '{:08b}'.format(i)[4:]

def bstri(bin:str) -> int:
    """
    Converts a binary string to an integer.

    Args:
        bin (str): The binary string to be converted.

    Returns:
        int: The integer representation of the binary string.
    """
    return int(bin, 2)

def logic(message:str, key:str, rounds:int = 6, debug:bool = True) -> tuple:
    """
    Performs encryption rounds on a message using a key.

    Feistel Network Logic:
        L = left half of message
        R = right half of message

        ki = k_(i-1) ⊕ bin(i)
        Ri = L_(i-1) ⊕ Fi(ki, R(i-1)) = L(i-1) ⊕ (ki ⊕ R(i-1))
        Fi = ki ⊕ R(i-1)
        Ri = L_(i-1) ⊕ Fi
        Li = Ri


    Args:
        message (str): The message to be encrypted.
        key (str): The encryption key.
        rounds (int, optional): The number of encryption rounds to perform. Defaults to 6.
        debug (bool, optional): Whether to print debug information during encryption. Defaults to True.

    Returns:
        tuple: A tuple containing the encrypted message.
    """

    # Initial data
    if len(message) % len(key) != 0:
        raise ValueError("Key must be half of the block size!")

    L_prev = bstri(message[:len(key)])
    R_prev = bstri(message[len(key):])
    F_prev = 0
    k_prev = bstri(key)


    # Perform the rounds of encryption
    for i in range(1, rounds + 1):

        k_i = xor(k_prev, i)  # XOR key with binary value of round number
        
        # Operations based on round number
        F_i = xor(k_i, R_prev)
        R_i = xor(L_prev, F_i)
        L_i = R_prev

        if debug:
            # Round debug block.
            print(f'Round {i}:')
            print(f'   k_{i - 1}   : {ib(k_prev)}')
            print(f'   bin({i}): {ib(i)}')
            print(f'   k_{i}   : {ib(k_prev)} ⊕ {ib(i)} = {ib(k_i)}')
            print(f'   F_{i}   : {ib(k_i)} ⊕ {ib(R_prev)} = {ib(F_i)}')
            print(f'   R_{i}   : {ib(L_prev)} ⊕ {ib(F_i)} = {ib(R_i)}')
            print(f'   L_{i}   : {ib(R_prev)}')
            print(f'End of round {i}.\n')
        

        # Update variables
        L_prev = L_i
        R_prev = R_i
        F_prev = F_i
        k_prev = k_i
    
    return L_i, R_i

message = "0110100110101111"
key = "01011001"
rounds = 6

L, R = logic(message, key, rounds)

print(f'Ciphertext: {ib(L)} {ib(R)}')

# This python code resolves Homework 1 Task 3: Unicity Distance
from typing import List
import math

import math

def unicity_distance_of_affine_cipher(n: int = 26, r: float = 1.8) -> float:
    """
    Calculates the unicity distance of an Affine cipher.

    Args:
        n: The size of the alphabet used in the cipher. Defaults to 26.
        r: The redundancy of the language. Defaults to 1.8.

    Returns:
        The unicity distance for the Affine cipher.

    Raises:
        ValueError: If n is less than or equal to 0.

    Notes:
        The unicity distance is a measure of the minimum length of ciphertext needed to uniquely determine the key used in an encryption scheme.
        It is calculated as the entropy of the key space divided by the redundancy of the language.

    Example:
        >>> unicity_distance_of_affine_cipher(26, 1.8)
        8.285402218862249
    """
    
    # Step 1: Find the cardinality 'K' for the Affine cipher key space of the defined alphabet size
    
    # To find 'a', we need to find all the possible coprimes of n (alphabet length)
    a = len(find_coprimes(n))
    
    # To find 'b', we need the total number of letters in the alphabet
    b = n
    
    # Calculate K as the product of a and b
    K = a * b
    
    print(f"\nTotal possible keys for Affine cipher with alphabet size:({n}) is: {K}\n")
    
    # Step 2: Calculate the entropy H(K) of the key space in the Affine cipher
    
    # Calculate H as the logarithm base 2 of K
    H = math.log2(K)
    
    print(f"Entropy for this Affine cipher with alphabet size:({n}) is: ~ {round(H, 2)}\n")
    
    # Step 3: Calculate the unicity distance for the Affine cipher
    
    # In case of a 26-letter alphabet, a single letter contains log2 26 ≈ 4.7 bits of information
    R = math.log2(n)
    
    # Meaningful English texts contain just about 1.5 bits of information per letter
    D = R - r
    
    # Calculate U as the ratio of H and D
    U = H / D
    
    print(f"Unicity distance for this Affine cipher with alphabet size:({n}) is: ~ {round(U, 2)}\n")
    
    return U


def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (gcd) of two numbers using the Euclidean algorithm.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The greatest common divisor of the two numbers.
    """
    while b:  # Loop until 'b' becomes zero
        # Use Euclidean algorithm to find gcd
        a, b = b, a % b  # Put 'a' mod 'b' (reminder) into 'b' and put 'b' into 'a'

    return a  # Return latest value of 'a' eg. greatest common divisor (gcd)

def find_coprimes(n: int) -> List[int]:
    """
    Finds the coprimes of a given number.

    Args:
        n (int): The number to find coprimes with.

    Returns:
        List[int]: A list of coprimes of the given number.
    """

    coprimes = []  # List where we collect coprimes

    # Iterate from 1 to n (n is the number that we need to find coprimes with)
    for i in range(1, n):
        # If the greatest common divisor is one, then it is a coprime
        if gcd(i, n) == 1:
            coprimes.append(i)

    return coprimes


if input("Run with default values (language rate, r = 1.8, alphabet size, n = 26)? (Y/n): ").lower() == "n":
    r = float(input("Enter language rate: "))
    n = int(input("Enter alphabet size: "))
    unicity_distance_of_affine_cipher(n, r)
else:
    unicity_distance_of_affine_cipher()

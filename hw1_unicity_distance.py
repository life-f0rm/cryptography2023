# This python code resolves Homework 1 Task 3: Unicity Distance
from typing import List
import math




def unicity_distance_of_affine_cipher(n: int = 26, r: float = 1.8) -> float:
    """
    Calculates U = H(K)/D

    Step 1: Find Cardinality 'K' for the Affine cipher key space of defined alphabet size
      1.1 To find 'a' we need to find all possible coprimes of n (alphabet lenght)
      1.2 To find 'b' we need total number of letters in alphabet
    """
    a = len(find_coprimes(n))
    b = n
    K = a * b

    print(f"\nTotal possible keys for Affine cipher with alphabet size:({n}) is: {K}\n")

    """
    Step 2: Find entropy H(K) of the key space in Affine cipher
    """
    H = math.log2(K)

    print(f"Entropy for this Affine cipher with alphabet size:({n}) is: {H}\n")

    """
    Step 2: Find the unicity distance for an Affine cipher.
    """
    R = math.log2(n) # In case of 26-letter alphabet, a single letter contains log2 26 ≈ 4.7 bits of information.
    D = R - r # Meaningful english texts contain just about 1.5 bits of information per letter.
    U = H / D # Calculates unicity distance

    print(f"Unicity distance for this Affine cipher with alphabet size:({n}) is: {U}\n")

    return U


def gcd(a: int, b: int) -> int:
    while b: # Loop until 'b' becomes zero
        # Use Euclidean algorithm to find gcd
        a, b = b, a % b # Put 'a' mod 'b' (reminder) into 'b' and put 'b' into 'a' and 

    return a # Return latest value of 'a' eg. greatest common divisor (gcd)

def find_coprimes(n: int) -> List[int]:

    coprimes = [] # List where do we collect coprimes

    for i in range(1, n): # Iterate from 1 to n (n is number that we need to find coprimes with)

        if gcd(i, n) == 1: # If greatest common divisor is one then it is coprime

            coprimes.append(i)

    return coprimes


if input("Run with default values (language rate, r = 1.8, alphabet size, n = 26)? (Y/n): ").lower() == "n":
    r = float(input("Enter language rate: "))
    n = int(input("Enter alphabet size: "))
    unicity_distance_of_affine_cipher(r, n)
else:
    unicity_distance_of_affine_cipher()
    
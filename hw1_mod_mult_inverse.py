# Reference https://www.geeksforgeeks.org/python-program-for-basic-and-extended-euclidean-algorithms-2/
# Rference https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
# Reference https://www.educative.io/answers/what-is-extended-euclidean-algorithm
def extended_gcd(a, b):
    """
    Compute the Extended Euclidean Algorithm for a and b.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        Tuple[int, int, int]: A tuple containing the greatest common divisor of a and b,
        and the coefficients x and y such that ax + by = gcd(a, b).
    """
    # Initialize the coefficients
    x0, x1, y0, y1 = 1, 0, 0, 1 # Initialize x0, x1, y0, y1

    # Perform the Extended Euclidean Algorithm
    while b != 0: # Loop until b becomes zero. If b = 0, then a = gcd
        q, a, b = a // b, b, a % b # quotient = a // b, a = b and b = remainder of a / b
        x0, x1 = x1, x0 - q * x1 # save x1 as x0, save x1 as x0 - quotient * x1
        y0, y1 = y1, y0 - q * y1 # Do same for y.

    # Return the result
    return a, x0, y0

def mod_inverse(a: int, m: int) -> int:
    """
    Compute the modular multiplicative inverse of a modulo m.

    Args:
        a (int): The number for which the inverse is to be computed.
        m (int): The modulo value.

    Returns:
        int: The modular multiplicative inverse of a modulo m, or None if it does not exist.
    """
    # Compute the extended gcd of a and m
    gcd, x, y = extended_gcd(a, m)

    if gcd != 1:
        return None  # Modular multiplicative inverse does not exist
    else:
        return x % m # Modular multiplicative inverse = reminder of coefficient x / modulo
    
# Test the function
a = 19
m = 97
inverse = mod_inverse(a, m)
print(f"The modular multiplicative inverse of {a} modulo {m} is {inverse}")

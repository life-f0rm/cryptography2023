
def gcd(a, b):
    """
    Calculate the greatest common divisor (GCD) of two numbers.

    Parameters:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The GCD of the two numbers.
    """

    while b:

        a, b = b, a % b

    return a

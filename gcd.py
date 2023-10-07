
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

def old_gcd(a, b):
    """
    Calculate the greatest common divisor (GCD) of two numbers.

    Parameters:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The GCD of the two numbers.
    """
    # Continue the loop as long as b is not zero
    while b != 0:
        # Find the remainder when a is divided by b
        remainder = a % b
        
        # Set a to the value of b
        a = b
        
        # Set b to the value of the remainder
        b = remainder
    
    # Once b becomes zero, a will hold the GCD of the original a and b
    return a

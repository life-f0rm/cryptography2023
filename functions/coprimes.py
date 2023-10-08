import gcd
gcd = gcd.gcd
def coprimes(n):
    """
    Find all the numbers that are coprime with a given number.

    Parameters:
    - n (int): The number to find coprimes for.

    Returns:
    - coprimes (List[int]): A list of numbers that are coprime with `n`.
    """

    coprimes = []

    for i in range(1, n):

        if gcd(i, n) == 1:

            coprimes.append(i)

    return coprimes

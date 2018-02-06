def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0                         """ New Line Added to remove the error """
    while x >= a:
        count += 1
        x = x - a
    return count

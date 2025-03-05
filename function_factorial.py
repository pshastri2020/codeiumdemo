
def function_factorial(n):

    """
    Calculate the factorial of a given integer.

    Args:
        n (int): The input number.

    Returns:
        int: The factorial of n.

    Examples:
        >>> function_factorial(5)
        120
    """
    if n == 0:
        return 1
    else:
        return n * function_factorial(n - 1)
    

result = function_factorial(5)
print(result)   

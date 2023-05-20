def my_add(a: int, b: int) -> int: 
    """add two numbers and returns the result
    
    Args:
    a(int, int) --the first number
    b(int, int) --the second number

    Returns:
    the sum
    """

    return a + b

print(my_add(5,7), my_add.__annotations__, my_add.__doc__)
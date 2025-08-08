def factorial(n):
    """
    Gets the factorial of a number.
    """
    if n < 0:
        raise ValueError("Cannot get the factorial of a negative number.")
    if n == 0:
        return 1
    else:
        return factorial(n-1)*n

if __name__ == "__main__":
    print(factorial(5))
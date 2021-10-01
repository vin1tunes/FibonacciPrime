from math import sqrt


def recursive_fibonacci(n):
    if isinstance(n, int) and n >= 0:  # Verifica se n é um inteiro e maior ou igual a zero.
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
    else:
        return None


def linear_fibonacci(n):
    if isinstance(n, int) and n >= 0:  # Verifica se n é um inteiro e maior ou igual a zero.
        result = ((1 + sqrt(5))**n - (1 - sqrt(5))**n) / (2**n * sqrt(5))
        return round(result)

def prime_number(n):
    # Verifica se um número é primo.

    counter = 0
    for i in range(1, n + 1):
        if n % i == 0:
            counter += 1
    return counter == 2


def prime_sequence(n):
    if isinstance(n, int) and n > 1:  # Verifica se n é um inteiro e maior que um.
        return [n for n in range(1, n + 1) if prime_number(n)]

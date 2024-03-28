"""
Exemplo de modulo com doctests.

O modulo fornece a função fatorial(). Exemplos:

>>> fatorial(5)
120

>>> fatorial2(5)
120
"""


def fatorial(n):
    """Calcula o fatorial de um inteiro >= 0

    Args:
        n (int): Um número inteiro >= 0.

    Returns:
        int: O fatorial de n.

    >>> [fatorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]

    >>> fatorial(30)
    265252859812191058636308480000000

    >>> fatorial(-1)
    Traceback (most recent call last):
    ...
    ValueError: n tem de ser >= 0

    O fatorial de float pode ser calculado deste que seja também um inteiro:
    >>> fatorial(30.1)
    Traceback (most recent call last):
    ...
    ValueError: n tem de ser inteiro

    E não pode ser demasiadamente grande:
    >>> fatorial(1e100)
    Traceback (most recent call last):
    ...
    OverflowError: n demasiado grande
    """
    if n < 0:
        raise ValueError("n tem de ser >= 0")

    if n.__floor__() != n:
        raise ValueError("n tem de ser inteiro")

    if n + 1 == n:  # catch a value like 1e100
        raise OverflowError("n demasiado grande")

    result = 1
    for factor in range(1, n + 1):
        result *= factor

    return result


def fatorial2(n):
    """
    :return: o fatorial de um inteiro >= 0.

    >>> [fatorial2(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]

    >>> fatorial2(30)
    265252859812191058636308480000000

    >>> fatorial2(-1)
    Traceback (most recent call last):
    ...
    AssertionError: n tem de ser >= 0

    o fatorial de float pode ser calculado deste que seja também um inteiro
    >>> fatorial2(30.1)
    Traceback (most recent call last):
    ...
    AssertionError: n tem de ser inteiro

    E não pode ser "ridiculamente" grande
    >>> fatorial2(1e100)
    Traceback (most recent call last):
    ...
    AssertionError: n demasiado grande
    """
    assert n >= 0, "n tem de ser >= 0"
    assert n.__floor__() == n, "n tem de ser inteiro"
    assert n + 1 != n, "n demasiado grande"

    result = 1
    for factor in range(1, n + 1):
        result *= factor

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=False)

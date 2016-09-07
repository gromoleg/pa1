def karatsuba(x, y) -> int:
    """
    multiply x by y using simplified Karatsuba method
    """
    x, y = str(x), str(y)
    n = len(x)
    a, b, c, d = int(x[:n // 2]), int(x[n // 2:]), int(y[:n // 2]), int(y[n // 2:])
    ac, bd = a * c, b * d
    return (10 ** n) * ac + (10 ** (n // 2)) * ((a + b) * (c + d) - ac - bd) + bd

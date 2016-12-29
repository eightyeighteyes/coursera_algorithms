def karatsuba(x, y):
    """
    Divide-and-conquer recursive multiplication strategy.
    x = 10^n/2 * a + b
    y = 10^n/2 * c + d
    x * y = 10^n * ac + 10^(n/2) (ad+bc) + bd
    where (ad+bc) = (a+b)(c+d) - ac - bd
    """
    if all([x < 10, y < 10]):
        return x * y

    # calculate base size:
    m = max(len(str(x)), len(str(y)))

    m2 = m / 2

    a = x / 10 ** m2
    b = x % 10 ** m2
    c = y / 10 ** m2
    d = y % 10 ** m2

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)

    adbc = karatsuba(a + b, c + d) - ac - bd

    return ac * 10 ** (2 * m2) + (adbc * 10 ** m2) + bd

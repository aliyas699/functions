def power(base, exponent):
    result = 1
    for _ in range(abs(exponent)):
        result *= base
    if exponent < 0:
        result = 1 / result  # Handle negative exponents
    return result
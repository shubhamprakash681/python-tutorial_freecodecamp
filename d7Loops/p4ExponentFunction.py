def exponent(base, power):
    result = 1
    while power >= 1:
        result *= base
        power -= 1
    return result


if __name__ == '__main__':
    bse = float(input('Enter Base: '))
    powr = float(input('Enter Power: '))
    print(str(exponent(bse, powr)))

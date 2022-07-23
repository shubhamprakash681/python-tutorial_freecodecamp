def calc(a, b, opr):
    if opr == "+":
        return float(a) + float(b)
    elif opr == "-":
        return float(a) - float(b)
    elif opr == "*":
        return float(a) * float(b)
    elif opr == "/":
        return float(a) / float(b)
    elif opr == "%":
        return float(a) % float(b)
    elif opr == 'q':
        return 'Exiting'
    else:
        return 'Wrong operator entered'


if __name__ == "__main__":
    operator = '+'
    while operator != 'q':
        num1 = input('Enter number1: ')
        num2 = input('Enter number1: ')

        operator = input('Enter operator or enter \'q\' to exit: ')
        print(operator)
        print(calc(num1, num2, operator))

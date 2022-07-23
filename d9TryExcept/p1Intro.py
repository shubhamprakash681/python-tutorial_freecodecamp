try:
    number1 = float(input('Enter a number: '))
    number2 = float(input('Enter another number: '))
    quotient = number1/number2

    print(quotient)
except ValueError as verr:
    print(verr)
    print('Invalid Input')
except ZeroDivisionError as zderr:
    print(zderr)
    print('Division by zero is not possible')

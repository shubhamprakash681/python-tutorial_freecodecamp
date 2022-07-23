def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


if __name__ == "__main__":
    n1 = input('Enter number1: ')
    n2 = input('Enter number2: ')
    n3 = input('Enter number3: ')

    print('Maximum of ' + n1 + ', ' + n2 + ', ' + n3 + ' is: '
          + str(max_num(float(n1), float(n2), float(n3))))

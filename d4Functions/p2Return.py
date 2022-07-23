def cube_a_number(num):
    return num * num * num


if __name__ == '__main__':
    my_num = input('Enter a number: ')
    print('Cube of ' + str(my_num) + ' is ' + str(cube_a_number(float(my_num))))

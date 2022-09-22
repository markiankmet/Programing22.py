from random import randint as rand
LIMITS1, LIMITS2 = -9, 9
menu_options = {1: 'Enter vectors', 2: 'Random generate vectors in a certain range', 3: 'Exit'}


def check_if_integer(user_input):
    it_is = False
    while not it_is:
        try:
            integer = int(user_input)
            it_is = True
            return integer
        except ValueError:
            user_input = input('Valid value, Try again: ')
            it_is = False


def check_if_numeric(x):
    check_x = False
    while not check_x:  # check if x is number
        if x.isnumeric():
            check_x = True
            x = int(x)
            return x
        else:
            x = input('Invalid Error! Try again: ')


def input_vector(n):
    vector = []
    if n != 0:
        print(f'Enter {n} values: ')
        for i in range(n):
            vector.append(check_if_integer(input()))
    return vector


def generate_vector(n):
    random_vector = []
    if n != 0:
        for i in range(n):
            random_vector.append(rand(LIMITS1, LIMITS2))
    return random_vector


def find_max_in_vector(vector):
    max_in_half = vector[0]
    max_index = 0
    for i in range(len(vector)):
        if max_in_half < vector[i]:
            max_in_half = vector[i]
            max_index = i
    return max_in_half, max_index


def input1(op):
    n = check_if_numeric(input('Enter a dimension: '))
    if n != 0:
        if op == 1:
            x = input_vector(n)
            y = input_vector(n)
            z = input_vector(n)
        elif op == 2:
            x = generate_vector(n)
            y = generate_vector(n)
            z = generate_vector(n)
        copy_vector_x = x[:len(x) // 2]
        res, max_index_half = find_max_in_vector(copy_vector_x)
        k = check_if_integer(input('Enter K: '))
        if res == k and all(val < 0 for val in y):
            max_in_x, max_index_x = find_max_in_vector(x)
            for i in range(max_index_x):
                x[i] = pow(x[i], 3)
        print(f'vector x: {x}\nvector y: {y}\nvector z: {z}')
    else:
        print('Vectors is empty!')


def print_menu():
    for key in menu_options.keys():
        print(key, menu_options[key], sep='--')


while True:
    print_menu()
    option = check_if_numeric(input('Enter your choice: '))
    if option == 1:
        input1(option)
    elif option == 2:
        input1(option)
    elif option == 3:
        print('Good luck, Bye!')
        exit()
    else:
        print('Invalid option. Please enter a number in range 1-3')

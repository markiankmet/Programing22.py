menu_options = {1: 'Generate a square matrix with dimension n', 2: 'Exit'}


def check_if_numeric(x):
    check_x = False
    while not check_x:  # check if x is number
        if x.isnumeric():
            check_x = True
            x = int(x)
            return x
        else:
            x = input('Invalid Error! Try again: ')


def print_menu():
    for key in menu_options.keys():
        print(key, menu_options[key], sep='--')


def generate_matrix():
    n = check_if_numeric(input('Enter a dimension of matrix: '))
    m = [[0 for j in range(n)] for i in range(n)]
    k = s = 0
    for i in range(n):
        k += 1
        s += 1
        for j in range(n - s + 1):
            m[i][j] = k
    for i in range(n):
        print(*m[i])


while True:
    print_menu()
    option = check_if_numeric(input('Enter your choice: '))
    if option == 1:
        generate_matrix()
    elif option == 2:
        print('Good luck, Bye!')
        exit()
    else:
        print('Invalid option. Please enter a number 1 or 2')

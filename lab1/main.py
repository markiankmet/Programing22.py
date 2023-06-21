LIMITS1 = 1000
LIMITS2 = 0


def check_if_numeric(x):
    check_x = False
    while not check_x:  # check if x is number
        if x.isnumeric():
            check_x = True
            x = int(x)
            return x
        else:
            x = input('Invalid Error! Try again: ')


def check_number_size(x):
    if x > LIMITS1:
        return False
    elif x < LIMITS2:
        return False
    else:
        return True


def number_ways_to_cut_tree(n, m):   # function to count number of ways to cut trees
    if not check_number_size(n):
        print('Invalid value(n > 1000)')
        return
    elif not check_number_size(m):
        print('Invalid value(m > 1000)')
    elif m > n:  # check if m bigger than n
        print('Invalid value(m > n)')
        return
    else:
        res = 0
        if m == 0:
            res = 1  # if 0 tree remain it's one way
        elif m == 1:
            res = n  # if 1 tree remain than n ways to cut down
        else:
            distance = int((n - 1) / (m - 1))  # distance between trees
            for i in range(1, distance + 1):
                res += n - (m - 1) * i
        return res


menu_options = {1: 'Start program(Number of ways to cut trees)', 2: 'Exit'}


def print_menu():
    for key in menu_options.keys():
        print(key, menu_options[key], sep='--')


def main_program():
    n = check_if_numeric(input('Enter number of trees: '))
    m = check_if_numeric(input('Enter number of trees that should remain: '))
    result = number_ways_to_cut_tree(n, m)
    print(f'Result = {result}.')


while True:
    print_menu()
    option = check_if_numeric(input('Enter your choice: '))
    if option == 1:
        main_program()
    elif option == 2:
        print('Good bye!')
        exit()
    else:
        print('Invalid option. Please enter a number 1 or 2!')

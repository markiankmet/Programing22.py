from MyList import LinkedList
from check_functions import *
menu_options = {1: 'Enter list by keyboard', 2: 'Random generate list in a certain range', 3: 'Do option 11',
                4: 'Generate by iterator', 5: 'Generate by generator', 6: 'Exit'}
question_options = {1: 'Delete on k position', 2: 'Insert in k position', 3: 'Exit'}


def print_menu():
    for key in menu_options.keys():
        print(key, menu_options[key], sep='--')


def question_delete_insert(arg: LinkedList):
    while True:
        for key in question_options:
            print(key, question_options[key], sep=' : ')
        option = check_if_numeric(input('Enter what you want: '))
        if option == 1:
            k = check_if_numeric(input('Enter an index: '))
            arg.erase(k)
            arg.output_list()
        elif option == 2:
            k = check_if_numeric(input('Enter an index: '))
            new_value = check_if_integer(input('Enter a new value: '))
            arg.insert(k, new_value)
            arg.output_list()
        elif option == 3:
            return
        else:
            print('Invalid option. Please enter a number in range 1-3!')


while True:
    print_menu()
    option_ = check_if_numeric(input('Enter your choice: '))
    if option_ == 1:
        n = check_if_numeric(input('Enter a dimension of list: '))
        list_ = LinkedList()
        print('Enter a list:')
        list_.input_keyboard(n)
        list_.output_list()
        question_delete_insert(list_)
    elif option_ == 2:
        n = check_if_numeric(input('Enter a dimension of list: '))
        list_ = LinkedList()
        list_.generate_random(n)
        list_.output_list()
        question_delete_insert(list_)
    elif option_ == 3:
        n = check_if_numeric(input('Enter a dimension of list: '))
        x = LinkedList()
        y = LinkedList()
        z = LinkedList()
        print('Enter a list x: ')
        x.input_keyboard(n)
        print('Enter a list y: ')
        y.input_keyboard(n)
        print('Enter a list z: ')
        z.input_keyboard(n)
        max_value, max_idx = x.find_max()
        idx_half = (n // 2)
        k_ = check_if_integer(input('Enter K: '))
        if max_value == k_ and y.is_negative() and max_idx < idx_half:
            x.made_kub(max_idx)
        print('Vector x: ', end=' ')
        x.output_list()
        print('Vector y: ', end=' ')
        y.output_list()
    elif option_ == 4:
        x = LinkedList()
        size = check_if_numeric(input('Enter a dimension: '))
        a = check_if_integer(input('Enter a: '))
        b = check_if_integer(input('Enter b: '))
        x.generate_by_iterator(size, a, b)
        x.output_list()
    elif option_ == 5:
        x = LinkedList()
        size = check_if_numeric(input('Enter a dimension: '))
        a = check_if_integer(input('Enter a: '))
        b = check_if_integer(input('Enter b: '))
        x.generate_elements(size, a, b)
        x.output_list()
    elif option_ == 6:
        print('Good luck, Bye!')
        exit()
    else:
        print('Invalid option. Please enter a number in range 1-6!')

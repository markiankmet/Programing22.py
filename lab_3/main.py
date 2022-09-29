from linked_list import *
menu_options = {1: 'Enter list by keyboard', 2: 'Random generate list in a certain range', 3: 'Do option 11', 4: 'Exit'}


def input_from_keyboard():
        n = check_if_numeric(input('Enter a dimension of list: '))
        list_ = LinkedList()
        list_.input_list(n)
        list_.list_print()
        question_delete_insert(list_, n)


def random_generate():
        n = check_if_numeric(input('Enter a dimension of list: '))
        a = check_if_integer(input('Enter a: '))
        b = check_if_integer(input('Enter b: '))
        list_ = LinkedList()
        list_.generate_random_list(n, a, b)
        list_.list_print()
        question_delete_insert(list_, n)


def option11():
    n = check_if_numeric(input('Enter a dimension: '))
    if n != 0:
        x = y = z = LinkedList()
        x.input_list(n)
        y.input_list(n)
        z.input_list(n)
        new_list = x.made_kub()
        max_value, index_max = x.find_max()
        index_half = (n // 2)
        k = check_if_integer(input('Enter K: '))
        if max_value == k and x.is_negative() and index_max < index_half:
            for i in range(index_max):
                new_list[i] = pow(new_list[i], 3)
        for i in range(n):
            print(new_list[i], sep='\t')
    else:
        print('Vectors is empty!')


def question_delete_insert(arg:LinkedList, arg_n):
    while True:
        choice = check_if_numeric(input("1.Delete on k position\n2.Insert in k position\n3.Back\n"))
        if choice == 1:
            k = check_if_integer(input("Enter position: "))
            if check_position(k, arg_n):
                continue
            arg.delete_element(k)
            arg.list_print()
        if choice == 2:
            k = check_if_integer(input("Enter position: "))
            if check_position(k, arg_n):
                continue
            to_ad = check_if_integer(input("Enter element: "))
            arg.insert_value(to_ad, k)
            arg_n += 1
            arg.list_print()
        if choice == 3:
            return


def print_menu():
    for key in menu_options.keys():
        print(key, menu_options[key], sep='--')


while True:
    print_menu()
    option = check_if_numeric(input('Enter your choice: '))
    if option == 1:
        input_from_keyboard()
    elif option == 2:
        random_generate()
    elif option == 3:
        option11()
    elif option == 4:
        print('Good luck, Bye!')
        exit()
    else:
        print('Invalid option. Please enter a number in range 1-3')

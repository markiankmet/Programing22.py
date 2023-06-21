from Strategy import *

menu_options = {1: 'Strategy 1', 2: 'Strategy 2', 3: 'Generate elements',
                4: 'Delete element on k position', 5: 'Delete elements in range', 6: 'Do option 11',
                7: 'Print list', 8: 'Exit'}


def print_menu():
    for key in menu_options.keys():
        print(key, menu_options[key], sep='--')


def generate(list_, context):
    index = check_if_numeric(input('Enter an index: '))
    context = validate_generation(context)
    if isinstance(context.strategy, StrategyA):
        n = check_if_numeric(input('Dimension of list: '))
    else:
        n = validate_file()
    return context.generate(list_, index, n)


def program():
    list_ = LinkedList()
    context = None
    while True:
        print_menu()
        option = check_if_numeric(input('Enter what you want: '))
        if option == 1:
            context = Context(StrategyA())
            continue
        elif option == 2:
            context = Context(StrategyB())
        elif option == 3:
            generate(list_, context)
            continue
        elif option == 4:
            k = check_if_numeric(input('Enter k: '))
            list_.erase(k)
            continue
        elif option == 5:
            a = check_if_numeric(input('Enter a: '))
            b = check_if_numeric(input('Enter b: '))
            if b >= list_.length() + 1:
                print("Index out of range!!")
            else:
                list_.delete_in_range(a, b)
            continue
        elif option == 6:
            max_value, max_index = list_.find_max()
            ind_half = (list_.length() // 2)
            k_ = check_if_integer((input('Enter K: ')))
            if max_value == k_ and max_index < ind_half:
                list_.made_kub(max_index)
        elif option == 7:
            list_.output_list()
        elif option == 8:
            print('Good luck, Bye!')
            exit()
        else:
            print('Invalid option. Please enter a number in range 1-8!')


program()

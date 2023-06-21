import copy
from Strategy import *
from logger import *
from event import Event
from observer import Observer


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
    copy_list = copy.deepcopy(list_)
    context.generate(list_, index, n)
    Event("Add", copy_list, list_, index)


def program():
    obs = Observer()
    obs.observe("Add")
    obs.observe("Remove")
    obs.observe('Change')
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
            copy_list = copy.deepcopy(list_)
            deleted_list = []
            deleted_list.append(copy_list.return_by_index(k))
            list_.erase(k)
            Event("Remove", deleted_list, list_, k)
            continue
        elif option == 5:
            a = check_if_numeric(input('Enter a: '))
            b = check_if_numeric(input('Enter b: '))
            copy_list = copy.deepcopy(list_)
            if b >= list_.length() + 1:
                print("Index out of range!!")
            else:
                list_.delete_in_range(a, b)
                deleted_list = []
                for i in range(a, b):
                    deleted_list.append(copy_list.return_by_index(i))
                Event('Remove', deleted_list, list_, a, b)
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

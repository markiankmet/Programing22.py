from Validation import *
from Collection_cars import *
from decorators import repeat_if_error
menu_options = {1: 'Search information in collection', 2: 'Sort elements',
                3: 'Delete car from collection by id', 4: 'Add new element in collection and file',
                5: 'Edit element in collection by id', 6: 'Print collection', 7: 'Exit'}


def print_menu():
    for key in menu_options.keys():
        print(key, menu_options[key], sep='--')


@repeat_if_error
def program():
    path = 'data.txt'
    collection_ = Collection(path)
    collection_.read_from_file()
    while True:
        print_menu()
        option = check_if_numeric(input('Enter your choice: '))
        if option == 1:
            search_element = input('Enter what to search: ')
            collection_.search(search_element)
        elif option == 2:
            for i in menu_fields:
                print(menu_fields[i], end=' ')
            print()
            field = input()
            collection_.sort(field)
        elif option == 3:
            id_ = check_id(input('Enter id: '))
            collection_.remove(id_)
        elif option == 4:
            collection_.add()
        elif option == 5:
            collection_.edit_by_id()
        elif option == 6:
            print(collection_)
        elif option == 7:
            print('Good luck, Bye!')
            exit()
        else:
            print('Invalid option. Please enter a number in range 1-7')


program()
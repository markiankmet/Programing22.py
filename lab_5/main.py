from memento import *
menu_options = {1: 'Search information in collection', 2: 'Sort elements',
                3: 'Delete car from collection by id', 4: 'Add new element in collection and file',
                5: 'Edit element in collection by id', 6: 'Print collection', 7: 'Undo', 8: 'Redo', 9: 'Exit'}


def print_menu():
    for key in menu_options.keys():
        print(key, menu_options[key], sep='--')


def program():
    file_name = input_file(input('Enter a file: '))
    collection_ = Collection(file_name)
    collection_.read_from_file()
    caretaker = CareTaker(collection_)
    while True:
        print_menu()
        option = check_if_numeric(input('Enter your choice: '))
        if option == 1:
            search_element = input('Enter what to search: ')
            collection_.search(search_element)
        elif option == 2:
            caretaker.create()
            print_fields()
            field = input()
            for fields in menu_fields:
                if menu_fields[fields] == field:
                    collection_.sort(field)
        elif option == 3:
            caretaker.create()
            id_ = check_id(input('Enter id: '))
            collection_.remove(id_)
        elif option == 4:
            caretaker.create()
            collection_.add()
        elif option == 5:
            caretaker.create()
            collection_.edit_by_id()
        elif option == 6:
            print(collection_)
        elif option == 7:
            caretaker.undo()
            collection_.write_in_file()
        elif option == 8:
            caretaker.redo()
            collection_.write_in_file()
        elif option == 9:
            print('Good luck, Bye!')
            exit()
        else:
            print('Invalid option. Please enter a number in range 1-9')


program()

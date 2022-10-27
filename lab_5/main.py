from memento import *
menu_options = {1: 'Search information in collection', 2: 'Sort elements',
                3: 'Delete car from collection by id', 4: 'Add new element in collection and file',
                5: 'Edit element in collection by id', 6: 'Print collection', 7: 'Undo', 8: 'Redo', 9: 'Exit'}


def print_menu():
    for key in menu_options.keys():
        print(key, menu_options[key], sep='--')


def program():
    file_name = input_file(input('Enter file: '))
    collection_ = Collection(file_name)
    collection_.read_from_file()
    originator = Originator()
    caretaker = CareTaker()
    memento(originator, caretaker, collection_)
    while True:
        print_menu()
        option = check_if_numeric_(input('Enter your choice: '))
        if option == 1:
            search_element = input('Enter what to search: ')
            collection_.search(search_element)
        elif option == 2:
            print_fields()
            field = input()
            collection_.sort(field)
            memento(originator, caretaker, collection_)
        elif option == 3:
            id_ = check_if_numeric_(input('Enter id: '))
            collection_.remove(id_)
            memento(originator, caretaker, collection_)
        elif option == 4:
            collection_.add()
            memento(originator, caretaker, collection_)
        elif option == 5:
            print_fields()
            collection_.edit_by_id()
            memento(originator, caretaker, collection_)
        elif option == 6:
            print(collection_)
        elif option == 7:
            originator.restore(caretaker.undo())
            write_changes_after(originator, file_name)
            collection_.read_from_file()
        elif option == 8:
            originator.restore(caretaker.redo())
            write_changes_after(originator, file_name)
            collection_.read_from_file()
        elif option == 9:
            print('Good luck, Bye!')
            exit()
        else:
            print('Invalid option. Please enter a number in range 1-9')


program()

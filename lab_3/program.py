from Collection_of_Cars import *
from Validation_fields import *
from check_functions import *
menu_options = {1: 'Read cars from file into collection', 2: 'Write down data collection to another file',
                3: 'Search information in collection', 4: 'Sort elements',
                5: 'Delete car from collection by id', 6: 'Add new element in collection and file',
                7: 'Edit element in collection by id', 8: 'Print collection', 9: 'Exit'}


def print_menu():
    for key in menu_options.keys():
        print(key, menu_options[key], sep='--')


while True:
    print_menu()
    option = check_if_numeric(input('Enter your choice: '))
    if option == 1:
        collection = Collection()
        file = Validation.input_file("Name of the file: ")
        collection.read_from_file(file)
        print(collection)
        continue
    elif option == 2:
        file = Validation.input_file("Name of the file: ")
        collection.write_in_file(file)
        print("Data was written in file ", file)
        continue
    elif option == 3:
        collection.search(input("Enter what you want to search: "))
    elif option == 4:
        field = input_field()
        collection.sort(field)
    elif option == 5:
        ID = check_id()
        collection.delete(str(ID))
    elif option == 6:
        elem = Car.input_car("ID", "brand", "model", "registration_number",
                             "last_repaired_at", "bought_at", "car_mileage")
        collection.add(elem)
        collection.add_element_to_file("DataOutput.txt", elem)
    elif option == 7:
        id = check_id()
        field = input_field()
        value = input_value()
        collection.edit_by_id(str(id), field, value)
    elif option == 8:
        print(collection)
    elif option == 9:
        print('Good luck, Bye!')
        exit()
    else:
        print('Invalid option. Please enter a number in range 1-9')


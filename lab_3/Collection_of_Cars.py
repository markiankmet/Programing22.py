from Car import *
import json


class Collection:
    def __init__(self):
        self.list = []

    def __str__(self):
        text = ""
        for i in range(len(self.list)):
            text += str(self.list[i]) + "\n"
        return text

    def __getitem__(self, item):
        return self.list[item]

    def __len__(self):
        return len(self.list)

    def __setitem__(self, key, value):
        self.list[key] = value

    def add(self, element):
        self.list.append(Car(**element))
        Car(**element).validate_car()

    def read_from_file(self, file):
        Validation.check_file(file)
        file_op = open(file)
        file = json.load(file_op)
        for i, car_ in enumerate(file):
            self.list.append(Car(**car_))
            Car(**car_).validate_car()

    def delete(self, id):
        for element in self.list:
            if str(element.ID) == id:
                self.list.remove(element)
                break
        else:
            print("No car with this id!")

    def edit_by_id(self, id, attr, value):
        for element in self.list:
            if str(element.ID) == id:
                setattr(element, attr, value)
                break
        else:
            print(f"No car with this  id : {id}!")

    def write_in_file(self, file):
        Validation.check_file(file)
        f = open(file, mode="w")
        f.writelines(str(i) + "\n" for i in self.list)
        f.close()

    def add_element_to_file(self, file, element):
        Validation.check_file(file)
        f = open(file, mode="a+", encoding="utf-8")
        f.writelines(str(element) + "\n")

    def sort(self, field=""):
        self.list = sorted(self.list, key=lambda product: str(getattr(product, field).lower()))

    def add_smth(self, element):
        self.list.append(element)

    def search(self, string):
        search_it = Collection()
        string_low = string.lower()
        string_up = string.capitalize()
        for i in self.list:
            for val in i.__dict__.values():
                if string_low in val or string_up in val:
                    search_it.add_smth(i)
                    break
        print(search_it)
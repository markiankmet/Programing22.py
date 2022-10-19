from Car import *
from os.path import exists
import sys


class Collection:
    def __init__(self, file_name):
        self.collection = []
        self.file_name = file_name

    def __str__(self):
        text = ""
        for item in self.collection:
            text += str(item) + "\n"
        return text

    def add(self):
        file = open(self.file_name, 'a')
        new_car = Car()
        new_car.input_data()
        self.collection.append(new_car)
        file.write("\n"+str(new_car))
        return self

    def write_in_file(self):
        file = open(self.file_name, 'w')
        for item in self.collection:
            file.write(str(item)+"\n")
        return self

    def read_from_file(self):
        if exists(self.file_name):
            file = open(self.file_name, 'r')
            for i, line in enumerate(file):
                data = line.split()
                car = Car(*data)
                self.collection.append(car)
            self.write_in_file()
            file.close()
            return self
        else:
            print(f"{self.file_name} does not exists")
            sys.exit()

    def remove(self, id_):
        for i in range(len(self.collection)):
            if str(self.collection[i].get_id) == str(id_):
                self.collection.pop(i)
                break
        self.write_in_file()

    def search(self, x):
        contain = False
        for i in self.collection:
            if i.is_found(x):
                print(i)
                contain = True
        if not contain:
            print('Nothing found!')

    def search_id(self, id_of_obj):
        is_found = False
        for container_object in self.collection:
            for key, value in container_object.__dict__.items():
                if key == "id_" and str(value) == str(id_of_obj):
                    is_found = True
                    return container_object
        if not is_found:
            raise ValueError(f"No object with id:'{id_of_obj}'")

    def edit_by_id(self):
        id_of_edited_obj = input("ID of element you want edit: ")
        container_object = self.search_id(id_of_edited_obj)
        if container_object:
            container_object.edit()
        self.write_in_file()

    def sort(self, parameter):
        sorted_list = sorted(self.collection, key=lambda x: x.__getitem__(parameter).lower())
        self.collection = sorted_list

from Library import *


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
        new_library = Library()
        new_library.input_data()
        self.collection.append(new_library)
        file.write("\n"+str(new_library))
        return self

    def write_in_file(self):
        file = open(self.file_name, 'w')
        for item in self.collection:
            file.write(str(item)+"\n")
        return self

    def read_from_file(self):
        file = open(self.file_name, 'r')
        for i, line in enumerate(file):
            data = line.split()
            car = Library(*data)
            self.collection.append(car)
        self.write_in_file()
        file.close()
        return self

    # def top(self):
    #     for item in self.collection:
    #         text += str(item) + "\n"
    #     return text

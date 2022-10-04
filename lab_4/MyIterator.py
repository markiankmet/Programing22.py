from check_functions import *
from random import randint as rand


class Iterator:
    def __iter__(self):
        return self

    def __init__(self, size):
        self.size = size
        self.element = 0

    def __next__(self):
        if self.element < self.size:
            self.element += 1
        for i in range(self.size):
            self.size -= 1
            return check_if_numeric(input('Enter a value: '))
        else:
            raise StopIteration


def my_generator(a, b, size):
    if a < b:
        while size != 0:
            size -= 1
            yield rand(a, b)
    else:
        print('b should be bigger than a')

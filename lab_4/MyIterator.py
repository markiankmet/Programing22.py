from random import randint
from MyList import *


class MyIterator:
    def __init__(self, size, a, b):
        self.size = size
        self.a = a
        self.b = b

    def __iter__(self):
        return self

    def __next__(self):
        if self.size == 0:
            raise StopIteration
        self.size -= 1
        return randint(self.a, self.b)


def my_generator(a, b, size):
    if a < b:
        for _ in range(size):
            yield randint(a, b)
    elif a > b:
        for _ in range(size):
            yield randint(b, a)

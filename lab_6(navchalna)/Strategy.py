import abc
from MyList import *


class Strategy(LinkedList):
    @abc.abstractmethod
    def generate_data(self, data: LinkedList, pos, param):
        pass


class StrategyA(Strategy):
    def generate_data(self, data: LinkedList, pos, n):
        a = check_if_integer(input('Enter a: '))
        b = check_if_integer(input('Enter b: '))
        if a > b:
            a, b = b, a
        if data.length() == 0:
            pos = 0
            data.generate_by_iterator(n, a, b, pos)
        else:
            data.generate_by_iterator(n, a, b, pos)


class StrategyB(Strategy):
    def generate_data(self, data: LinkedList, pos, filename):
        with open(filename, "r") as readfile:
            if data.length() == 0:
                for elem in readfile:
                    for x in elem.split():
                        a = int(x)
                        data.append(a)
            else:
                for elem in readfile:
                    for x in elem.split():
                        a = int(x)
                        data.insert(pos, a)
                        pos += 1
                readfile.close()


class Context:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    @property
    def strategy_(self):
        return self.strategy

    @strategy_.setter
    def strategy_(self, strategy: Strategy):
        self.strategy = strategy

    def generate(self, list_, index, n):
        self.strategy.generate_data(list_, index, n)

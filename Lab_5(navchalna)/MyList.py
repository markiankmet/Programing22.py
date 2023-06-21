from check_functions import *
from MyIterator import *


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        size = 0
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            size += 1
        return size

    def output_list(self):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            print(cur.data, end=' ')
        print()

    def input_keyboard(self, size):
        for i in range(size):
            self.append(check_if_integer(input('Enter a value: ')))

    def generate_random(self, size):
        a = check_if_integer(input('Enter a: '))
        b = check_if_integer(input('Enter b: '))
        if a < b:
            for i in range(size):
                self.append(randint(a, b))
        elif a > b:
            for i in range(size):
                self.append(randint(b, a))

    def insert(self, index, data):
        new_node = Node(data)
        if index >= self.length() + 1 or index < 0:
            print('Position out of range!')
            return
        cur = self.head
        for i in range(index):
            if cur is not None:
                cur = cur.next
        if cur is not None:
            new_node.next = cur.next
            cur.next = new_node

    def erase(self, index):
        if index >= self.length():
            print('Index out of range!')
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1

    def find_max(self):
        max_value = self.head.next.data
        max_idx = 0
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            if max_value < cur.data:
                max_value = cur.data
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            if cur.data == max_value:
                break
            if max_value > cur.data:
                max_idx += 1
        return max_value, max_idx

    def is_negative(self):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            if cur.data > 0:
                return False
        return True

    def delete_in_range(self, a, b):
        if a > b:
            a, b = b, a
        n = b - a
        k = 0
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            if k == a:
                for i in range(n):
                    self.erase(k)
            k += 1

    def made_kub(self, max_index):
        cur = self.head
        for i in range(max_index):
            cur = cur.next
            cur.data = cur.data**3

    def generate_by_iterator(self, size, a, b, index):
        if a > b:
            my_class = MyIterator(size, b, a)
        elif a < b:
            my_class = MyIterator(size, a, b)
        for i in my_class:
            self.insert(index, i)

    def generate_elements(self, size, a, b):
        generator = my_generator(a, b, size)
        cur = Node(next(generator))
        self.head.next = cur
        for el in generator:
            self.append(el)

import random


def check_position(arg, n):
    if arg < 1 or arg > n - 1:
        print("Invalid position!")
        return True
    return False


def check_if_integer(user_input):
    it_is = False
    while not it_is:
        try:
            integer = int(user_input)
            it_is = True
            return integer
        except ValueError:
            user_input = input('Valid value, Try again: ')
            it_is = False


def check_if_numeric(x):
    check_x = False
    while not check_x:
        if x.isnumeric():
            check_x = True
            x = int(x)
            return x
        else:
            x = input('Invalid Error! Try again: ')


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_value = None


class LinkedList:
    def __init__(self):
        self.head = None

    def list_print(self):
        print_value = self.head
        output = ''
        while print_value is not None:
            output += str(print_value.value) + ' '
            print_value = print_value.next_value
        print(output)

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def clear(self):
        current = self.head
        if current is None:
            print('Empty list')
        while current:
            self.head = current.next_value
            current = self.head

    def append_value(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        else:
            instant = self.head
            while instant.next_value is not None:
                instant = instant.next_value
            instant.next_value = new_node

    def insert_value(self, item, position):
        if position == 1:
            new_node = Node(item)
            new_node.next_value = self.head
            self.head = new_node
            return
        n = self.head
        i = 0
        while i < position - 1 and n is not None:
            n = n.next_value
            i += 1
        if n is None:
            print('Invalid index!')
        else:
            new_node = Node(item)
            new_node.next_value = n.next_value
            n.next_value = new_node

    def delete_element(self, position):
        if self.is_empty():
            print('Empty list!')
        current = self.head
        if position == 1:
            self.head = current.next_value
            current = None
            return
        for i in range(position - 2):
            current = current.next_value
            if current is None:
                break
        if current is None:
            return
        if current.next_value is None:
            return
        next_val = current.next_value.next_value
        current.next_value = None
        current.next_value = next_val

    def input_list(self, n):
        if n != 0:
            print("Input list:")
            for i in range(n):
                self.append_value(check_if_integer(input('Enter a value: ')))
        else:
            print('List is empty')

    def generate_random_list(self, size_of_list, a, b):
        if b > a:
            for i in range(size_of_list):
                self.append_value(random.randint(a, b))
        else:
            print('b must be bigger than a')

    def find_max(self):
        node = self.head
        max_value = self.head.value
        while self.head is not None:
            if max_value < self.head.value:
                max_value = self.head.value
            self.head = self.head.next_value
        i = 0
        while node is not None:
            if node.value == max_value:
                break
            if max_value > node.value:
                i += 1
            node = node.next_value
        return max_value, i

    def made_kub(self):
        list_ = []
        node = self.head
        while node is not None:
            list_.append(node.value)
            node = node.next_value
        return list_

    def is_negative(self):
        is_negative = True
        while self.head is not None:
            if self.head.value > 0:
                return False
            self.head = self.head.next_value
        return True

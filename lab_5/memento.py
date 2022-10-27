from Collection_cars import *


class Memento():
    def __init__(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state


class Originator:
    def __init__(self):
        self.record = Collection()

    def set_record(self, record):
        self.record = record

    def get_record(self):
        return self.record

    def save(self):
        return Memento(self.record.make_copy())

    def restore(self, mem_obj):
        self.record = mem_obj.get_state()


class CareTaker:

    def __init__(self):
        self.states = []
        self.index = -1

    def memento(self, mem_obj):
        if len(self.states) >= 6:
            self.states.pop(0)
            self.states.append(mem_obj)
            self.index = len(self.states) - 1
        else:
            self.states.append(mem_obj)
            self.index = len(self.states) - 1

    def undo(self):
        if self.index == 0:
            print("You can't undo")
            return self.states[0]
        else:
            self.index = self.index - 1
            return self.states[self.index]

    def redo(self):
        if self.index >= len(self.states) - 1:
            print("You can't redo")
            self.index = len(self.states) - 1
            return self.states[self.index]
        else:
            self.index = self.index + 1
            return self.states[self.index]


def write_changes_after(originator, path):
    file = open(path, 'w')
    for item in originator.get_record():
        file.write(str(item) + "\n")
    for i in originator.get_record():
        print(i)


def memento(originator, caretaker, collection):
    originator.set_record(collection)
    caretaker.memento(originator.save())

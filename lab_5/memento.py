from Collection_cars import *


class Memento:
    def __init__(self, state):
        self.state = state


class CareTaker:
    def __init__(self, originator: Collection):
        self.originator = originator
        self.undo_mementos: list[Memento] = []
        self.redo_mementos: list[Memento] = []

    def create(self):
        self.undo_mementos.append(Memento(self.originator.make_copy()))
        self.redo_mementos.clear()

    def undo(self):
        if len(self.undo_mementos) == 0:
            print("Can't undo")
        else:
            self.redo_mementos.append(Memento(self.originator.make_copy()))
            self.originator.set_memento(self.undo_mementos.pop())

    def redo(self):
        if len(self.redo_mementos) == 0:
            print("Can't redo")
        else:
            self.undo_mementos.append(Memento(self.originator.make_copy()))
            self.originator.set_memento(self.redo_mementos.pop())

from observer import Observer


class Event:
    def __init__(self, name, before_changes, after_changes, pos1=None, pos2=None, do=True):
        self.name = name
        self.before_changes = before_changes
        self.after_changes = after_changes
        self.pos1 = pos1
        self.pos2 = pos2
        if do:
            self.is_event()

    def is_event(self):
        for observer in Observer.observers_:
            if self.name in observer.events:
                observer.events[self.name](self)

    def __str__(self):
        if self.pos1 is None and self.pos2 is None:
            return f"Event({self.name}, (old list: {self.before_changes}, new list: {self.after_changes}))"
        elif self.pos2 is not None:
            return f"Event({self.name}, (old list: {self.before_changes}, new list: {self.after_changes}," \
                   f" from position:{self.pos1}, to:{self.pos2} ))"
        else:
            return f"Event({self.name}, (old list: {self.before_changes}," \
                   f" new list: {self.after_changes}, on/from position:{self.pos1})"

from logger import Logger


class Observer:
    observers_ = []

    def __init__(self):
        self.observers_.append(self)
        self.events = dict()

    def observe(self, event_name, callback=Logger.write_into_file):
        self.events[event_name] = callback

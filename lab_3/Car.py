from Validation_fields import *


class Car:
    def __init__(self, **arguments):
        for (cont, default) in arguments.items():
            setattr(self, cont, arguments.get(cont, default))

    def __str__(self):
        text = ""
        for key, value in vars(self).items():
            text += str(key) + ": " + str(value) + "\n"
        return text

    def validate_car(self):
        Validation.check_brand(self.brand)

    def get_id(self):
        return self.ID

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_registration_number(self):
        return self.registration_number

    def get_last_repaired_at(self):
        return self.last_repaired_at

    def get_bought_at(self):
        return self.bought_at

    def get_bought_at(self):
        return self.bought_at

    def get_car_mileage(self):
        return self.car_mileage

    def set_id(self, value):
        self.ID = value

    def set_brand(self, value):
        self.brand = value

    def set_model(self, value):
        self.model = value

    def set_registration_number(self, value):
        self.registration_number = value

    def set_last_repaired_at(self, value):
        self.last_repaired_at = value

    def set_bought_at(self, value):
        self.bought_at = value

    def set_car_mileage(self, value):
        self.car_mileage = value

    def input_car(*arguments):
        d = dict((cont, input(cont + ": ")) for cont in arguments)
        return d

    def validate_car(self):
        Validation.check_positive_number(self.ID)
        Validation.check_brand(self.brand)
        Validation.check_model(self.model)
        Validation.check_registration_number(self.registration_number)
        Validation.check_date(self.last_repaired_at)
        Validation.check_date(self.bought_at)
        Validation.compare_date(self.last_repaired_at, self.bought_at)

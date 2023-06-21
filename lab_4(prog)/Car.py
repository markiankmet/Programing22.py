from Validation import *


class Car:
    def __init__(self, id_="9", brand='Audi', model='R7', registration_number='BC2302KA', last_repaired_at='2022-10-10',
                 bought_at='2021-10-10', car_mileage='21000'):
        self.set_id(id_)
        self.set_brand(brand)
        self.set_model(model)
        self.set_registration_number(registration_number)
        self.set_last_repaired_at(last_repaired_at)
        self.set_bought_at(bought_at, self.last_repaired_at)
        self.set_car_mileage(car_mileage)

    def __str__(self):
        # text = ""
        # for attr, value in self.__dict__.items():
        #     text += value + " "
        # return text
        return f"{self.id_} {self.brand} {self.model} {self.registration_number} " \
               f"{self.last_repaired_at.strftime('%Y-%m-%d')} " \
               f"{self.bought_at.strftime('%Y-%m-%d')} {self.car_mileage}"

    @property
    def get_id(self):
        return self.id_

    @property
    def get_brand(self):
        return self.brand

    @property
    def get_model(self):
        return self.model

    @property
    def get_registration_number(self):
        return self.registration_number

    @property
    def get_last_repaired_at(self):
        return self.last_repaired_at

    @property
    def get_bought_at(self):
        return self.bought_at

    @property
    def get_car_mileage(self):
        return self.car_mileage

    @check_if_numeric
    @check_id
    def set_id(self, new_id):
        self.id_ = new_id

    @check_brand
    def set_brand(self, new_brand):
        self.brand = new_brand

    @check_model
    def set_model(self, new_model):
        self.model = new_model

    @check_registration_number
    def set_registration_number(self, new_number):
        self.registration_number = new_number

    @check_last_repaired_at
    def set_last_repaired_at(self, new_last_repaired):
        self.last_repaired_at = new_last_repaired

    @check_bought_at_date
    @check_last_repaired_at
    def set_bought_at(self, new_bought_at):
        self.bought_at = new_bought_at

    @check_if_numeric
    @check_car_mileage
    def set_car_mileage(self, new_mileage):
        self.car_mileage = new_mileage

    def input_data(self):
        setters = filter(lambda x: x.startswith('set'), list(Car.__dict__.keys()))
        for item in setters:
            x = getattr(self, item)
            print(f"Input {x.__name__[4:]}: ")
            _input = input()
            x(_input)

    def is_found(self, search_object):
        all_parameters = (str(self)).split()
        for i in all_parameters:
            if str(search_object) in i:
                return True
        return False

    def edit(self):
        key = input("Which field you want edit: ")
        value = input(f"Input new {key} value: ")
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]

from Validation import *


class Car:
    def __init__(self, id_="1", brand='b', model='b', registration_number='BC1111KA', last_repaired_at='2022-10-10',
                 bought_at='2021-10-10', car_mileage='2'):
        self.id_ = check_id(id_)
        self.brand = check_brand(brand)
        self.model = check_model(model)
        self.registration_number = check_registration_number(registration_number)
        self.last_repaired_at = check_last_repaired_date(last_repaired_at)
        self.bought_at = check_bought_at_date(bought_at, self.last_repaired_at)
        self.car_mileage = check_car_mileage(car_mileage)

    def __str__(self):
        return f"{self.id_} {self.brand} {self.model} {self.registration_number} {self.last_repaired_at} " \
               f"{self.bought_at} {self.car_mileage}"

    @property
    def get_id(self):
        return self.id_

    @get_id.setter
    def get_id(self, new_id):
        self.id_ = new_id

    @property
    def get_brand(self):
        return self.brand

    @get_brand.setter
    def get_brand(self, new_brand):
        self.brand = new_brand

    @property
    def get_model(self):
        return self.model

    @get_model.setter
    def get_model(self, new_model):
        self.model = new_model

    @property
    def get_registration_number(self):
        return self.registration_number

    @get_registration_number.setter
    def get_registration_number(self, new_number):
        self.registration_number = new_number

    @property
    def get_last_repaired_at(self):
        return self.last_repaired_at

    @get_last_repaired_at.setter
    def get_last_repaired_at(self, new_last_repaired):
        self.last_repaired_at = new_last_repaired

    @property
    def get_bought_at(self):
        return self.bought_at

    @get_bought_at.setter
    def get_bought_at(self, new_bought_at):
        self.bought_at = new_bought_at

    @property
    def get_car_mileage(self):
        return self.car_mileage

    @get_car_mileage.setter
    def get_car_mileage(self, new_mileage):
        self.car_mileage = new_mileage

    def input_data(self):
        self.id_ = check_id(input("Enter id: "))
        self.brand = check_brand(input("Enter brand: "))
        self.model = check_model(input("Enter model: "))
        self.registration_number = check_registration_number(input("Enter registration_number: "))
        self.last_repaired_at = check_last_repaired_date(input("Enter last_repaired_date: "))
        self.bought_at = check_bought_at_date(input("Enter bought_at: "), self.last_repaired_at)
        self.car_mileage = check_car_mileage(input("Enter car_mileage: "))

    def is_found(self, search_object):
        all_parameters = (str(self)).split()
        for i in all_parameters:
            if str(search_object) in i:
                return True
        return False

    def edit(self):
        key = input("Which field you want edit: ")
        value = input(f"Input new {key} value :")
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]

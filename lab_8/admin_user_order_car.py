from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from validation import *


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:MARIK2016@localhost/Last_Test'
app.config['SECRET_KEY'] = 'k54kag94k5l0ad90gj425kgd'
db = SQLAlchemy(app)


class Car(db.Model):
    __tablename__ = "Cars"
    ID = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50))
    model = db.Column(db.String(30))
    registration_number = db.Column(db.String(8))
    last_repaired_at = db.Column(db.String(15))
    bought_at = db.Column(db.String(15))
    car_mileage = db.Column(db.Integer)

    def __init__(self, ID=0, brand='b', model='b', registration_number='BC1111KA', last_repaired_at='2022-10-10',
                 bought_at='2021-10-10', car_mileage=2):
        self.set_ID(ID)
        self.set_brand(brand)
        self.set_model(model)
        self.set_registration_number(registration_number)
        self.set_last_repaired_at(last_repaired_at)
        self.set_bought_at(bought_at)
        self.set_car_mileage(car_mileage)

    def to_file(self):
        return {
            "ID": str(self.get_ID),
            "brand": str(self.get_brand),
            "model": str(self.get_model),
            "registration_number": str(self.get_registration_number),
            "last_repaired_at": self.get_last_repaired_at,
            "bought_at": self.get_bought_at,
            "car_mileage": str(self.get_car_mileage)
        }

    def __str__(self):
        return f"{self.ID}, {self.brand}, {self.model}, {self.registration_number}, " + \
               f"{self.last_repaired_at}, {self.bought_at}, {self.car_mileage}"

    @check_if_numeric
    def set_ID(self, ID):
        self.ID = ID

    @check_brand
    def set_brand(self, brand):
        self.brand = brand

    @check_model
    def set_model(self, model):
        self.model = model

    @check_registration_number
    def set_registration_number(self, registration_number):
        self.registration_number = registration_number

    @validation_date
    def set_last_repaired_at(self, last_repaired_at):
        self.last_repaired_at = last_repaired_at

    @validation_date_after
    @validation_date
    def set_bought_at(self, bought_at):
        self.bought_at = bought_at

    @check_if_numeric
    def set_car_mileage(self, car_mileage):
        self.car_mileage = car_mileage

    @property
    def get_ID(self):
        return self.ID

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

    def elem_search(self, value):
        for element in self.__dict__.values():
            if value in str(element):
                return True
        return False

    @staticmethod
    def get_attributes():
        attributes = []
        for attr, values in vars(Car).items():
            if not attr.startswith("_") and not attr.startswith("set") and not attr.startswith(
                    "get") and not attr.startswith("elem") and not attr.startswith("__") and not attr.startswith("to"):
                attributes.append(attr)
        return attributes


class User(db.Model):
    __tablename__ = "User"
    ID = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(30))
    email = db.Column(db.String(30))
    password = db.Column(db.String(500))
    is_admin = db.Column(db.Boolean, default=0)

    def __init__(self, ID=0, first_name='b', last_name='BC1111KA', email='2022-10-10',
                 password='2021-10-10', is_admin=False):
        self.set_ID(ID)
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_email(email)
        self.set_password(password)
        self.is_admin = is_admin

    def to_file(self):
        return {
            "ID": str(self.get_ID),
            "first_name": str(self.first_name),
            "last_name": str(self.last_name),
            "email": str(self.email),
            "password": self.password,
        }

    def __str__(self):
        return f"{self.ID}, {self.first_name}, {self.last_name}, {self.email}, " + \
               f"{self.password}"

    @check_if_numeric
    def set_ID(self, ID):
        self.ID = ID

    @check_name
    def set_first_name(self, first_name):
        self.first_name = first_name

    @check_name
    def set_last_name(self, last_name):
        self.last_name = last_name

    @check_email
    def set_email(self, email):
        self.email = email

    @check_password
    def set_password(self, password):
        self.password = password

    @property
    def get_ID(self):
        return self.ID

    @property
    def get_first_name(self):
        return self.first_name

    @property
    def get_last_name(self):
        return self.last_name

    @property
    def get_email(self):
        return self.email

    @property
    def get_password(self):
        return self.password

    def elem_search(self, value):
        for element in self.__dict__.values():
            if value in str(element):
                return True
        return False

    @staticmethod
    def get_attributes():
        attributes = []
        for attr, values in vars(User).items():
            if not attr.startswith("_") and not attr.startswith("set") and not attr.startswith(
                    "get") and not attr.startswith("elem") and not attr.startswith("__") and not attr.startswith("to")\
                    and not attr.startswith("is"):
                attributes.append(attr)
        return attributes


class Order(db.Model):
    __tablename__ = "Order"
    item_ID = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50))
    amount = db.Column(db.Integer)

    def __init__(self, item_ID=0, model='b', amount=2):
        self.set_item_ID(item_ID)
        self.set_model(model)
        self.set_amount(amount)

    def to_file(self):
        return {
            "item_ID": str(self.get_item_ID),
            "model": str(self.get_model),
            "amount": str(self.get_amount)
        }

    def __str__(self):
        return f"{self.item_ID}, {self.model}, {self.amount}"

    @check_if_numeric
    def set_item_ID(self, item_ID):
        self.item_ID = item_ID

    @check_model
    def set_model(self, model):
        self.model = model

    @check_if_numeric
    def set_amount(self, amount):
        self.amount = amount

    @property
    def get_item_ID(self):
        return self.item_ID

    @property
    def get_model(self):
        return self.model

    @property
    def get_amount(self):
        return self.amount

    def elem_search(self, value):
        for element in self.__dict__.values():
            if value in str(element):
                return True
        return False

    @staticmethod
    def get_attributes():
        attributes = []
        for attr, values in vars(Order).items():
            if not attr.startswith("_") and not attr.startswith("set") and not attr.startswith(
                    "get") and not attr.startswith("elem") and not attr.startswith("__") and not attr.startswith("to"):
                attributes.append(attr)
        return attributes

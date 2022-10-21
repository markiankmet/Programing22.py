import datetime
from functools import wraps
import os
import sys
LIMIT_M = 1000000
menu_fields = {1: "id_", 2: "brand", 3: "model", 4: "registration_number",
               5: "last_repaired_at", 6: "bought_at", 7: "car_mileage"}


def check_id(func):
    @wraps(func)
    def wrapper(*args):
        if int(args[1]) >= 0:
            return func(args[0], args[1])
        else:
            return wrapper(args[0], input(f"{args[1]} value must be positive! Try again: "))
    return wrapper


def check_if_numeric(func):
    @wraps(func)
    def wrapper(*args):
        if not isinstance(args[1], int):
            try:
                return func(args[0], args[1])
            except:
                return wrapper(args[0], input(f"Value {args[1]} must be an integer! Try again: "))
        else:
            return func(args[0], args[1])
    return wrapper


def check_brand(func):
    @wraps(func)
    def wrapper(*args):
        if not all(x.isalpha() or x == '-' for x in args[1]):
            return wrapper(args[0], input(f"{args[1]} must consist of letters! Try again: "))
        else:
            return func(*args)
    return wrapper


def check_model(func):
    @wraps(func)
    def wrapper(*args):
        if not all(x.isalpha() or x == '-' or x.isnumeric() for x in args[1]):
            return wrapper(args[0], input(f"{args[1]} must consist of letters! Try again: "))
        else:
            return func(*args)
    return wrapper


def check_registration_number(func):
    @wraps(func)
    def wrapper(*args):
        letters = (args[1])[:2] + (args[1])[-1:-3:-1]
        numbers = (args[1])[2:6]
        if not all(x.isupper() and x.isalpha() for x in letters) and all(x.isnumeric() for x in numbers):
            return wrapper(args[0], input(f"{args[1]} Invalid registration number! Try again: "))
        return func(*args)
    return wrapper


def check_last_repaired_at(func):
    @wraps(func)
    def wrapper(*args):
        if isinstance(args[1], str):
            try:
                return func(args[0], datetime.datetime.strptime(args[1], '%Y-%m-%d'))
            except:
                pass
        else:
            return wrapper(args[0], input(f'Valid format of date {args[1]}! Try again: '))
    return wrapper


def check_bought_at_date(func):
    @wraps(func)
    def wrapper(*args):
        if str(datetime.datetime.strptime(args[1], '%Y-%m-%d')) < str(args[0].last_repaired_at):
            return func(*args)
        else:
            return wrapper(args[0], input(f"{args[1]} must be earlier than last_repaired! Try again: "))
    return wrapper


def check_car_mileage(func):
    @wraps(func)
    def wrapper(*args):
        if int(args[1]) >= 0:
            return func(args[0], args[1])
        else:
            return wrapper(args[0], input(f"{args[1]} car mileage must be positive! Try again: "))
    return wrapper


def input_field(list_, field=None):
    if field is None:
        field = f"get_{input('Enter by what to sort: ')}"
    if field not in list_:
        print(f"This field doesn't exist! Try again!")
        return input_field(list_)
    return field


def input_file(fl):
    while True:
        if os.path.isfile(fl) and fl.endswith(".txt"):
            return fl
        else:
            fl = input("File name is incorrect. Try again: ")


def check_if_numeric_(x):
    check_x = False
    while not check_x:
        if x.isnumeric():
            check_x = True
            x = int(x)
            return x
        else:
            x = input('Invalid Error! Try again: ')

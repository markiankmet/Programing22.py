import datetime
LIMIT_M = 1000000
menu_fields = {1: "id_", 2: "brand", 3: "model", 4: "registration_number",
               5: "last_repaired_at", 6: "bought_at", 7: "car_mileage"}


def check_id(id_):
    while True:
        try:
            if int(id_) < 0:
                print('Valid id, must be positive: ', id_)
                id_ = input('Enter new id: ')
                continue
            elif isinstance(id_, str):
                return id_
        except ValueError:
            print('Valid id, must be integer: ', id_)
            id_ = input('Enter new id: ')
            continue


def check_brand(brand):
    while True:
        if len(brand) == 0 or all(x.isspace() for x in brand):
            print('Valid brand, cannot be a space!')
            brand = input('Enter a new brand: ')
            continue
        if all(x.isalpha() or '-' for x in brand):
            return brand
        else:
            print('Valid brand, must be str: ', brand)
            brand = input('Enter a new brand: ')
            continue


def check_model(model):
    while True:
        if all(x.isspace() for x in model):
            print('Valid brand, cannot be a space!')
            model = input('Enter a new brand: ')
            continue
        if all(x.isalpha() or '-' or x.isnumeric() for x in model):
            return model
        else:
            print('Valid model, must be str: ', model)
            brand = input('Enter a new model: ')
            continue


def check_registration_number(registration_number):
    while True:
        letters = registration_number[:2] + registration_number[-1:-3:-1]
        numbers = registration_number[2:6]
        if len(registration_number) == 8:
            if all(x.isupper() and x.isalpha() for x in letters) and all(x.isnumeric() for x in numbers):
                return registration_number
            else:
                print('Valid registration_number: ', registration_number)
                registration_number = input('Enter a new registration_number: ')
                continue
        else:
            print('Valid registration_number, size must be 8 : ', registration_number)
            registration_number = input('Enter a new registration_number: ')
            continue


def check_last_repaired_date(date):
    while True:
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
            return date
        except ValueError:
            print('Valid input date: ', date)
            date = input('Enter new date: ')
            continue


def check_bought_at_date(bought_at, repaired_at):
    while True:
        try:
            datetime.datetime.strptime(bought_at, '%Y-%m-%d')
        except ValueError:
            print('Valid input date: ', bought_at)
            bought_at = input('Enter new date: ')
            continue
        if bought_at < repaired_at:
            return bought_at
        else:
            print('Bought date must be earlier than last repaired date!')
            bought_at = input('Enter a new bought_at date: ')
            continue


def check_car_mileage(car_mileage):
    while True:
        try:
            if car_mileage.isnumeric() and int(car_mileage) < LIMIT_M:
                return car_mileage
            elif int(car_mileage) < 0:
                print('Valid car_mileage, must be positive: ', car_mileage)
                car_mileage = input('Enter new car_mileage: ')
                continue
            else:
                print('Car mileage must be lower than LIMIT_M')
                car_mileage = input('Enter new car_mileage: ')
                continue
        except ValueError:
            print('Valid car_mileage, must be integer: ', car_mileage)
            car_mileage = input('Enter new car_mileage: ')
            continue


def input_field(list_, field=None):
    if field is None:
        field = f"get_{input('Enter by what to sort: ')}"
    if field not in list_:
        print(f"This field doesn't exist! Try again!")
        return input_field(list_)
    return field


def check_if_numeric(x):
    check_x = False
    while not check_x:
        if x.isnumeric():
            check_x = True
            x = int(x)
            return x
        else:
            x = input('Invalid Error! Try again: ')

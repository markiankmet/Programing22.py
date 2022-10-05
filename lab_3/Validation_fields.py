import datetime
import os
LIMIT = 1000000


class Validation:
    def __init__(self):
        pass

    def check_brand(brand):
        if all(x.isalpha() or x.isspace() for x in brand):
            return brand
        else:
            print("Valid input brand: ", brand)

    def check_model(model):
        if all(x.isalpha() or x.isdigit() or x.isspace() for x in model):
            return model
        else:
            print("Valid model input!")

    def check_date(date):
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
            return date
        except ValueError:
            print("Valid input date : ", date)

    def compare_date(last_repaired_at, bought_at):
        if bought_at < last_repaired_at:
            return
        else:
            print("Bought date must be earlier than last repaired date")

    def check_registration_number(registration_number):
        letters = registration_number[:2] + registration_number[-1:-3:-1]
        numbers = registration_number[2:6]
        if len(registration_number) == 8:
            if all(x.isupper() and x.isalpha() for x in letters) and all(x.isdigit() for x in numbers):
                return registration_number
            else:
                print("Valid input registration number: ", registration_number)

    def input_file(file_):
        while True:
            path = input(file_)
            if os.path.isfile(path) and path.endswith(".txt"):
                return path
            else:
                print("Valid file name!")
                continue

    def check_file(path):
        if os.path.isfile(path) and path.endswith(".txt"):
            return path
        else:
            print("File can't be found")
            return Validation.input_file("Input correct file name: ")

    def check_positive_number(value):
        while True:
            try:
                if 0 < int(value) < LIMIT:
                    return value
                elif int(value) <= 0:
                    print("Value must be positive : ", value)
                    break
            except ValueError:
                print("Car_mileage must be a number!")

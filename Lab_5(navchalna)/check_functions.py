from Strategy import *
import os


def check_if_integer(user_input):
    while True:
        try:
            integer = int(user_input)
            return integer
        except ValueError:
            user_input = input('Valid value, Try again: ')
            continue


def check_if_numeric(x):
    while True:
        if x.isnumeric():
            x = int(x)
            return x
        else:
            x = input('Invalid Error! Try again: ')
            continue


def validate_file(end=".txt"):
    while True:
        try:
            filename = input("Enter file name: ")
            if not os.path.isfile(filename) and not filename.endswith(end):
                print("There's no such" + filename + " file")
                continue
            break
        except ValueError:
            print("Incorrect symbols")
    return filename


def validate_generation(context):
    if context is None:
        raise UnboundLocalError("You need to choose type of generation and after do another options.")
    return context

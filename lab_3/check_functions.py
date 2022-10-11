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
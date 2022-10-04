def check_position(arg, n):
    if arg < 1 or arg > n - 1:
        print("Invalid position!")
        return True
    return False


def check_if_integer(user_input):
    it_is = False
    while not it_is:
        try:
            integer = int(user_input)
            it_is = True
            return integer
        except ValueError:
            user_input = input('Valid value, Try again: ')
            it_is = False


def check_if_numeric(x):
    check_x = False
    while not check_x:
        if x.isnumeric():
            check_x = True
            x = int(x)
            return x
        else:
            x = input('Invalid Error! Try again: ')

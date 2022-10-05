def check_if_numeric(x):
    check_x = False
    while not check_x:
        if x.isnumeric():
            check_x = True
            x = int(x)
            return x
        else:
            x = input('Invalid Error! Try again: ')


def check_id():
    while True:
        number = check_if_numeric(input("Input id: "))
        if number <= 0:
            print("ID must be positive!")
            continue
        return number


def input_value():
    value = input("Input value: ")
    return value


def input_field():
    while True:
        try:
            print("Choose by what to sort:\n"
                  "1 - id \n"
                  "2 - brand\n"
                  "3 - model\n"
                  "4 - registration_number\n"
                  "5 - last_repaired_at\n"
                  "6 - bought_at\n"
                  "7 - car_mileage\n")
            what_chosen = int(input(""))
            if what_chosen == 1:
                return 'id'
            elif what_chosen == 2:
                return 'brand'
            elif what_chosen == 3:
                return 'model'
            elif what_chosen == 4:
                return 'registration_number'
            elif what_chosen == 5:
                return 'last_repaired_at'
            elif what_chosen == 6:
                return 'bought_at'
            elif what_chosen == 7:
                return 'car_mileage'
            else:
                print("Enter right option")
                continue
        except ValueError:
            print("Something went wrong, enter an number you want:")

from random import randint
menu_options = {1: 'Enter massive', 2: 'Generate massive in a certain range', 3: 'Exit'}


def check_if_numeric(x):
    check_x = False
    while not check_x:  # check if x is number
        if x.isnumeric():
            check_x = True
            x = int(x)
            return x
        else:
            x = input('Invalid Error! Try again: ')


def input_massive():
    n = check_if_numeric(input('Enter length of massive: '))
    massive = []
    if n != 0:
        print(f'Enter {n} values: ')
        for i in range(n):
            massive.append(check_if_numeric(input()))
    return massive


def generate_random_massive():
    n = check_if_numeric(input('Enter length of massive: '))
    random_massive = []
    if n != 0:
        a, b = check_if_numeric(input('Enter a: ')), check_if_numeric(input('Enter b: '))
        for i in range(n):
            random_massive.append(randint(a, b+1))
    return random_massive


def merge_sort(arr):
    number_operation = 0
    if len(arr) > 1:
        mid = len(arr) // 2     # Finding the pivot of the array
        left, right = arr[:mid], arr[mid:]  # Dividing the array elements  into 2 halves
        merge_sort(left)   # Sorting the first half
        merge_sort(right)   # Sorting the second half
        i = j = k = 0
        while i < len(left) and j < len(right):    # Copy data to temp arrays L[] and R[]
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
                number_operation += 1
            else:
                arr[k] = right[j]
                j += 1
                number_operation += 1
            k += 1
            number_operation += 1
        while i < len(left):   # Checking if any element was left
            arr[k] = left[i]
            i += 1
            k += 1
            number_operation += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            number_operation += 1
        return arr, number_operation


def question_sort(massive):
    if len(massive) != 0:
        s = check_if_numeric(input('Sort massive?(1--Yes or 2--No): '))
        if s == 1:
            result, number_of_iterations = merge_sort(massive)
            print(f'Sorted array: {massive}, number of iterations: {number_of_iterations} ')
        elif s == 2:
            print(massive)
        else:
            print('Enter number 1 or 2')
    else:
        print('Massive is empty')


def print_menu():
    for key in menu_options.keys():
        print(key, menu_options[key], sep='--')


while True:
    print_menu()
    option = check_if_numeric(input('Enter your choice: '))
    if option == 1:
        res = input_massive()
        question_sort(res)
    elif option == 2:
        res = generate_random_massive()
        question_sort(res)
    elif option == 3:
        print('Good luck, Bye!')
        exit()
    else:
        print('Invalid option. Please enter a number in range 1-3')

def number_ways_to_cut_tree():   # function to count number of ways to cut trees
    check_n = False
    while not check_n:  # check if n is number
        n = (input('Enter number of trees: '))
        if n.isnumeric():
            check_n = True
            n = int(n)
        else:
            print('Invalid Error! Try again!')
    check_m = False
    while not check_m:  # check if m is number
        m = input('Enter number of trees that should remain: ')
        if m.isnumeric():
            check_m = True
            m = int(m)
        else:
            print('Invalid Error! Try again!')
    if n > 1000 or n < 0 or m > 1000 or m < 0:
        print('Invalid value(0 > n,m > 1000)')
        return
    elif m > n:  # check if m bigger than n
        print('Invalid value(m > n)')
        return
    else:
        res = 0
        if m == 0:
            res = 1  # if 0 tree remain it's one way
        elif m == 1:
            res = n  # if 1 tree remain than n ways to cut down
        else:
            distance = int((n - 1) / (m - 1))  # distance between trees
            for i in range(1, distance + 1):
                res += n - (m - 1) * i
        return res


result = number_ways_to_cut_tree()
print(f'Result = {result}.')


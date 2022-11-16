from functools import wraps
import datetime as dt


class ValidationError(Exception):
    pass


def check_if_numeric(func):
    @wraps(func)
    def wrapper(*args):
        if args[1].isnumeric():
            return func(args[0], int(args[1]))
        else:
            raise ValidationError(f'{args[1]} - incorrect int number')
    return wrapper


def check_brand(func):
    @wraps(func)
    def wrapper(*args):
        if len(args[1]) == 0 or all(x.isspace() or x.isnumeric() for x in args[1]):
            raise ValidationError(f'{args[1]} - incorrect brand!')
        if all(x.isalpha() or '-' for x in args[1]):
            return func(args[0], args[1])
        else:
            raise ValidationError(f'{args[1]} - incorrect brand!')
    return wrapper


def check_model(func):
    @wraps(func)
    def wrapper(*args):
        if len(args[1]) == 0 or all(x.isspace() for x in args[1]):
            raise ValidationError(f'{args[1]} - incorrect model!')
        if all(x.isalpha() or '-' or x.isnumeric() for x in args[1]):
            return func(args[0], args[1])
        else:
            raise ValidationError(f'{args[1]} - incorrect model!')
    return wrapper


def check_registration_number(func):
    @wraps(func)
    def wrapper(*args):
        letters = args[1][:2] + args[1][-1:-3:-1]
        numbers = args[1][2:6]
        if len(args[1]) == 8:
            if all(x.isupper() and x.isalpha() for x in letters) and all(x.isnumeric() for x in numbers):
                return func(args[0], args[1])
            else:
                raise ValidationError(f'{args[1]} - incorrect registration_number!')
        else:
            raise ValidationError(f'{args[1]} - incorrect registration_number!')
    return wrapper


def validation_date(func):
    @wraps(func)
    def wrapper(*args):
            try:
                if dt.datetime.strptime(args[1], '%Y-%m-%d'):
                    return func(*args)
            except:
                raise ValidationError(f'{args[1]} - incorrect date')

    return wrapper


def validation_date_after(func):
    @wraps(func)
    def wrapper(*args):
        if args[1] < args[0].last_repaired_at:
            return func(*args)
        else:
            raise ValidationError(f'bought_at date must be earlier than last_repaired_at!')

    return wrapper

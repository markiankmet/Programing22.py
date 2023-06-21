def repeat_if_error(func):
    def wrapper(*args, **kwargs):
        while True:
            try:
                func(*args, **kwargs)
                break
            except Exception as error:
                print('Caught this error: ' + repr(error)+'\nTry again...')
    return wrapper

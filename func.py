def my_decorator(func):
    def wrapper(name):
        x = func(name.upper())
        return x + '!'
    return wrapper

@my_decorator
def hi(name):
    return f'Hi, {name}'

print(hi('rustam'))

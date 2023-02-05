def my_decorator(func):
    def wrapper():
        x = func()
        return x + '!'
    return wrapper

def hi():
    return 'Hi'

f = my_decorator(hi)
print(f())

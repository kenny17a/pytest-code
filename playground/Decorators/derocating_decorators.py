import functools
import time


# def hello():
#     return "hello world"


def decorate(func):
    @functools.wraps(func)
    def wrap(*arg, **kwargs):
        print("I am before the decorator")
        f = func(*arg, **kwargs)
        print("I am after decorator")
        return f

    return wrap


def multiply(a, b):
    return a * b


def performance_counter(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func = f(*args, **kwargs)
        end = time.perf_counter()
        print(f"the function {f.__name__} took {end - start} to run")
        return func

    return wrapper


@decorate
def hello(name):
    return f"Hello {name}"


@decorate
def add(x, y):
    return x + y


@performance_counter
def add(x, y):
    return x + y


# hello = decorate(hello)()
print(hello("Semicolon"))
print(add(2, 3))
print(add.__name__)
# print(add.__doc__)

multiply_by_5 = functools.partial(multiply, 5)
print(multiply_by_5(6))

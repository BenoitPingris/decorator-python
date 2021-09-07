# Function decorator

import time


def timeit(func):
    def handler(*args, **kwargs):
        s = time.perf_counter()
        func(*args, **kwargs)
        e = time.perf_counter()
        print(f"function took {e-s:.3f}s to run.")

    return handler

def timeit_range(n: int):
    def handler(func):
        def _handler(*args, **kwargs):
            mean = 0
            for _ in range(n):
                s = time.perf_counter()
                func(*args, **kwargs)
                e = time.perf_counter()
                mean += e-s
            print(f"function took {mean/n:.3f}s to run in average.")
        return _handler
    return handler

def logit(func):
    def handler(*args, **kwargs):
        print(f"About to call {func.__name__}...")
        func(*args, **kwargs)
        print("Done.")

    return handler

N=10_000_000

## Function with no decorator

# def some_fn():
#     for _ in range(N):
#         pass


## Function with 1 simple decorator

# @timeit
# def some_fn():
#     for _ in range(N):
#         pass

# some_fn = timeit(some_fn)

## Function with 1 parametable decorator

# @timeit_range(10)
# def some_fn():
#     for _ in range(N):
#         pass

## Function with 1 simple decorator

# @logit
# def some_fn():
#     for _ in range(N):
#         pass

## Function with 2 decorators

# @logit
# @timeit_range(10)
# def some_fn():
#     for _ in range(N):
#         pass

## Function with 2 decorators, in another order

# @try_except(3)
@logit
def some_fn():
    for _ in range(N):
        pass

some_fn()


# Class decorator
import random

def class_dec(cls):
    class DecoratedClass(cls):
        def __init__(self, *a, **kw):
            super(DecoratedClass, self).__init__(*a, **kw)
            self.__id = random.randint(0, 100)
        
        def custom_fn(self):
            print(f"the id is '{self.__id}'")
    return DecoratedClass

@class_dec
class FooBar:
    pass
# Our FooBar class now has a `custom_fn` method and a `__id` property

foobar = FooBar()
foobar.custom_fn()

from dataclasses import dataclass
# Two ways to create a class that only stores data

@dataclass
class A:
    foo: int
    bar: str

class B:
    def __init__(self, foo: int, bar: str) -> None:
        self.foo = foo
        self.bar = bar
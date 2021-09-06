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

def some_fn():
    for _ in range(N):
        pass


## Function with 1 simple decorator

# @timeit
# def some_fn():
#     for _ in range(N):
#         pass

# some_fn_dec = timeit(some_fn)

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

# @timeit_range(10)
# @logit
# def some_fn():
#     for _ in range(N):
#         pass

some_fn()

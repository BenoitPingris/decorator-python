# Decorators python

## Wrap existing function or class to add new behaviour


### Function
syntax:
```python
@decorator
def my_function(n: int):
    print("even" if n % 2 == 0 else "odd")
```

`decorator` is a function with the following body:
```python
def decorator(func): # `func` is the decorated function

    # `handler` is the function called when the decorated function is called in the code
    def handler(*args, **kwargs):
        # Logic might go here *
        print("Pre-call")

        func(*args, **kwargs) # This is the call to the decorated function, the logic written in the orignal function is not altered

        # * or here
        print("Post-call")

    # We return the new function
    return handler
```

### Class

syntax:
```python
@decorator
class Foo:
    pass
```

`decorator` is a function with the following body:
```python
import random

def decorator(cls): # `cls` is the decorated class
    class DecoratedClass(cls): # We dynamically create a new class that inherits from the `cls`
        def __init__(self, *a, **kw):
            super(DecoratedClass, self).__init__(*a, **kw)
            self.__id = random.randint(0, 100) # Add custom behaviour, properties, methods...
    return DecoratedClass # We return the DecoratedClass, it will replace `cls`
```
## Useful decorators

### Standard library
- `@lru_cache` (from `functools`)
    - memoize function
- `@dataclass` (from `dataclasses`)
    - class made to store data easily, avoid the boilerplate
- `@abstractmethod` (from `abc`)
    - mark a method as abstract, used to create an interface with `abc.ABC`
- `register` (from `atexit`)
    - register a function to be executed when the program ends

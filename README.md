# Decorators python

## Wraps existing function to add new behaviour

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

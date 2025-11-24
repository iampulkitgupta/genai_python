from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} called with args {args} and kwargs {kwargs}")
        return result
    return wrapper

@log_activity
def add(a, b):
    return a + b

sum = add(4, 5)
print(sum)
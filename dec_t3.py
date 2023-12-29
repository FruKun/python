from functools import wraps

def simple_decorator(decorator):
    def decorator_wrapper(decorated_func):
        @wraps(decorated_func)
        def wrapper(*args, **kwargs):
            return decorated_func(*args, **kwargs)
        return wrapper
    return decorator_wrapper

@simple_decorator
def my_simple_logging_decorator(func):
    def you_will_never_see_this_name(*args, **kwargs):
        print('calling {}'.format(func.__name__))
        return func(*args, **kwargs)
    return you_will_never_see_this_name

@my_simple_logging_decorator
def double(x):
    'Doubles a number.'
    return 2 * x

assert double.__name__ == 'double'
assert double.__doc__ == 'Doubles a number.'
print(double(155))
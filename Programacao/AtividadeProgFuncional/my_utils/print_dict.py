from typing import Callable, Any
from functools import wraps


def print_dict(print_fn: Callable[[Any, Any], str] | None = None):
    def decorator(func: Callable[[], dict]):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        
        _dict = wrapper()
        for key, value in _dict.items():
            if print_fn is None:
                print(f"{key} ==> {value}")
            else:
                print(print_fn(key, value))

        return wrapper
    
    return decorator
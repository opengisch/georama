import warnings
from functools import wraps


def temporary_fix(reason: str = ""):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            warnings.warn(
                f"{func.__name__} is a TEMPORARY FIX. {reason}",
                category=UserWarning,
                stacklevel=2,
            )
            return func(*args, **kwargs)

        return wrapper

    return decorator

from functools import wraps


def ignore_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = None
        ignored_exceptions = kwargs['ignored_exceptions']

        if ignored_exceptions:
            try:
                result = func(*args, **kwargs)
            except ignored_exceptions:
                pass
        else:
            result = func(*args, **kwargs)

        return result
    return wrapper

from inspect import getfullargspec, signature


def overload(fn, func_map={}):
    mark = (*(fn.__qualname__.split(".")), len(getfullargspec(fn).args))
    if mark not in func_map:
        func_map[mark] = fn

    def wrapper(*args, **kwargs):
        return func_map[(*(fn.__qualname__.split(".")), len(args))](*args, **kwargs)

    return wrapper

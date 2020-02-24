from inspect import getfullargspec, signature
from typing import Dict, Tuple, Any, Callable


def overload(
    fn: Callable, func_map: Dict[Tuple, Callable] = {}
) -> Callable[[Any, Any], Any]:
    mark = (*(fn.__qualname__.split(".")), len(getfullargspec(fn).args))
    if mark not in func_map:
        func_map[mark] = fn

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        return func_map[(*(fn.__qualname__.split(".")), len(args))](*args, **kwargs)

    return wrapper

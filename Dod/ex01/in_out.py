from typing import Callable

def square(x: int | float) -> int | float:
    """Returns the square of x."""
    return x * x

def pow(x: int | float) -> int | float:
    """Returns x raised to the power of x."""
    return x ** x

def outer(x: int | float, function: Callable) -> object:
    """Returns a closure that applies 'function' to 'x' and keeps a call count."""
    count = 0

    def inner() -> float:
        nonlocal count
        count += 1
        return function(x ** count)

    return inner
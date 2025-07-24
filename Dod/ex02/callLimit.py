from typing import Any, Callable

def callLimit(limit: int) -> Callable:
    """
    Decorator factory that limits the number of times a function can be called.

    Args:
        limit (int): The maximum number of times the decorated function is allowed to be called.

    Returns:
        Callable: A decorator that wraps the function with call-limiting behavior.
    """
    count = 0

    def callLimiter(function: Callable) -> Callable:
        """
        Decorator that wraps the target function to limit its number of calls.

        Args:
            function (Callable): The function to be limited.

        Returns:
            Callable: The wrapped function with limited calls.
        """
        def limit_function(*args: Any, **kwds: Any) -> Any:
            """
            Wrapper function that enforces the call limit.

            Returns:
                Any: The result of the original function, or None if the limit is reached.
            """
            nonlocal count
            if count >= limit:
                print(f"Function {function.__name__} call limit reached.")
                return
            count += 1
            return function(*args, **kwds)

        return limit_function

    return callLimiter

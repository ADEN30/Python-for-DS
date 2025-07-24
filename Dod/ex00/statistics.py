from typing import Any
from math import sqrt

def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Calculate and print statistical measures based on given keyword arguments."""

    # Filtrer uniquement les valeurs numériques
    numbers = [x for x in args if isinstance(x, (int, float))]

    if not numbers:
        print("ERROR: No numeric data provided.")
        return

    n = len(numbers)
    sorted_numbers = sorted(numbers)

    def mean():
        return sum(numbers) / n

    def median():
        mid = n // 2
        if n % 2 == 0:
            return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
        return sorted_numbers[mid]

    def quartile(q):
        pos = (n - 1) * q
        lower = int(pos)
        upper = lower + 1
        if upper >= n:
            return sorted_numbers[lower]
        return sorted_numbers[lower] + (pos - lower) * (sorted_numbers[upper] - sorted_numbers[lower])

    def var():
        m = mean()
        return sum((x - m) ** 2 for x in numbers) / n

    def std():
        return sqrt(var())

    functions = {
        "mean": mean,
        "median": median,
        "quartile": lambda: [quartile(0.25), quartile(0.75)],
        "var": var,
        "std": std
    }

    for key, func in kwargs.items():
        stat_func = functions.get(func)
        if stat_func:
            print(f"{func} : {stat_func()}")
        else:
            print(f"{func} : ERROR")


ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
print("-----")
ft_statistics(toto="mean", tutu="median", tata="quartile")
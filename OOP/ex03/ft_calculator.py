class calculator:
    """A simple calculator for scalar operations on float vectors."""

    def __init__(self, vector: list[float]):
        """Initialize the calculator with a list of floats."""
        self.vector = vector

    def __add__(self, other) -> None:
        """Add a scalar to the vector and print the result."""
        if isinstance(other, (int, float)):
            result = [x + other for x in self.vector]
            print(result)

    def __sub__(self, other) -> None:
        """Subtract a scalar from the vector and print the result."""
        if isinstance(other, (int, float)):
            result = [x - other for x in self.vector]
            print(result)

    def __mul__(self, other) -> None:
        """Multiply the vector by a scalar and print the result."""
        if isinstance(other, (int, float)):
            result = [x * other for x in self.vector]
            print(result)

    def __truediv__(self, other) -> None:
        """Divide the vector by a scalar and print the result."""
        if isinstance(other, (int, float)):
            if other == 0:
                print("Error: Division by zero")
                return
            result = [x / other for x in self.vector]
            print(result)


v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v1 + 5
print("---")
v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v2 * 5
print("---")
v3 = calculator([10.0, 15.0, 20.0])
v3 - 5
v3 / 5
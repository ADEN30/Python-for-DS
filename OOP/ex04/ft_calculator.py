class calculator:
    """A calculator class to perform vector operations without instantiation."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Prints the dot product of two vectors."""
        result = sum(x * y for x, y in zip(V1, V2))
        print(result)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Prints the element-wise addition of two vectors."""
        result = [x + y for x, y in zip(V1, V2)]
        print(result)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Prints the element-wise subtraction of two vectors."""
        result = [x - y for x, y in zip(V1, V2)]
        print(result)
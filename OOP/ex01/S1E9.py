from abc import ABC, abstractmethod

class Character(ABC):
    """Abstract base class representing a character with a name and life status."""

    def __init__(self, first_name, is_alive=True):
        """
        Initialize a Character.

        Parameters:
        first_name (str): The first name of the character.
        is_alive (bool, optional): The life status of the character. Defaults to True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Change the character's life status from alive to dead."""
        self.is_alive = False

    @abstractmethod
    def __str__(self):
        """Abstract method to return a string representation of the character."""
        pass


class Stark(Character):
    """Concrete class representing a member of House Stark."""

    def __init__(self, first_name, is_alive=True):
        """
        Initialize a Stark character.

        Parameters:
        first_name (str): The first name of the Stark character.
        is_alive (bool, optional): The life status of the character. Defaults to True.
        """
        super().__init__(first_name, is_alive)

    def __str__(self):
        return f"{self.first_name} Stark - {'Alive' if self.is_alive else 'Dead'}"
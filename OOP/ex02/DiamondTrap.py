from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    """Class representing King Joffrey Baratheon, the weird 'false' king."""

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        # on initialise les attributs physiques via les properties
        self._eyes = self.eyes  # utilise la valeur héritée (brown)
        self._hairs = self.hairs  # (dark)

    # --- Property eyes ---
    @property
    def eyes(self):
        return self._eyes

    @eyes.setter
    def eyes(self, value):
        self._eyes = value

    def get_eyes(self):
        return self.eyes

    def set_eyes(self, color):
        self.eyes = color

    # --- Property hairs ---
    @property
    def hairs(self):
        return self._hairs

    @hairs.setter
    def hairs(self, value):
        self._hairs = value

    def get_hairs(self):
        return self.hairs

    def set_hairs(self, color):
        self.hairs = color

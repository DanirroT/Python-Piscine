
from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    """A Class to represent the king.
Requires first_name as parameters.
may take is_alive as parameters.
sets eye and hair color to the Defoult, that being Baratheon."""

    hair: str

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Constructor for King Class."""
        
        super().__init__(first_name, is_alive)    

        self.hair = self.hairs
        del self.hairs

    def set_eyes(self, color) -> None:
        """Used to change the character's Eye Color."""
        self.eyes = color

    def set_hairs(self, color) -> None:
        """Used to change the character's Hair Color."""
        del self.hair
        self.hairs = color

    def get_eyes(self) -> str:
        """Used to get a character's Eye Color."""
        return self.eyes

    def get_hairs(self) -> str:
        """Used to  get a character's Hair Color."""
        return self.hairs

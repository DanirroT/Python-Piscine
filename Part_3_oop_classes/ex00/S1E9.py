
from abc import ABC, abstractmethod

class Character(ABC):
    """An Abstrach Class to represent a Character.
Requires first_name as parameters.
may take is_alive as parameters."""
    
    first_name: str
    is_alive: bool
    
    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Abstrach Constructor for Character Class."""
        self.first_name = first_name
        self.is_alive = is_alive
        
    def die(self) -> None:
        """Used to set is_alive to False."""
        self.is_alive = False
    
class Stark(Character):
    """A Class to represent a Character.
Requires first_name as parameters.
may take is_alive as parameters."""
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Constructor for Stark Class."""
        super().__init__(first_name, is_alive)    
    


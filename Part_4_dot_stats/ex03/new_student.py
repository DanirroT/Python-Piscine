
"""
 name and nickname, set active to True,
create the student login, and generate a random ID with the generate_id function.
You must not use __str__ , __repr__ in your class.
The prototype of function and class is:
"""

import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
    
    name: str
    surname: str
    active: bool = field(default = True)
    login: str = field(init=False)
    ID: str = field(init=False)

    def __post_init__(self):
        self.login = self.name[0] + self.surname.lower()
        self.ID = generate_id()
    
    def    __str__(self):
        return f"""Student(name='{self.name}', surname='{self.surname}', active={self.active}, login={self.login}, ID='{self.ID}')"""
    
    def    __repr__(self):
        return f"""Student(name='{self.name}', surname='{self.surname}', active={self.active}, login={self.login}, ID='{self.ID})"""

student_1 = Student(name = "Edward", surname = "agle")
print(student_1)

student_2 = Student(name = "Edward", surname = "agle", id = "toto")
print(student_2)

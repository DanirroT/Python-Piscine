
from S1E7 import Baratheon, Lannister

Robert = Baratheon("Robert")
print(Robert.__dict__) #{'first_name': 'Robert', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'brown', 'hairs': 'dark'}
print(Robert.__str__) #<bound method Baratheon.__str__ of Vector: ('Baratheon', 'brown', 'dark')>
print(Robert.__repr__) #<bound method Baratheon.__repr__ of Vector: ('Baratheon', 'brown', 'dark')>
print(Robert.is_alive) #True
Robert.die()
print(Robert.is_alive) #False
print(Robert.__doc__) #Representing the Baratheon family.
print("---") #---
Cersei = Lannister("Cersei")
print(Cersei.__dict__) #{'first_name': 'Cersei', 'is_alive': True, 'family_name': 'Lannister', 'eyes': 'blue', 'hairs': 'light'}
print(Cersei.__str__) #<bound method Lannister.__str__ of Vector: ('Lannister', 'blue', 'light')>
print(Cersei.is_alive) #True
print("---") #---
Jaine = Lannister.create_lannister("Jaine", True)
print(f"Name: {Jaine.first_name, type(Jaine).__name__}, Alive: {Jaine.is_alive}") #Name: ('Jaine', 'Lannister'), Alive: True









# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    S1E9.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dmota-ri <dmota-ri@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/27 16:26:10 by dmota-ri          #+#    #+#              #
#    Updated: 2026/01/27 20:12:15 by dmota-ri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from abc import ABC, abstractmethod

class Character(ABC):
	"""Your docstring for Class"""
	
	first_name: str
	is_alive: bool
	
	@abstractmethod
	def __init__(self, first_name: str, is_alive: bool = True) -> None:
		"""Your docstring for Constructor"""
		self.first_name = first_name
		self.is_alive = is_alive
		
	def die(self) -> None:
		"""Your docstring for Method"""
		self.is_alive = False
	
class Stark(Character):
	"""Your docstring for Class"""
	def __init__(self, first_name: str, is_alive: bool = True) -> None:
		"""Your docstring for Constructor"""
		super().__init__(first_name, is_alive)	
	



Ned = Stark("Ned")
print(Ned.__dict__)
print(Ned.is_alive)
Ned.die()
print(Ned.is_alive)
print(Ned.__doc__)
print(Ned.__init__.__doc__)
print(Ned.die.__doc__)
print("---")
Lyanna = Stark("Lyanna", False)
print(Lyanna.__dict__)


#	{'first_name': 'Ned', 'is_alive': True}
#	True
#	False
#	Your docstring for Class
#	Your docstring for Constructor
#	Your docstring for Method
#	---
#	{'first_name': 'Lyanna', 'is_alive': False}

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    S1E7.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dmota-ri <dmota-ri@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/27 16:26:10 by dmota-ri          #+#    #+#              #
#    Updated: 2026/02/01 13:54:45 by dmota-ri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from S1E9 import Character, Stark

class Baratheon(Character):
	"""A Class to represent a character of the Baratheon Family.
Requires first_name as parameters.
Takes first_name and is_alive as parameters.
sets eye and hair color to brown and dark respectively."""

	family_name : str
	eyes : str
	hairs : str

	def __init__(self, first_name: str, is_alive: bool = True) -> None:
		"""Constructor for Baratheon Class."""
		
		super().__init__(first_name, is_alive)

		self.family_name = "Baratheon"
		self.eyes = "brown"
		self.hairs = "dark"
		
	def	__str__(self):
		return f"""'{self.family_name}', '{self.eyes}', '{self.hairs}'"""
	
	def	__repr__(self):
		return f"""'{self.family_name}', '{self.eyes}', '{self.hairs}'"""
	
class Lannister(Character):
	"""A Class to represent a character of the Lannister Family.
Takes first_name and is_alive as parameters.
sets eye and hair color to blue and light respectively."""

	family_name : str
	eyes : str
	hairs : str

	def __init__(self, first_name: str, is_alive: bool = True) -> None:
		"""Constructor for Lannister Class."""
		
		super().__init__(first_name, is_alive)	

		self.family_name = "Lannister"
		self.eyes = "blue"
		self.hairs = "light"
		
	def	__str__(self):
		return f"""('{self.family_name}', '{self.eyes}', '{self.hairs}')"""
	
	def	__repr__(self):
		return f"""('{self.family_name}', '{self.eyes}', '{self.hairs}')"""
	
	def create_lannister(first_name: str, is_alive: bool = True) -> 'Lannister':
		"""Factory method to create a Lannister instance."""
		return Lannister(first_name, is_alive)
	

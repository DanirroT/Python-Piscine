# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    S1E9.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dmota-ri <dmota-ri@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/27 16:26:10 by dmota-ri          #+#    #+#              #
#    Updated: 2026/02/01 13:50:22 by dmota-ri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from abc import ABC, abstractmethod

class Character(ABC):
	"""An Abstrach Class to represent a Character.
Takes first_name and is_alive as parameters."""
	
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
may take is_alive parameters."""
	def __init__(self, first_name: str, is_alive: bool = True) -> None:
		"""Constructor for Stark Class."""
		super().__init__(first_name, is_alive)	
	


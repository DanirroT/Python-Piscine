# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_calculator.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dmota-ri <dmota-ri@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/01 13:55:54 by dmota-ri          #+#    #+#              #
#    Updated: 2026/02/01 14:06:23 by dmota-ri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class calculator:
	"""A Class to perform basic arithmetic operations on a list of numbers."""

	list : list[float]
	
	def __init__(self, list_of_numbers: list[float]) -> None:
		"""Constructor for calculator Class."""
		self.list = list_of_numbers
		
	def __add__(self, object) -> None:
		print([i + object for i in self.list])
		
	def __mul__(self, object) -> None:
		print([i * object for i in self.list])

	def __sub__(self, object) -> None:
		print([i - object for i in self.list])

	def __truediv__(self, object) -> None:
		print([i / object for i in self.list])

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_calculator.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dmota-ri <dmota-ri@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/01 13:55:54 by dmota-ri          #+#    #+#              #
#    Updated: 2026/02/01 14:18:01 by dmota-ri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class calculator:
	"""A Class to perform basic arithmetic operations on a list of numbers."""

	def add_vec(V1: list[float], V2: list[float]) -> None:
		print("Add Vector is :", [float(i + j) for i, j in zip(V1, V2)])
		
	def sous_vec(V1: list[float], V2: list[float]) -> None:
		print("sous Vector is :", [float(i - j) for i, j in zip(V1, V2)])

	def dotproduct(V1: list[float], V2: list[float]) -> None:
		print(sum([i * j for i, j in zip(V1, V2)]))




a = [5, 10, 2]
b = [2, 4, 3]

calculator.dotproduct(a,b)
calculator.add_vec(a,b)
calculator.sous_vec(a,b)

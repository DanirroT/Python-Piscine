# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    give_bmi.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dmota-ri <dmota-ri@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/27 16:26:10 by dmota-ri          #+#    #+#              #
#    Updated: 2026/01/27 20:46:39 by dmota-ri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	"""Takes two lists, Height and Weight. Calculates the BMI value of each set and returns all in a list."""
	if len(height) != len(weight):
		raise ValueError("Height and weight lists must have the same length.")

	bmi	= []
	for i in range(0, len(weight)):
		bmi.append(weight[i] / (height[i] ** 2))
	print("1: ", bmi)			
	
	bmi = [ w/(h**2) for (h, w) in zip(height, weight)]
	print("2: ", bmi)

	return bmi
	




def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	"""Takes a list of BMI values and a limit, returns a list of booleans indicating if each BMI is above the limit."""
	above = []
	for i in bmi:
		above.append(bool(i > limit))
	return above




height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))


#	print([ i for i in map(lambda x: x>26, [ w/(h**2) for (h, w) in zip(height, weight)])])	
#	print([w/(h**2) > 26 for h, w in zip(height, weight)])
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    array2D.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dmota-ri <dmota-ri@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/27 16:26:14 by dmota-ri          #+#    #+#              #
#    Updated: 2026/01/30 18:17:34 by dmota-ri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
	"""Takes a lists, and two arguments, start and end as ints.
It slices the list returning only the elements after Start and before end.
Handles negative indices counting from the bottom of the list.
If end is smaller that start returns an empty list."""
	shape = [0, 0]
	shape[0] = len(family)
	shape[1] = len(family[1])
	print(f"Original Shape is : {shape}")
	if start < 0:
		start = shape[0] + start
	if end < 0:
		end = shape[1] + end
	if end <= start or start >= shape[0]:
		return []
	new_shape = (end - start, shape[1])
	print(f"My Shape is : {shape}")
	print(f"My New Shape is : {new_shape}")
	return family[start:end]



family = [[1.80, 78.4],
		[2.15, 102.7],
		[2.10, 98.5],
		[1.88, 75.2]]

print()
print(slice_me(family, 1, 2))

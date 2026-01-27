# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    array2D.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dmota-ri <dmota-ri@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/27 16:26:14 by dmota-ri          #+#    #+#              #
#    Updated: 2026/01/27 20:52:39 by dmota-ri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
	height = len(family)
	width = len(family[1])
	shape = (height, width)
	if start < 0:
		start = height + start
	if end < 0:
		end = height + end
	new_shape = (end - start, width)
	print(f"My Shape is : {shape}")
	print(f"My New Shape is : {new_shape}")
	return family[start:end]



family = [[1.80, 78.4],
		[2.15, 102.7],
		[2.10, 98.5],
		[1.88, 75.2]]
print()
print(slice_me(family, 0, 2))
print()
print(slice_me(family, 1, -2))

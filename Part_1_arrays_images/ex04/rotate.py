# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    rotate.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dmota-ri <dmota-ri@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/27 16:26:14 by dmota-ri          #+#    #+#              #
#    Updated: 2026/01/27 18:47:40 by dmota-ri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#import numpy as np
from load_image import ft_load
def array as list

def rotate(path: str):
	image = ft_load(path)
	height = len(image)
	width = len(image[1])
	collor_vals = len(image[1][1])
	if collor_vals == 1:
		shape = (height, width)
	else:
		shape = (height, width, collor_vals)
#	print(f"My Shape is : {shape}")
	h_center = height // 2
	w_center = width // 2
	print(f"New shape after Transpose: {shape}")
	new_image = [[[]]]
	while i < shape[0]:
		j = 0
		while j < shape[1]:
			new_image[j][shape[1] - i] = image[i][j]
			i += 1
		j += 1
	print(new_image)

ft_load("landscape.jpg")
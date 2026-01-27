# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pimp_image copy.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dmota-ri <dmota-ri@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/27 16:26:14 by dmota-ri          #+#    #+#              #
#    Updated: 2026/01/27 18:13:28 by dmota-ri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#import numpy as np
from load_image import ft_load
def array as list

def ft_invert(array): # -> array:
	hight = len(array)
	width = len(array[1])
	collor_vals = len(image[1][1])
	for i in range(hight):
		for j in range(width):
			for k in range(collor_vals):
				array[i][j][k] = 255 - array[i][j][k]
	return array

def ft_red(array): # -> array:
	hight = len(array)
	width = len(array[1])
	for i in range(hight):
		for j in range(width):
			array[i][j][2] = 0
			array[i][j][3] = 0
	return array
				
def ft_green(array): # -> array:
	hight = len(array)
	width = len(array[1])
	for i in range(hight):
		for j in range(width):
			array[i][j][1] = 0
			array[i][j][3] = 0
	return array
				
def ft_blue(array): # -> array:
	hight = len(array)
	width = len(array[1])
	for i in range(hight):
		for j in range(width):
			array[i][j][1] = 0
			array[i][j][2] = 0
	return array
				
def ft_grey(array): # -> array:
	hight = len(array)
	width = len(array[1])
	for i in range(hight):
		for j in range(width):
			pixel_avg = int(((array[i][j][1])**2 + (array[i][j][2])**2 + (array[i][j][3])**2 / 3)**0.5)
			array[i][j][1] = pixel_avg
			array[i][j][2] = pixel_avg
			array[i][j][3] = pixel_avg
	return array


RGB
print(ft_load("landscape.jpg"))
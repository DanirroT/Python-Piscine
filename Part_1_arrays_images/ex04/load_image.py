# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    load_image.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dmota-ri <dmota-ri@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/27 16:26:14 by dmota-ri          #+#    #+#              #
#    Updated: 2026/01/27 22:06:33 by dmota-ri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os

#import numpy as np
from PIL import Image
import numpy as np

def ft_load(path: str) -> np.array:
	"""
	Docstring for ft_load()
	
	:param path: Description
	:type path: str - Accepted formats are .jpg, .jpeg (at least)
	:returns: np.array - The image as a NumPy array
	"""
	try:
		image = Image.open(path)
	except Exception as e:
		print(f"Error loading image: {e}")
		return None
	
	image = np.array(image)
	shape = image.shape
	
	print(f"The shape of image is: {shape}", end="")
	if shape[2] == 1:
		print(f" or {str((height, width))}", end="")
	print()
	return image

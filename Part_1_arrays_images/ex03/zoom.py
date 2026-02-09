# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    zoom.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dmota-ri <dmota-ri@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/27 16:26:14 by dmota-ri          #+#    #+#              #
#    Updated: 2026/01/30 18:24:36 by dmota-ri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

def display_image(image, name):
	if image is None:
		return None
	plt.imshow(image, cmap="gray")
	plt.savefig(name)
#	plt.show()

def zoom(path: str):
	"""Takes the path to a image as a string and returns a zoomed in crop of the image.
this zoomed version is 400x400 pixels or smaller if the image is smaller than that and is also in GreyTone."""
	image = ft_load(path)
	if image is None:
		return None
	print(image)
#	display_image(image, "original_image.png")
	
	shape = image.shape
	h_center = shape[0] // 2
	w_center = shape[1] // 2
	
	new_shape = (min(shape[0], 400), min(shape[1], 400), 1)
	new_shape_2 = (new_shape[0], new_shape[1])
	print(f"My New Shape is : {new_shape} or {new_shape_2}")
#	new_image = [[[0 for _ in range(collor_vals)] for _ in range(new_shape[1])] for _ in range(new_shape[0])]

#	grey = np.sqrt((image ** 2).mean(axis=2))
	grey_2 = np.sqrt(np.mean(image.astype(np.float32) ** 2, axis=2))
	grey = grey_2[:, :, np.newaxis].astype(np.uint8)
#	print("post grey:\n", grey)
	zoomed = grey[h_center - new_shape[0]//2 : h_center + new_shape[0]//2 + (new_shape[0] % 2),
					w_center - new_shape[1]//2 : w_center + new_shape[1]//2 + (new_shape[1] % 2)]
	print(zoomed)
	display_image(zoomed, "zoomed_image.png")
	
	return zoomed


def main():
	zoom("Part_1_arrays_images/ex03/animal.jpeg")
#	zoom("animal.jpeg")
#	zoom("Part_1_arrays_images/ex03/Small_Test.jpg")

if __name__ == "__main__":
	main()

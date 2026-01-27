# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    zoom.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dmota-ri <dmota-ri@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/27 16:26:14 by dmota-ri          #+#    #+#              #
#    Updated: 2026/01/27 22:56:46 by dmota-ri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

def display_image(image, name):
	plt.imshow(image)  # squeeze removes the singleton channel
	plt.axis('off')  # optional: remove axes
	plt.savefig(name)
#	plt.show()

def zoom(path: str):
	image = ft_load(path)
#	print(image)
	display_image(image, "original_image.png")
	shape = image.shape
#	shape = (height, width, collor_vals)
#	print(f"My Shape is : {shape}")


#	h_center = shape[0] // 2
#	w_center = shape[1] // 2
	new_shape = (400, 400, 1)
	new_shape_2 = (new_shape[0], new_shape[1])
	print(f"My New Shape is : {new_shape} or {new_shape_2}")
#	new_image = [[[0 for _ in range(collor_vals)] for _ in range(new_shape[1])] for _ in range(new_shape[0])]
	image = image.mean(axis=2)
	norm = image / image.max()
	h_indices, w_indices, _ = np.indices(shape)
	h_center = int(np.sum(h_indices * norm) / np.sum(norm))
	w_center = int(np.sum(w_indices * norm) / np.sum(norm))
	zoomed = image[h_center - new_shape[0]//2 : h_center + new_shape[0]//2,
					w_center - new_shape[1]//2 : w_center + new_shape[1]//2]
	print(zoomed)
	display_image(zoomed, "zoomed_image.png")
#	print(zoomed[:, :, np.newaxis])


def main():
	zoom("Part_1_arrays_images/ex03/animal.jpeg")
#	zoom("animal.jpeg")

if __name__ == "__main__":
	main()

#	[167]
#	[180]
#	[194]
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    load_csv.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dmota-ri <dmota-ri@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/27 16:26:10 by dmota-ri          #+#    #+#              #
#    Updated: 2026/01/27 19:02:37 by dmota-ri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pamdas as pd


def load(path: str) -> Dataset:
	try:
		table = pd.open_csv("./" + path)
	except Exception as e:
		print(f"Error loading image: {e}")
		return None
	
	height = len(table)
	width = len(table[1])
	
	shape = (height, width)
	
	print(f"Loading dataset of dimensions {shape}")

#	print(f"[[{f"{image[i][j] for j in range(height)}..." for i in range(min(3, height))}]]")
	
	print(table)
	
	return table



print(load("life_expectancy_years.csv"))




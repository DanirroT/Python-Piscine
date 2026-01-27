# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aff_life.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dmota-ri <dmota-ri@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/27 16:26:10 by dmota-ri          #+#    #+#              #
#    Updated: 2026/01/27 19:11:18 by dmota-ri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib
from Part_3_DataTable_pandas.ex01.aff_life import load

def main():
	table = load("life_expectancy_years.csv")

	table["Year"]["Life expectancy"]["Portugal"].plot()
	matplotlib.pyplot.show()


if __name__ == "__main__":
	main()
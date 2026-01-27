# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    projection_life.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dmota-ri <dmota-ri@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/27 16:26:10 by dmota-ri          #+#    #+#              #
#    Updated: 2026/01/27 19:25:38 by dmota-ri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib
from Part_3_DataTable_pandas.ex01.aff_life import load

def main():
	table_income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
	table_ley = load("life_expectancy_years.csv")

	table_income["Gross Docestic Product"]["Portugal"].plot_x()
	table_ley["Life expectancy"]["Portugal"].plot_y()
	matplotlib.pyplot.show()


if __name__ == "__main__":
	main()
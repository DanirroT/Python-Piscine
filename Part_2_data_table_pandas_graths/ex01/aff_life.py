# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aff_life.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dmota-ri <dmota-ri@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/27 16:26:10 by dmota-ri          #+#    #+#              #
#    Updated: 2026/01/31 20:37:56 by dmota-ri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from load_csv import load

def main():
	table = load("Part_2_data_table_pandas_graths/ex01/life_expectancy_years.csv")
#	table = load("life_expectancy_years.csv")
	table.columns = table.columns.astype(int)
	print(table)

	print("portugal")
	years = table.columns.tolist()
	print(years)
	print(years[::10])
	portugal = table.loc["Portugal"]

#	print(portugal[years])
	plt.plot(portugal)

	plt.title("Portugal Life Expectency Projections")
	
	plt.xlabel("Year")
	plt.ylabel("Life Expectency")

#	print(np.arange(min(years),max(years) + 1,40))

	plt.xticks(range(min(years), max(years) + 1, 40))
	
	plt.savefig("ex01_aff_life.png")
#	plt.show()


if __name__ == "__main__":
	main()



# 02. Valores do gráfico
#overs    = [1,2,3,4,5,6,7,8,9,10]
#run_rate = [6,5,5,7,6.5,8,8.5,9,8,8.5]

# 03. Construção do gráfico
#plt.plot(overs,run_rate)

# 04. Valores dos eixos
#     Eixo dos xx: de 1 a 10 variando de 1 em 1
#     Eixo dos yy: de 4 a 10 variando 0,5
#plt.xticks([x for x in np.arange(1,11,1)])
#plt.yticks([x for x in np.arange(4,10.5,0.5)])

# 05. Apresentação do gráfico
#plt.savefig("ex01_aff_life.png")
#plt.show()

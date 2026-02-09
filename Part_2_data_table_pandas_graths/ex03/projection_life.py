
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from load_csv import load

def main():
# table_income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    table_income = load("Part_2_data_table_pandas_graths/ex03/income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    table_income.columns = table_income.columns.astype(int)
    print(table_income, end="\n\n")

# table_ley = load("life_expectancy_years.csv") 
    table_ley = load("Part_2_data_table_pandas_graths/ex03/life_expectancy_years.csv")
    table_ley.columns = table_ley.columns.astype(int)
    print(table_ley)

    print("table -> portugal")
    income_1900 = table_income.loc[:, 1900]
    ley_1900 = table_ley.loc[:, 1900]

    print(income_1900, ley_1900)

    print("plot")
    plt.scatter(income_1900, ley_1900)

    print("labels")
    plt.title("1900")

    plt.xlabel("Gross Domestic Product")
    plt.ylabel("Life Expectancy")

    print("axis")
    plt.yticks(range(int(min(ley_1900)), int(max(ley_1900) + 1), 5))
    #plt.yticks(range(0, len(portugal) + 1, 200))
    #ticks = range(0, max(f_int), 20000000)
    #plt.yticks(ticks, [f"{t/1_000_000:.1f}M" for t in ticks])
    plt.xscale("log")
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])

    plt.savefig("ex03_projection_life.png")
# plt.show()









if __name__ == "__main__":
    main()
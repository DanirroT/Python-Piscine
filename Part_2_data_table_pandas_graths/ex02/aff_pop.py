
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from load_csv import load

def main():
    table = load("Part_2_data_table_pandas_graths/ex02/population_total.csv")
# table = load("population_total.csv")
    table.columns = table.columns.astype(int)
# print(table)

    years = np.array(table.columns.tolist())
    portugal = table.loc["Portugal"]
    france = table.loc["France"]
    
# print("portugal")
    years = years[years <= 2050]
    portugal = portugal.loc[table.columns <= 2050]
    france = france.loc[table.columns <= 2050]
    p_int = (portugal.str.replace("M", "", regex=False).astype(float) * 1_000_000).astype(int)
    f_int = (france.str.replace("M", "", regex=False).astype(float) * 1_000_000).astype(int)


# print("portugal")
    print(p_int, f_int)
# print(portugal)
# print(years, type(years), years.dtype)
    
# print("portugal")
    plt.plot(p_int, label="Portugal")
    plt.plot(f_int, label="France")

# print("portugal")
    plt.title("Population Projections")
    
    plt.xlabel("Year")
    plt.ylabel("Population")

# print(np.arange(min(years),max(years) + 1,40))

    print("portugal")
    plt.xticks(range(min(years), max(years) + 1, 40))
    #plt.yticks(range(0, len(portugal) + 1, 200))
    ticks = range(0, max(f_int), 20000000)
    plt.yticks(ticks, [f"{t/1_000_000:.1f}M" for t in ticks])
    
    plt.savefig("ex02_aff_pop.png")
# plt.show()


if __name__ == "__main__":
    main()
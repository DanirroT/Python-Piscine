
import pandas as pd

def load(path: str): # -> Dataset:
    """
    Docstring for load()
    
    :param path: Description
    :type path: str - Accepted formats is .csv
    :returns: pd.Dataset - The table as a Pandas Dataset
    """
    try:
        table = pd.read_csv(path)
    except Exception as e:
        print(f"Error loading table: {e}")
        return None
    shape = table.shape
    print(f"Loading dataset of dimensions {shape}")    
    table = table.set_index(table.columns[0])
    return table

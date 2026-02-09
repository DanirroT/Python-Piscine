
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
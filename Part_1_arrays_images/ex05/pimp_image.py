
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

def display_image(image, name):
    if image is None:
        return None
    plt.imshow(image, cmap="gray")
    plt.savefig(name)
# plt.show()

def ft_invert(array): # -> array:
    """Inverts the color of the image received."""
    if type(array) is not array:
        return None
    output = 255 - array
    display_image(output, "invertgrey_image.png")
    return output

def ft_red(array): # -> array:
    """Zeroes Blue and Green Chanels from a given image, keeping only Red."""
    if type(array) is not array:
        return None
    array[:,:,1] = 0
    array[:,:,2] = 0
    display_image(array, "red_image.png")
    return array
                
def ft_green(array): # -> array:
    """Zeroes Red and Blue Chanels from a given image, keeping only Green."""
    if type(array) is not array:
        return None
    array[:,:,0] = 0
    array[:,:,2] = 0
    display_image(array, "green_image.png")
    return array
                
def ft_blue(array): # -> array:
    """Zeroes Red and Green Chanels from a given image, keeping only Blue."""
    if type(array) is not array:
        return None
    array[:,:,0] = 0
    array[:,:,1] = 0
    display_image(array, "blue_image.png")
    return array
                
def ft_grey(array): # -> array:
    """Converts the image into Greytone, with a single channel."""
    if type(array) is not array:
        return None
    grey = np.sqrt(np.mean(array.astype(np.float32) ** 2, axis=2))
    output = grey[:, :, np.newaxis].astype(np.uint8)
    display_image(output, "grey_image.png")
    return output



def main():
    image = ft_load("Part_1_arrays_images/ex05/landscape.jpg")
# image = ft_load("landscape.jpg")
# image = ft_load("Part_1_arrays_images/ex03/Small_Test.jpg")
    ft_invert(image)
    image = ft_load("Part_1_arrays_images/ex05/landscape.jpg")
    ft_red(image)        
    image = ft_load("Part_1_arrays_images/ex05/landscape.jpg")
    ft_green(image)
    image = ft_load("Part_1_arrays_images/ex05/landscape.jpg")
    ft_blue(image)
    image = ft_load("Part_1_arrays_images/ex05/landscape.jpg")
    ft_grey(image)

if __name__ == "__main__":
    main()

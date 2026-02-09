
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

def display_image(image, name):
    if image is None:
        return None
    plt.imshow(image, cmap="gray")
    plt.savefig(name)
# plt.show()

def zoom(path: str):
    """Takes the path to a image as a string and returns a zoomed in crop of the image.
this zoomed version is 400x400 pixels or smaller if the image is smaller than that and is also in GreyTone."""
    image = ft_load(path)
    if image is None:
        return None
# display_image(image, "original_image.png")
    
    shape = image.shape
    h_center = shape[0] // 2
    w_center = shape[1] // 2
    
    new_shape = (min(shape[0], 400), min(shape[1], 400), 1)
# new_image = [[[0 for _ in range(collor_vals)] for _ in range(new_shape[1])] for _ in range(new_shape[0])]

# grey = np.sqrt((image ** 2).mean(axis=2))
    grey_2 = np.sqrt(np.mean(image.astype(np.float32) ** 2, axis=2))
    grey = grey_2[:, :, np.newaxis].astype(np.uint8)
# print("post grey:\n", grey)
    zoomed = grey[h_center - new_shape[0]//2: h_center + new_shape[0]//2 + (new_shape[0] % 2),
                    w_center - new_shape[1]//2: w_center + new_shape[1]//2 + (new_shape[1] % 2)]
    print(zoomed)
    
    return zoomed

def rotate(path: str):
    """Takes the path to a image as a string and returns a Rotated, zoomed in crop of the image.
this zoomed version is 400x400 pixels or smaller if the image is smaller than that and is also in GreyTone."""
    image = zoom(path)
    if image is None:
        return None
    shape = image.shape
    print(f"New shape after Transpose: {shape}")
    image = np.mean(image, axis=2)
    rotated = np.rot90(image, k=1)
    print(rotated)
    display_image(rotated, "rotated_image.png")

def main():
# rotate("zoomed_image.jpg")
    rotate("Part_1_arrays_images/ex03/animal.jpeg")
# zoom("animal.jpeg")
# zoom("Part_1_arrays_images/ex03/Small_Test.jpg")

if __name__ == "__main__":
    main()

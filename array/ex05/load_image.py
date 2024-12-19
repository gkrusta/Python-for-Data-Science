from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def display_image(array, flag):
    """Displays the image."""
    if flag:
        plt.imshow(array, cmap="gray")
    else:
        plt.imshow(array)
    plt.show()
    plt.close()


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image, converts it to RGB format
    and returns its pixel data as a NumPy array.
    Prints the shape of the image.
    """
    try:
        image = Image.open(path)
        rgb_image = image.convert("RGB")
        pixels = np.array(rgb_image)
        print("The shape of image is:", pixels.shape)
        print(pixels)
        display_image(pixels, 0)
        return pixels
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

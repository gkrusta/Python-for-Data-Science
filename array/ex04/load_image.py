import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def ft_load(path: str):
    """
    Loads an image, converts it to RGB format,
    and returns its pixel data as a NumPy array.
    """
    try:
        image = Image.open(path)
        if not image or image.format != "JPEG":
            raise ValueError("Cannot open the file or unsupported format.")
        rgb_image = image.convert("RGB")
        pixels = np.array(rgb_image)
        return pixels
    except FileNotFoundError:
        print(f"Error: File '{path}' not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")


def zoom(pixels: np.ndarray,
         x_start: int, x_end: int, y_start: int, y_end: int):
    """
    Zooms into a region of the image based on
    slicing indices and displays it with scaling axis.
    Turns image grey.
    """
    try:
        zoomed_image = pixels[x_start:x_end, y_start:y_end]
        grey_image = np.mean(zoomed_image, axis=2).astype(np.uint8)
        grey_image = np.expand_dims(grey_image, axis=-1)
        print("The shape of image is:", grey_image.shape)
        plt.imshow(grey_image, cmap="gray")
        plt.xticks(np.arange(0, grey_image.shape[1], 50))
        plt.yticks(np.arange(0, grey_image.shape[0], 50))
        return grey_image
    except Exception as e:
        print(f"An error occured: {e}")

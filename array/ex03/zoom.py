import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def zoom(pixels: np.ndarray,
         x_start: int, x_end: int, y_start: int, y_end: int):
    """
    Zooms into a region of the image based on
    slicing indices and displays it with scaling axis.
    Turns image grey.
    """
    try:
        zoomed_image = pixels[x_start:x_end, y_start:y_end]
        grey_iamge = np.mean(zoomed_image, axis=2).astype(np.uint8)
        grey_iamge = np.expand_dims(grey_iamge, axis=-1)
        print("New shape after slicing:", grey_iamge.shape)
        plt.imshow(grey_iamge, cmap="gray")
        plt.xticks(np.arange(0, grey_iamge.shape[1], 50))
        plt.yticks(np.arange(0, grey_iamge.shape[0], 50))
        plt.show()
        plt.close()
        return grey_iamge
    except Exception as e:
        print(f"An error occured: {e}")


def main():
    pixels = (ft_load("animal.jpeg"))
    if pixels is not None:
        print(pixels)
        print(zoom(pixels, x_start=100, x_end=500, y_start=450, y_end=850))


if __name__ == "__main__":
    main()

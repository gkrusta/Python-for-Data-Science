from load_image import ft_load
from load_image import zoom
import numpy as np
import matplotlib.pyplot as plt


def rotate(image):
    """
    Rotates an image 90 degrees counterclockwise
    and mirrors it horizontally.
    """
    rows, cols, channel = image.shape
    rotated_image = np.zeros((rows, cols, channel), dtype=image.dtype)

    for row in range(rows):
        i = 0
        for col in range(cols):
            rotated_image[i, rows - 1 - row] = image[row, col]
        i += 1
    return rotated_image


def main():
    pixels = (ft_load("animal.jpeg"))
    if pixels is not None:
        image = zoom(pixels, x_start=100, x_end=500, y_start=450, y_end=850)
        print(image)
        rotated_image = rotate(image)
        rotated_image = np.squeeze(rotated_image, axis=-1)
        print("New shape after Transpose:", rotated_image.shape)
        print(rotated_image)
        plt.imshow(rotated_image, cmap="gray")
        plt.show()
        plt.close()


if __name__ == "__main__":
    main()

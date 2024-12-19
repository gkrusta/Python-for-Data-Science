import numpy as np
from load_image import ft_load, display_image


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image."""
    inverted = 255 - array
    display_image(inverted, 0)
    return inverted


def ft_red(array) -> np.ndarray:
    """Applies a red filter to the image."""
    red = array.copy()
    red[:, :, 1] = 0
    red[:, :, 2] = 0
    display_image(red, 0)
    return red


def ft_green(array) -> np.ndarray:
    """Applies a green filter to the image."""
    green = array.copy()
    green[:, :, 0] = 0
    green[:, :, 2] = 0
    display_image(green, 0)
    return green


def ft_blue(array) -> np.ndarray:
    """Applies a blue filter to the image."""
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    display_image(blue, 0)
    return blue


def ft_grey(array) -> np.ndarray:
    """Converts the image to grayscale."""
    grey = np.mean(array, axis=2).astype(np.uint8)
    grey = np.expand_dims(grey, axis=-1)
    display_image(grey, 1)
    return grey


def main():
    array = ft_load("landscape.jpg")
    filters = [
        (ft_invert, 0),
        (ft_red, 0),
        (ft_green, 0),
        (ft_blue, 0),
        (ft_grey, 1),
    ]

    for filter_func, flag in filters:
        filter_func(array)


if __name__ == "__main__":
    main()

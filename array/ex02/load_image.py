from PIL import Image
import numpy as np


def ft_load(path: str):
    """
    Loads an image, converts it to RGB format,
    and returns its pixel data as a NumPy array.
    Prints the shape of the image.
    """
    try:
        image = Image.open(path)
        if not image or image.format != "JPEG":
            raise ValueError("Cannot open the file or unsupported format.")
        rgb_image = image.convert("RGB")
        pixels = np.array(rgb_image)
        print("The shape of image is:", pixels.shape)
        return pixels
    except FileNotFoundError:
        print(f"Error: File '{path}' not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    print(ft_load("landscape.jpg"))


if __name__ == "__main__":
    main()

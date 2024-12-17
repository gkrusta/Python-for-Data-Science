from PIL import Image
import numpy as np


def ft_load(path: str):
    try:
        image = Image.open(str)
        if not image or image.format is not "JPEG" or "JPG":
            raise("Error: Cannot open the file or unsupported format.")
        rgb_image = image.convert("RGB")
        pixels = np.array(rgb_image)
        print(pixels.shape)

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    print(ft_load("landscape.jpg"))


if __name__ == "__main__":
    main()
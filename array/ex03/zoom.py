import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load 


def zoom(pixels: np.ndarray, x_start: int, x_end: int, y_start: int, y_end: int):
	"""
	Zooms into a region of the image based on
	slicing indices and displays it with scaling axis.
	"""
	try:
		zoomed_image = [pixels[x_start:x_end, y_start:x_end]]
		#plt.imshow(zoomed_image)
		plt.xticks(np.arange(0, zoomed_image[1], 50))
		plt.yticks(np.arange(0, zoomed_image[0], 50))
		plt.show()
		return zoomed_image
	except Exception as e:
		print(f"An error occured: {e}")


def main():
	pixels = (ft_load("animal.jpeg"))
	if pixels is not None:
		zoom(pixels, x_start = 100, x_end = 500, y_start = 200, y_end = 600)


if __name__ == "__main__":
    main()

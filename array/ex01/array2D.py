import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes a 2D array, prints its shape,
    slices rows based on start and end indices,
    and returns the truncated array.
    """
    try:
        if not isinstance(family, list):
            raise TypeError("The input must be a list.")
        if not all(isinstance(row, list) for row in family):
            raise TypeError("All elements in the list must be lists.")
        row_len = len(family[0]) if family else 0
        if not all(len(row) == row_len for row in family):
            raise ValueError("All lists must have the same length.")
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("'start' and 'end' must be integers.")

        family = np.array(family, dtype=float)
        print("My shape is : ", family.shape)

        slieced_array = family[start:end]
        print("My new shape is : ", slieced_array.shape)
        result = slieced_array.tolist()
        return result

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    family = [["1.80", 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    print(slice_me(family, 0, 2))


if __name__ == "__main__":
    main()

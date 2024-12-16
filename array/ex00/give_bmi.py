def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:
    """
    Calculate the Body Mass Index (BMI) for a list of height and weight values.
    """
    try:
        if not all(isinstance(h, (int, float)) for h in height):
            raise TypeError("Height list must contain only int or float.")
        if len(height) != len(weight):
            raise ValueError("Lists must have the same length.")
        if not all(isinstance(w, (int, float)) for w in weight):
            raise TypeError("Weight list must contain only int or float.")
        if any(h == 0 for h in height):
            raise ValueError("Height values must be greater than 0.")

        return [w / (h * h) for h, w in zip(height, weight)]
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Determine if each BMI value exceeds a specified limit.
    """
    try:
        if not all(isinstance(b, (int, float)) for b in bmi):
            raise TypeError("Height list must contain only int or float.")
        if not isinstance(limit, int):
            raise TypeError("Limit list must contain only int.")

        return [b > limit for b in bmi]
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

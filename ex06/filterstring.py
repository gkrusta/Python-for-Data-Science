import sys
from ft_filter import ft_filter as my_filter


if __name__ == "__main__":
    """
    Handle user input and check for Assertion error
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("AssertionError: the arguments are bad")
        S = sys.argv[1]
        try:
            N = int(sys.argv[2])
            words = S.split()
            result = my_filter(lambda word: len(word) > N, words)
            print(result)
        except ValueError:
            raise AssertionError("AssertionError: the arguments are bad")

    except AssertionError as e:
        print(f"AssertionEroor: {e}")

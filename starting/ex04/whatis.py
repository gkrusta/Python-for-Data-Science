import sys


def odd_or_even():
    if len(sys.argv) < 2:
        return
    assert len(sys.argv) == 2, "Exactly one argument is required"

    try:
        nb = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")

    if nb % 2 == 0:
        print("I'm Even.")
    else:
        print('Im Odd.')


if __name__ == "__main__":
    try:
        odd_or_even()
    except AssertionError as e:
        print(f"AssertionEroor: {e}")

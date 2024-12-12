import sys


def ft_counter(text):
    """Counts characters and their specific types in a text"""
    lower = sum(1 for c in text if c.islower())
    upper = sum(1 for c in text if c.isupper())
    marks = sum(1 for c in text if not c.isalnum() and not c.isspace())
    space = sum(1 for c in text if c.isspace())
    digit = sum(1 for c in text if c.isdigit())

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{marks} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def main():
    """Handle user input and check for Assertion error"""
    if len(sys.argv) == 1:
        print("Enter a text: ")
        text = input()
    try:
        if len(sys.argv) > 2:
            raise AssertionError("AssertionError: too many arguments")
        else:
            text = sys.argv[1]
        ft_counter(text)
    except AssertionError as e:
        print(f"AssertionEroor: {e}")


if __name__ == "__main__":
    main()

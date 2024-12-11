import sys


MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ' ': '/'}


def to_morse_code():
    """
    Converts input string to morse code.
    """
    assert len(sys.argv) == 2, "the arguments are bad"
    msg = sys.argv[1]
    morse_code = ''
    if not all(char.isalnum() or char == ' ' for char in msg):
        raise AssertionError("the arguments are bad")
    for char in msg.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char]
    return morse_code


def main():
    """
    Handle user input and raise an Assertion
    error if input is invalid
    """
    try:
        msg = to_morse_code()
        print(msg)
    except AssertionError as e:
        print(f"AssertionEroor: {e}")


if __name__ == "__main__":
    main()

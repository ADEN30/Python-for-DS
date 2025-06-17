import sys
import string

"""
This script analyzes a given string and counts the number of:
- uppercase letters
- lowercase letters
- digits
- spaces (including tabs and line breaks)
- punctuation characters

Usage:
    python3 script.py "Your string here"
    python3 script.py          # Prompts the user to enter a string

Rules:
- If no argument is passed, the user will be prompted to enter the string.
- If more than one argument is passed, an AssertionError is raised.
- A carriage return (Enter) is counted as a space unless avoided
using Ctrl+D (EOF).
"""


def count_characters(text):
    """
    Analyzes the given text and prints the number of:

    - uppercase letters
    - lowercase letters
    - digits
    - spaces (including spaces, tabs, newlines)
    - punctuation characters

    Parameters:
        text (str): The string to analyze.
    """
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    digits = sum(1 for c in text if c.isdigit())
    spaces = sum(1 for c in text if c.isspace())
    punctuation = sum(1 for c in text if c in string.punctuation)
    all = sum(1 for c in text)

    print(f"The text contains {all}:")
    print(f"- {upper} upper letters")
    print(f"- {lower} lower letters")
    print(f"- {punctuation} punctuation marks")
    print(f"- {digits} digits")
    print(f"- {spaces} spaces")


def test_args(args: list):
    """_summary_
        Just check if args is > 2
    Args:
        agrs (_type_): lists of args
    throw AssertionError if args length < 2
    """
    if len(args) > 2:
        raise AssertionError("Too many arguments.")


def main():
    """
    Entry point of the program.

    - If exactly one argument is passed, it analyzes it.
    - If no argument is passed, prompts the user to enter a string.
    - If more than one argument is passed, raises an AssertionError.
    """
    args = sys.argv
    try:
        test_args(args)
        if len(args) == 2:
            text = args[1]
        else:
            text = input("What is the text to analyze?\n")

        count_characters(text)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()

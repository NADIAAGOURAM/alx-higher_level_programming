#!/usr/bin/python3
"""
function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """Prints text with added two newlines
    after each of these characters {'.', '?', ':'}.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = [".", "?", ":"]
    lines = text.splitlines()

    for line in lines:
        line = line.strip()
        if line:
            for char in line:
                print(char, end="")
                if char in punctuation_marks:
                    print("\n" * 2, end="")
            print()
        else:
            print()

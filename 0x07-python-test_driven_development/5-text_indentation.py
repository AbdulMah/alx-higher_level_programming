#!/usr/bin/python3
"""
Function to replace some characters with '\n\n'
"""


def text_indentation(text):
    """Prints a text with 2 new lines
    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.

    """
    special = ['.', '?', ':']
    if not isinstance(str, text):
        raise TypeError("text must be string")
    for x in text:
        print(x, end='')
        if x in special:
            print('\n\n', end='')

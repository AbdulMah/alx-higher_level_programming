#!/usr/bin/python3
"""
    Defines a function that prints a square
"""


def print_square(size):
    """
        Prints a square with the character "#".

        param: size(int) - the length of the square
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        for y in range(size):
            print("#", end='')
        print()

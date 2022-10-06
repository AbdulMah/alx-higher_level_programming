#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(mylist=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(mylist) == 0:
        return None
    result = mylist[0]
    i = 1
    while i < len(list):
        if mylist[i] > result:
            result = mylist[i]
        i += 1
    return result

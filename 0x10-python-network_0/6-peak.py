#!/usr/bin/python3
"""Defines a function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """
        Finds a peak in a list of unsorted integers
        Returns the value of the peak if found
    """
    num = len(list_of_integers)
    if num == 0:
        return None
    if num == 1:
        return list_of_integers[0]
    if num == 2:
        return max(list_of_integers)
    mid = num // 2
    if list_of_integers[mid] < list_of_integers[mid - 1]:
        # search left half
        return find_peak(list_of_integers[:mid])
    elif list_of_integers[mid] < list_of_integers[mid + 1]:
        # seach the right half
        return find_peak(list_of_integers[mid:])
    else:
        # the peak
        return list_of_integers[mid]

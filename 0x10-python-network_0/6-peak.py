#!/usr/bin/python3
"""Finding peak in list of ints
"""


def find_peak(list_of_integers):
    """Implementation
    """
    peak = None
    for ele in list_of_integers:
        if peak is None or peak < ele:
            peak = ele
    return peak

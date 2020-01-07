#!/usr/bin/python3


def increasing(list_of_integers):
    """ returns True if elements are increasing in the list"""
    for i in range(1, len(list_of_integers)):
        if list_of_integers[i - 1] > list_of_integers[i]:
            return False
    return True


def decreasing(list_of_integers):
    """ returns True if elements are decreasing in the list """""
    for i in range(1, len(list_of_integers)):
        if list_of_integers[i - 1] < list_of_integers[i]:
            return False
    return True


def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers """
    if not list_of_integers:
        return None
    if increasing(list_of_integers):
        return list_of_integers[-1]
    if decreasing(list_of_integers):
        return list_of_integers[0]
    for i in range(1, len(list_of_integers) - 1):
        if (list_of_integers[i] >= list_of_integers[i - 1] and
                list_of_integers[i] > list_of_integers[i + 1]):
            return list_of_integers[i]
        if (list_of_integers[i] > list_of_integers[i - 1] and
                list_of_integers[i] >= list_of_integers[i + 1]):
            return list_of_integers[i]
    return (list_of_integers[0])

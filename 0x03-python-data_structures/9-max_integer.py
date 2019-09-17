#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_number = my_list[0]
        for i in my_list[1:]:
            if max_number < i:
                max_number = i
        return max_number
    return None

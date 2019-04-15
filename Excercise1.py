""" Exercise 1
Author: Vivek Mistry
"""


def print_depth(data, level=1):
    """Print the depth of a given nested Dictionary
    Parameters:
        data - nested dictionary
    """
    tracker = level
    for k in data:
        if not isinstance(data[k], dict) or not k:
            print(k, tracker)
        else:
            print(k, tracker)
            print_depth(data[k], tracker + 1)


a = {"key1": 1, "key2": {"key3": 1, "key4": {"key5": 4}}}


print_depth(a, level=1)



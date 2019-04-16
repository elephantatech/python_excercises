""" Exercise 3
Author: Vivek Mistry
"""
import fnmatch
import re

def isMatch( s: str, p: str) -> bool:
    """
    Given an input string (s) and a pattern (p), implement wildcard pattern matching with support
    for '?' and '*'.

    :param s: input string
    :param p: pattern
    :return: true or false
    """
    if fnmatch.filter([s], p) == [s]:
        return True
    else:
        return False

print(isMatch("aa","*"))

print(isMatch("aa","?b"))


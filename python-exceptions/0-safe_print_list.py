#!/usr/bin/python3
"""Module for safe_print_list method."""


def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list."""
    nb_print = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            nb_print += 1
        except IndexError:
            break
    print()
    return nb_print

#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    This module prints x elements of a list.
    """
    count = 0

    # It iterates from 0 up to x.
    for i in range(x):
        try:
            # attempting to access and print the element at index i.
            # end="" ensures it prints on the same line.
            print("{}".format(my_list[i]), end="")

            # if the line above succeeded, it increments our counter.
            count += 1

        except IndexError:
            # if my_list[i] doesn't exist, an IndexError happens.
            # it catches it here and does nothing (pass) or break.
            # this prevents the program from crashing.
            pass

    # printing a new line at the end of the output
    print()

    # returns the actual number of items it managed to print
    return count

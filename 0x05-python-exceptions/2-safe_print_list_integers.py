#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    while i < x:
        try:
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            i += 1
        except (ValueError, TypeError):
            break
    print()
    return count

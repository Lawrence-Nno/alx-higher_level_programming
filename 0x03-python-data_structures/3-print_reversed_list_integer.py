#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    count = len(my_list)
    for i in reversed(range(count)):
        print('{}'.format(i))

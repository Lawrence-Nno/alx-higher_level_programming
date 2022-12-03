#!/usr/bin/python3
def no_c(my_string):
    string = ""
    ops = ['C', 'c']
    for i in my_string:
        if i not in ops:
            string += i
    return (string)


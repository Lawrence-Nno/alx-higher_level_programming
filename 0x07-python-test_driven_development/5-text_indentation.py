#!/usr/bin/python3

"""This function defines how a text is printed"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for delimeter in ".?:":
        i = (delimeter + "\n\n").join([index.strip(" ") for index in i.split(delimeter)])

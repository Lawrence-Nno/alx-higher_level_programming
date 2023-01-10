#!/usr/bin/python3
"""A file-appending function."""


def append_write(filename="", text=""):
    """Appends a string (text) to the end of a UTF8 text file (filename).
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

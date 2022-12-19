#!/usr/bin/python3
def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
       c = a / b
    except (TypeError, ZeroDivisionError):
        c = None
    finally:
        print("Inside result: {}".format(c))
    return c

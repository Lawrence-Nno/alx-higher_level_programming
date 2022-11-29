#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -1 * number
        print('{0}'.format((number % 10)), end="")
        return(number % 10)
    else:
        print('{0}'.format((number % 10)), end="")
        return(number % 10)

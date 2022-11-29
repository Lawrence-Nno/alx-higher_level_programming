#!/usr/bin/python3
for i in range(100):
    if (i % 10) > i//10 and i//10 >= 8:
        print('{0}{1}'.format((i//10), (i % 10)))
    elif i % 10 > i//10:
        print('{0}{1}, '.format((i//10), (i % 10)), end="")

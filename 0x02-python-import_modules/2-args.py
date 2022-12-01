#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argv_count = len(argv)
    index = 1
    if argv_count == 0:
        print("{0} arguments.".format(argv_count))
    elif argv_count == 1:
        print("{0} argument.".format(argv_count))
        print("{0}: {1}".format(index, sys.argv[1]))
    else:
        print("{0} arguments:".format(argv_count))
        while index <= argv_count:
            print("{0}: {1}".format(index, sys.argv[index]))
            index += 1

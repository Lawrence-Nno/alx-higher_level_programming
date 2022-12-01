#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    index = 1
    argv_count = len(argv)
    argv_sum = 0
    while index <= argv_count:
        argv_sum += int(sys.argv[index])
        index += 1
    print("{0}".format(argv_sum))

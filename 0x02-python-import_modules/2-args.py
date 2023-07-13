#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    if len == 0:
        print("{} arguments.".format(length))
    elif len == 1:
        print("{} argument:".format(length))
    else:
        print("{} arguments:".format(length))
        for i in range(1, length + 1):
            print("{:d}: {:s}".format(i, argv[i]))

#!/usr/bin/python3
charend = ", "
for a in range(0, 100):
    if a < 10:
        print("0{}".format(a), end=charend)
    else:
        if a == 99:
            charend = "\n"
        print("{}".format(a), end=charend)

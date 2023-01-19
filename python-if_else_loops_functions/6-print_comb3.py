#!/usr/bin/python3
for i in range (0, 10):
    for n in range (0, 10):
        if n == i or n < i:
            continue
        print("{}{}".format(i, n), end='')
        if i == 8 and n == 9:
            print("\n", end='')
            break
        print(', ', end='')


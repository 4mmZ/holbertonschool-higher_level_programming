#!/usr/bin/python3


def fizzbuzz():
    for n in range(1, 101):
        if n % 15 == 0:
            print("FizzBuzz", end=' ')
            continue
        elif n % 5 == 0:
            print("Buzz", end=' ')
            continue
        elif n % 3 == 0:
            print("Fizz", end=' ')
            continue
        print("{}".format(n), end=' ')

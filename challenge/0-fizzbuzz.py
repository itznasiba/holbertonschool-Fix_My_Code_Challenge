#!/usr/bin/python3
"""
FizzBuzz implementation
"""
import sys


def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.
    - For multiples of three print "Fizz"
    - For multiples of five print "Buzz"
    - For numbers which are multiples of both three and five print "FizzBuzz"
    """
    if n < 1:
        return

    tmp_ns = []
    for i in range(1, n + 1):
        if (i % 3) == 0 and (i % 5) == 0:
            tmp_ns.append("FizzBuzz")
        elif (i % 3) == 0:
            tmp_ns.append("Fizz")
        elif (i % 5) == 0:
            tmp_ns.append("Buzz")
        else:
            tmp_ns.append(str(i))
    print(" ".join(tmp_ns))


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)

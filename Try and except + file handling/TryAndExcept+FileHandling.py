#!/usr/bin/env python
"""
info about our project
"""

# import
import datetime

__author__ = "Senne De Winter"
__email__ = "senne.dewinter@student.kdg.be"
__status__ = "Production"


def main():
    try:
        number = int(input("Give me a random round number: "))
        if (number % 2) == 0:
            print("the number", str(number), "is even")
        else:
            print("the number", str(number), "is odd")
    except ValueError as err:
        text = open("log.txt", "w")
        text.write(str(err) + " : " + str(datetime.datetime.now()))
        print("Oops that was not a valid number:", err)
    finally:
        print("program has ended.")


if __name__ == '__main__':
    main()
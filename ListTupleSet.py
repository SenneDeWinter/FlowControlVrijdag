#!/usr/bin/env python
"""
bron:https://www.geeksforgeeks.org/difference-between-list-vs-set-vs-tuple-in-python/
"""


__author__ = "Senne De Winter"
__email__ = "senne.dewinter@student.kdg.be"
__status__ = "Production"


def main():
    # Creating a List
    List = []
    print("Blank List: ")
    print(List)

    # Creating a List of numbers
    List = [10, 20, 14]
    print("\nList of numbers: ")
    print(List)

    # Creating a List of strings and accessing
    # using index
    List = ["Geeks", "For", "Geeks"]
    print("\nList Items: ")
    print(List[0])
    print(List[2])

    # Creating an empty Tuple
    Tuple1 = ()
    print("Initial empty Tuple: ")
    print(Tuple1)

    # Creating a Tuple with
    # the use of list
    list1 = [1, 2, 4, 5, 6]
    print("\nTuple using List: ")
    print(tuple(list1))

    # Creating a Tuple
    # with the use of built-in function
    Tuple1 = tuple('Geeks')
    print("\nTuple with the use of function: ")
    print(Tuple1)

    # Creating a Set
    set1 = set()
    print("Intial blank Set: ")
    print(set1)

    # Creating a Set with
    # the use of Constructor
    # (Using object to Store String)
    String = 'GeeksForGeeks'
    set1 = set(String)
    print("\nSet with the use of an Object: ")
    print(set1)

    # Creating a Set with
    # the use of a List
    set1 = set(["Geeks", "For", "Geeks"])
    print("\nSet with the use of List: ")
    print(set1)


if __name__ == '__main__':    #code to execute if called from command-line
    main()
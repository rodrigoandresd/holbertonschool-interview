#!/usr/bin/python3
"""
Given a number n this method calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""


def copyAll(myList):
    """method that copy a str"""
    myList[0] = myList[0] + 1
    myList[2] = myList[1]
    # print("copy", myList)
    return (myList)


def paste(myList):
    """method that paste a str"""
    myList[0] = myList[0] + 1
    myList[1] = myList[1] + myList[2]
    # print("paste", myList)
    return (myList)


def minOperations(n):
    """method that calculates the fewest number of operations needed"""
    chars = "H"
    string = chars
    count = 0
    myData = [count, string, chars]

    if type(n) is not int:
        return (0)
    if n <= 1:
        return (0)
    while len(myData[1]) < n:
        if n % len(myData[1]) == 0:
            myData = copyAll(myData)
            myData = paste(myData)
        else:
            myData = paste(myData)
    return myData[0]

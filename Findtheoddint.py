# Given an array of ints, find the one that appears an odd number of times. Always one int that appears an odd number of times



def find_it(arr):

    for i in list(set(arr)):
        if arr.count(i) % 2 != 0:
            return (i)

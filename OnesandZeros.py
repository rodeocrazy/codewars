###Given an array of ones and zeroes, convert the equivalent binary value to an integer.

def binary_array_to_number(arr):

    number = int(0)
    power = ''

    for i in range(len(arr)):
        power = ((len(arr) - 1) - i)
        if arr[i] == 1:
            number += int(2**power)

    return number

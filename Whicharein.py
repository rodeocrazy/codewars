####List 1 is substring of List 2 and put into alphabetical order into list 3

def in_array(array1, array2):
    array3 = []

    for i in array1:
        for u in array2:
            if i in u and i not in array3:
                array3.append(i)
                array3.sort()

    return array3
#
##God Solution
#return sorted(i for i in array1 if any(i in u for u in array2))
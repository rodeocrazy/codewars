""" Given two integers a and b, which can be positive or negative, find the sum of all the ints between including them too and return it. If the two ints are equal return a or b.

Note: a and b are not ordered! """

# Add all ints in a range, if both ints the same print the ints

def get_sum(a,b):

    ints = (a, b)
    intslist= list(ints)
    numlist = []

    if ints[0] == ints[1]:
        return(ints[0])

    else:
        if intslist[0] < intslist[1]:
            for i in range(intslist[0], intslist[1] + 1, 1):
                numlist.append(i)
            return(sum((numlist)))
        elif intslist[1] < intslist[0]:
            for i in range(intslist[1], intslist[0] + 1, 1):
                numlist.append(i)
            return(sum((numlist)))
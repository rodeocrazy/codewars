"""
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.
"""

###Rules:
##No duplicates next to each other, preserver order, returns a list

def unique_in_order(iterable):

    newiterable = ""
    newlist = []

    if type(iterable) is list:

        for i in range(len(iterable)):
            ##First letter
            if i == 0:
                newlist.append(iterable[i])
            ###Body
            if 0 < i < (len(iterable) - 1):
                if iterable[i-1] != iterable[i]:
                    newlist.append(iterable[i])
            ##Last letter case
            if (len(iterable) - 1) == i:
                if iterable[i-1] != iterable[i]:
                    newlist.append(iterable[i])
        return newlist

    else: 

        for i in range(len(iterable)):
                ##First letter
            if i == 0:
                newiterable += str(iterable[i])
                    ###Body
            if 0 < i < (len(iterable) - 1):
                if iterable[i-1] != iterable[i]:
                    newiterable += str(iterable[i])
            ##Last letter case
            if (len(iterable) - 1) == i:
                if iterable[i-1] != iterable[i]:
                    newiterable += str(iterable[i])

        return list(newiterable)

###Notes: when in a for loop, the first and last positions of the list will cause problems
###An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

###Important conditions:
## Only letters, ignore letter case, consecutive or non-consecutive

def is_isogram(string):

    newstring = string.lower()

    for i in newstring:
        if newstring.count(i) > 1:
            return False
    
    return True
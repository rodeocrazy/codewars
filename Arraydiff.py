## Remove all values from list 2 from list 1 and print new list

def array_diff(a,b):
    for i in b:
        while i in a:
            a.remove(i)
    return a
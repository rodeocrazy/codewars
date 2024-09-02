## True or flase if value is narcissistic

def narcissistic(value):
    newvalue = 0
    valuelist = list(str(value))

    for i in valuelist:
        newvalue += int(i) ** len(valuelist)

    if value == newvalue:
        return(True)

    return(False)

##BEST SOLUTION
#def narcissistic(value):
#    return value == sum(int(x) ** len(str(value)) for x in str(value))
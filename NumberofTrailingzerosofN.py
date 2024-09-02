"""import math

def zeros(n):
    i = 1
    fact = math.factorial(n)

    while fact % (10 ** i) == 0:
        i += 1

    return(i-1) """

def zeros(n):
    i = 1
    zeros = 0

    while int(n / (5 ** i)) >= 1:
        zeros += int(n / (5 ** i))
        i += 1

    return zeros
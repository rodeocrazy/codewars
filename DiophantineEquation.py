##Find x,y when n given for equatin x^2-4*y^2=n, 
# in decreasing order of the postive x

##ex solEquaStr(12) --> "[[4,1]]"

import math #for sqrt

n = 69

#find type of n
if n % 2 == 0:
    ntype = "even"
else:
    ntype = "odd"

sol = []
xlst = []

##create list/revlist of n to iterate x and y
for i in (range(n)):
    xlst.insert(0, i+1)


# Adds 0 to list and creates reverse list
xlst.insert(0, 0)
revxlst = xlst[::-1]
#ylst = xlst

#brute force solution 
##Iterate both lists to find solutions
#basic optimization
#n**2 solution

"""
for i in revxlst:
    xvalue = (i**2)
    for u in ylst:
        yvalue = (4*(u**2))
        value = ((xvalue)-(yvalue))
        print("x:", i, "y:", u, "value:", value)
        
        #go to next value of x if value is lower than n
        if value < n or (i == u):
            break
        if value == n:
            sol.append([i, u])
            break
print(sol)

"""

# solution attempt 2 (use 1 loop) for value x solve for y where y will always be less than x
#still too slow with 50% speed increase of adding even and odd

for x in revxlst:
    #if n is odd x must be odd, if n is even x must be even
    if ntype == "odd" and (x % 2 != 0):
        numerator = ((x**2) - n)
        if numerator >= 0:
            y = math.sqrt((numerator)/4)
            if y.is_integer() == True:
                sol.append([x,int(y)])

    if ntype == "even" and (x % 2 == 0):
        numerator = ((x**2) - n)
        if numerator >= 0:
            y = math.sqrt((numerator)/4)
            if y.is_integer() == True:
                sol.append([x,int(y)])

print(sol)


# solution ended up being some weird even odd bullshit with floor division, I'm accepting my above answer
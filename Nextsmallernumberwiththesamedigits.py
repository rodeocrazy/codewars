#first didgit will be the same if another combination of other digits in the number are smaller than original value

#If next digit is greater than the last, it won't have a lesser value


# No leading zeros

#Can try collections.Counter() if this doenst work

import collections
import math

n = 2071

print(math.factorial(len(str(n))))

count = collections.Counter(list(str(n)))
shortlst = []


for i in range((10**((len(str(n))) - 1)), n):
    if list(str(i)).count(str(0)) == list(str(n)).count(str(0)):
        count2 = collections.Counter(list(str(i)))
        if count == count2:
            shortlst.append(i)

print(len(shortlst))

if shortlst == []:
    print(-1)

else:
    print(max(shortlst))
#Create all permutations of an input string and remove duplicates, if present.

#formula for # of permutations? n^r, aabb,

#find number of total permutaions
import math

string = 'ab'

temp = ""
numerator = math.factorial(len(string))
denomenator = 1

for i in string:
    if temp != i and string.count(i) > 1:
        temp = i
        denomenator *= math.factorial(string.count(i))

permutations = int(numerator/denomenator)

print("# of permutations:", permutations)


#constructor function:

for i in string:
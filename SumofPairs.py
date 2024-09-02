##check divisibility of s for all ints, only try adding divisible numbers

ints = [11, 3, 7, 5]
s = 10

divints = []
sumpair = []

for i in ints:
    if s / i >= 1 or i == 0:
        divints.append(i)

for i in range(len(divints)):
    for u in range(len(divints)):
        if u < (len(divints) - 1):
            if divints[i] + divints[(u+1)] == s:
                sumpair.append(divints[i])
                sumpair.append(divints[(u+1)])


print(sumpair)
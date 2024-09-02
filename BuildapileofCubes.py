import math

m = 1071225

left = 0
right = m
n = math.ceil((right + left)/2)
totalvolume = 0



while totalvolume != m and n != 1:
    totalvolume = 0
    while n >= 1:
        originaln = n
        totalvolume += n ** 3
        print(n, totalvolume)
        if totalvolume < m:
            left = n
            n = math.ceil((right + left)/2)
        if totalvolume > m:
            right = n
            n = math.ceil((right + left)/2)
        if totalvolume == m and n == 1:
            print(originaln)
            break
        n = math.ceil((right + left)/2)
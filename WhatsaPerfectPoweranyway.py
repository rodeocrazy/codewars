#### input ==n
### find m, k where m^k == n 
#### n = 343 7^3 not working because of repeating 9's or 0's. EDIT: FIXED BY ROUND UP


def isPP(n):
    print(n)
    k = 0
    m = 0
    for i in range(n):
        if (int(round(n ** (1/(i+2))))) ** (i+2) == n:
            m = n ** (1/(i+2))
            k = i+2
            print(int(m), k)
            return[int(round(m)), k]
    return None
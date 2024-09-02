args = [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
max = []
new = []
u = 0

for i in range(len(args)):
    u = 0
    if i < (len(args) - u):
        if u < 2:
            new.append(args[i])
        while args[i] - args[i+u] == (-1 * u):
            u += 1
            if i < (len(args) - u):
                continue
            
            else: break
        if i < (len(args) - u) and u >= 2:
                new.append('-')
                new.append(args[i+u-1])
                i += u


###unsolved



print(new)
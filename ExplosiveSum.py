n = 5
count = 0


for i in (range(1, n+1)):
    print(i, n % i)
    if n % i == 0:
        count += 1
    elif n % i == 1:
        count += 1
    elif n % i == 2:
        count += 2
    elif n % i == 3:
        count += 3
    elif n % i == 4:
        count += 5
    elif n % i == 5:
        count += 7


print(count)
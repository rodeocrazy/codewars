n = 7
k = 3
lst2 = []
count = 0

lst = []
for i in range(n+1):
    if i != 0:
        lst.append(i)

while lst != []:
    if count > len(lst):
        count = count % len(lst)
        print(count)
    if (k+count) < len(lst):
        lst2.append(lst[k+count-1])
        lst.remove(lst[k+count-1])
        count = k+count-1
        print(lst, lst2, count, 'if')
    elif (k+count) >= len(lst):
        m = (k+count) % len(lst)
        print(count)
        lst2.append(lst[m-1])
        lst.remove(lst[m-1])
        count = m - 1
        print(lst, lst2, count, 'elif')

print(lst2)
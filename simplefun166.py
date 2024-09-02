#smallest difference in goals between two teams score, return the index of the smallest difference where goals 2 is highest


goals1 = [1,2,3,4,5]
goals2 = [0,1,2,3,4]

tempgoals2 = -1

diff = []



for i, u in zip(goals1,goals2):
    diff.append(i-u)


if diff.count(max(diff)) > 1:
    print #last position of max(diff)
    index = diff.index(max(diff))

    for i in range(len(diff)):
        if diff[i] == max(diff) and (int(goals2[i]) > tempgoals2):
            tempgoals2 = i

else: 
    print(diff.index(max(diff)))

print(tempgoals2)

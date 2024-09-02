max_sequence = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


negativeints = 0 
maxsum = 0
tempsum = 0

for i in max_sequence:
    if i >= 0:
        tempsum += i
        print(tempsum)
    if i < 0:
        negativeints += 1
        #if 
    if tempsum >= maxsum:
        maxsum = tempsum
        print(maxsum)
        tempsum = 0 
            
if negativeints == len(max_sequence):
    print(0)


for i in max_sequence:
    

    
print(maxsum)
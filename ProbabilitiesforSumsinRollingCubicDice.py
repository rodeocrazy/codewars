#given a sum and an amount of dice, determine the probability of that dice roll


import itertools

def rolldice_sum_prob(sum_, dice_amount):

    dice_arr = [1,2,3,4,5,6]
    combinations = 0

    # return if sum_ is above max roll
    if sum_ > (dice_amount * 6):
        return 0


    # use itertools

    perms = itertools.product(dice_arr, repeat = dice_amount)
    for i in perms:
        if sum(i) == sum_:
            combinations += 1

    print((float((6) ^ (dice_amount))))
    return (float(combinations)) / (float((6) ** (dice_amount)))



"""
#try brute force first

# Based on dice_amount create loop to iterate through all dice arr's
#Can't create amount of for loops easily from user input so try recursion

while dice_amount != 0:

    for i in dice_arr:
        print(i)
        for u in dice_arr:
            print(i,u)
            for y in dice_arr:
                print(i,u,y)
    
    dice_amount -= 1
                
combinations = 0
"""


###Tickets are 25, must have change for 50 and 100 bills
def tickets(people):

    twenty = 0
    fifty = 0
    hundred = 0

    for i in people:
        if i == 25:
            twenty += 1
        elif i == 50:
            twenty -= 1
            fifty += 1
            if twenty < 0:
                return('NO')
        elif i == 100:
            if twenty >= 1 and fifty >= 1:
                twenty -= 1
                fifty -= 1
                hundred += 1
            elif twenty >= 3:
                twenty -= 3
                hundred += 1
            if (twenty or fifty) < 0:
                return('NO')
            
    if (twenty and fifty and hundred) >= 0:
        return('YES')


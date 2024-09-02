def rot13(message):

    cipher = ''

    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = lower.upper()

    for i in range(len(message)):
        if message[i].isupper() == True:
            cipher +=  upper[(upper.find((message[i])))-13]
        elif message[i].islower() == True:
            cipher += lower[(lower.find(message[i]))-13]
        else:
            cipher += message[i]

    return(cipher)
##Problem
#Make sure all words in a sentence are capitalized

#solution check to see if there is a space, if there is assume next word is start of sentence and capitalize

def to_jaden_case(string):
    newstring = ''

    if string[0].islower():
        newstring += string[0].capitalize()

    for i in range(len(string)):
    
        if string[i] != ' ' and string[i-1] != ' ': 
            newstring += string[i]
        if string[i] == ' ':
            newstring += ' ' + string[i+1].capitalize()
    

    return (newstring)

### Try Join method next time
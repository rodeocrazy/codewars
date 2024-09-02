def generate_hashtag(s):

    if s == "":
        return(False)

    split = (s.split(" "))
    newstr = ''
    newstr2 = ''
    print(split)

    for i in split:
        if i != "":
            newstr += (i.lower()) + ','
    
    print(newstr)
    
    split2 = newstr.split(",")
    
    print(split2)
    
    for i in split2:
        if i != "":
            newstr2 += i[0].upper() + i[1:]
    
    if newstr2 == "":
        return(False)

    newstr2 = '#' + newstr2
    
    print(newstr2)

    if len(newstr2) > 140:
        return(False)
    else:
        return(newstr2)
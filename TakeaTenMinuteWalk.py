#### (X,Y) coordinate after 10 moves needs to be (0,0)

def is_valid_walk(walk):
    return((len(walk) == 10 and ((walk.count('n') - walk.count('s')) == 0) and ((walk.count('e') - walk.count('w')) == 0)))
    
    
    """Xcoordinates = (0)
    Ycoordinates = (0)

    if len(walk) != 10:
        return(False)

    elif len(walk) == 10:
        for i in walk:
            if i == 'n':
                Ycoordinates += 1
            if i == 's':
                Ycoordinates -= 1
            if i == 'e':
                Xcoordinates += 1
            if i == 'w':
                Xcoordinates -= 1
        
        if Xcoordinates == 0 and Ycoordinates == 0:
            return(True)
        else:
            return(False) """

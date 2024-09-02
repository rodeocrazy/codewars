## seconds >= 0. Transformed minutes/seconds 00-59


def make_readable(seconds):
    
    HH = "00"
    MM = "00"
    SS = "00"
    
    if seconds == 0:
        return(str(HH)+":"+str(MM)+":"+str(SS))
    
    if seconds / 3600 >= 1:
        HH = str((seconds//3600))
        seconds -= (HH*3600)

    if seconds / 60 >= 1:
        MM = str((seconds//60))
        seconds -= (MM*60)

    SS = str(seconds)

    if len(HH) == 1:
        HH = "0" + HH
    if len(MM) == 1:
        MM = "0" + MM
    if len(SS) == 1:
        SS = "0" + SS

    return((HH)+":"+(MM)+":"+(SS))
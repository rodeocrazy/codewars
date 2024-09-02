###Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
##Requirements:
## Returns Boolean, case insensitive, any char.

def xo(s):
    
    ss = s.lower()
    if ss.count('x') == ss.count('o'):
        return True
    else: return False
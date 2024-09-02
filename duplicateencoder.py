###The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
###Ignore capitalizatoin

def duplicate_encode(word):

    word = word.lower()
    newword = ''

    for i in word:
        if word.count(i) > 1:
            newword += (')')
        else: newword += ('(')

    return newword

###Symbols
### End problem -> When rewriting the same string, when there was a bracket in the original string it would notice there were multiple after having changed initial characters.
### Solution was to write to new string instead of manipulating old string
dna = 'ATTGC'
complementary = ''

""" for i in dna:
    if i == 'A':
        complementary += ('C')
    elif i == 'T':
        complementary +=('G')
    elif i == 'C':
        complementary +=('A')
    elif i == 'G':
        complementary +=('T') """


print(dna.translate(str.maketrans("ATCG","TAGC")))


###use translation table solution above next time, can also use pairs
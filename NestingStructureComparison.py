def same_structure_as(original,other):

    print(str(original))

    #replace values to common and then replace and compare to oriingal

    for i in range(len(original)):
        original[i] = 1

    for i in range(len(other)):
        other[i] = 1

    if original == other:
        print(True)

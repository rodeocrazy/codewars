import itertools

code = [3,6,9]


for i in itertools.combinations_with_replacement([3,6,9], 3):
    print(i)
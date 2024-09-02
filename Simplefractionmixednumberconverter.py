from fractions import Fraction

s = "-10/7"

y = s.split('/')

print(y)

remainder = abs(int(y[0])) % int(y[1])

print(remainder)

wholenumber = int(int(y[0]) / int(y[1]))


fraction = Fraction(remainder / int(y[1])).limit_denominator(7)


answer = str(wholenumber) + " " + str(fraction)

print(answer)


# Take % and use remainder over denominator
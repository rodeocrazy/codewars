#Reduce the opposing directions to the best method of travel
arr = ['NORTH', 'EAST', 'NORTH', 'EAST', 'WEST', 'WEST', 'EAST', 'EAST', 'WEST', 'SOUTH']

North = 0
South = 0
East = 0
West = 0
Directions = []

for i in arr:
    if i == "NORTH":
        North += 1
    if i == "SOUTH":
        South += 1
    if i == "EAST":
        East += 1
    if i == "WEST":
        West += 1

print(North)
print(South)
print(East)
print(West)
print(range(North-South))
print(range(East-West))

if North - South > 0:
    for i in range(North-South):
        Directions.append("NORTH")
elif South - North > 0:
    for i in range(South-North):
        Directions.append("SOUTH")
if East - West > 0:
    for i in range(East-West):
        Directions.append("EAST")
elif West - East > 0:
    for i in range(West-East):
        Directions.append("WEST")


print(Directions)
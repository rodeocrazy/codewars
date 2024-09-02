### TOp left of matrix to bottom right, using NSEW movements

#can move if maze[0] = maze[1]

#count walls of everx row to quicklx check first if its even valid
##If anx rows have x walls

#Check possible movement from start position and then from new position


maze = [
   "......",
  "......",
  "......",
  "......",
  "......",
  "......"
]


start =[[0,0]]

legalmoves = []


for y in range(len(maze)): #Y coordinate
    for x in range(len(maze)): #X Coordinate
        if maze[y][x] == ".":
            if x != (len(maze) - 1):
                if maze[y][x] == maze[y][x+1]:
                    #print("Can Move Right", y, x)
                    legalmoves.append([y,x])
            if x != 0:
                if maze[y][x] == maze[y][x-1]:
                    #print("Can Move Left", y, x)
                    legalmoves.append([y,x])
            if y != 0:
                if maze[y][x] == maze[y-1][x]:
                    #print("Can Move Up", y, x)
                    legalmoves.append([y,x])
            if y != (len(maze) - 1):
                if maze[y][x] == maze[y+1][x]:
                    #print("Can Move Down", y, x)
                    legalmoves.append([y,x])



#Checks to see if the exit is apart of legal moves, automatically fails the maze if inaccessible 


print(legalmoves)

end = [(len(maze)-1), (len(maze)-1)]

if end in legalmoves:
    print("Exit is open")
else:
    print("Exit not accesible:", "False")


start =[0,0]


i = 1

while start != end:
    if start[0] != (len(maze)):
        start = [(start[0]+i), int(start[1])]
        print(start)
        if start == end:
            print('There is a pathway', 'True')
        if start not in legalmoves:
            print(start, "here")
            start = [(start[0]-i), (start[1]+i)]
            if start == end:
                print(start)
                print('There is a pathway', 'True')
            if start not in legalmoves:
                print(start)
                print("No Pathway", 'False')
                break
        if [(start[0]+i), start[1]] in legalmoves:
            start = [(start[0]+i), start[1]]
            if start == end:
                print(start)
                print('There is a pathway', 'True')
        print(start)
        if [(start[0]), ((start[1])+i)] in legalmoves:
            start = [(start[0]), ((start[1])+i)]
            if start == end:
                print(start)
                print('There is a pathway', 'True')
        if start == end:
            print(start)
            print('There is a pathway', 'True')
    
    elif start[1] != (len(maze)):
        start = [(start[0]), (start[1]+i)]
        if start not in legalmoves:
            print(start)
            print("No Pathway", 'False')
            break
        if start == end:
            print(start)
            print('There is a pathway', 'True')


###Current state: 50% of test cases work, cannot go back up if it needs to. Store previous move? Sometimes gets stuck in corners. If the end is open but blocked will sometimes get stuck in the loop.
##Create a function that temperentiates a polynomial for a given value of x.

## 6/16 passes

### find postition of x and iterate 1 -> position of x for proper coefficient


string = "x-66"
x = 3


#Potential New solution, read string left to right and store previous variable for comparison  (Logn)


temp = 0


#split at +'s
newstring = []
if string.count('+') > 0:
    newstring = string.split('+')

    print(newstring)

    temp = 0
    temp1 = ""
    for i in newstring:
        #print("i:", i)
        for u in range(len(i)):
            #print("u:", u, 'i[u]:', i[u])
            #exponents 2...n
            if u != (len(i)-1):
                if i[u] == 'x' and i[u+1] == '^':
                    
                    if i[0] == '-':
                        for t in range(1,(u)):
                            temp1 += i[t]
                        temp += (-1) * int(temp1) * (int(i[u+2])) *  (x ** (int(i[u+2]) - 1))

                    if i[0] != "-":
                        #print("here!")
                        for t in range(0,(u)):
                            temp1 += i[t]
                        #print(temp1)
                        temp += int(temp1) * (int(i[u+2])) * (x ** (int(i[u+2]) - 1))
                    
                    
                #exponent 1
                elif i[u] == 'x' and i[u+1] != '^':
                    temp1 = ""
                    if i[0] == '-':
                        if i[1] == 'x':
                            temp += (-1)
                        else: 
                            for t in range(0,(u)):
                                temp1 += i[t]
                        
                        temp += (-1) * int(temp1)
                        
                    if i[0] != "-":
                        if i[0] == 'x':
                            temp += (1)
                        else: 
                            for t in range(0,(u)):
                                temp1 += i[t]

                        temp += (1) * int(temp1)
                        
            if u == (len(i)-1):
                #print("here!")
                if i[u] == 'x':
                    temp1 = ""
                    if i[0] == '-':
                        if i[1] == 'x':
                            temp += (-1)
                        else: 
                            for t in range(0,(u)):
                                temp1 += i[t]
                        
                        temp += (-1) * int(temp1)
                        
                    if i[0] != "-":
                        if i[0] == 'x':
                            temp += (1)
                        else: 
                            for t in range(0,(u)):
                                temp1 += i[t]
                            temp += (1) * int(temp1)


if string.find('-') != 0:
    if string.count('-') > 0:
        newstring = string.split('-')

        print(newstring)

        temp = 0
        temp1 = ""
        for i in newstring:

            for u in range(len(i)):
                print("u:", u)
                #exponents 2...n
                if u != (len(i)-1):
                    if i[u] == 'x' and i[u+1] == '^':
                        if i[0] == '-':
                            for t in range(1,(u)):
                                temp1 += i[t]
                            temp += (-1) * int(temp1) * (int(i[u+2])) *  (x ** (int(i[u+2]) - 1))

                        if i[0] != "-":
                            if u == 0:
                                temp += (int(i[u+2])) *  (x ** (int(i[u+2]) - 1))
                            else:  
                                for t in range(0,(u)):
                                    print(i[t])
                                    temp1 += i[t]
                                
                                temp += int(temp1) * (int(i[u+2])) *  (x ** (int(i[u+2]) - 1))

                        
                    #exponent 1
                    elif i[u] == 'x' and i[u+1] != '^':
                        temp1 = ""
                        if i[0] == '-':
                            if i[1] == 'x':
                                temp += (-1)
                            else: 
                                for t in range(0,(u)):
                                    temp1 += i[t]
                            
                            temp += (-1) * int(temp1)
                            
                        if i[0] != "-":
                            if i[0] == 'x':
                                temp += (1)
                            else: 
                                for t in range(0,(u)):
                                    temp1 += i[t]

                            temp += (1) * int(temp1)

                if u == (len(i)-1):
                    print("Here!")
                    if i[u] == 'x':
                        temp1 = ""
                        if i[0] == '-':
                            print("Here!1")
                            if i[1] == 'x':
                                temp += (-1)
                            else: 
                                for t in range(0,(u)):
                                    print("Here!2")
                                    temp1 += i[t]
                            
                            temp += (-1) * int(temp1)
                            
                        if i[0] != "-" and u == 0:
                            print("Here!3")
                            if i[0] == 'x':
                                temp += (1)
                            
                            else: 
                                for t in range(0,(u)):
                                    temp1 += i[t]
                                temp += (1) * int(temp1)

                                
                        if u != 0:
                            temp -= (1)


                                
                  
print(temp)
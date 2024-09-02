#Add "1" to end of string with no int's
#Add 1 to int at end of string with an int


strng = "foobar00"
strngstrng = ""
zerostrng = ""
digitstrng = ""



if strng == "":
    print(1)

else:
    for i in strng:
        if i.isdigit() == True:
            if i == "0" and digitstrng == "":
                zerostrng += i
            
            else:
                digitstrng += i
        else:
            strngstrng += i

if digitstrng != "":
    digitstrng = str(int(digitstrng) + 1)
else:
    digitstrng = "1"

strng = strngstrng + zerostrng + digitstrng

print(strng)
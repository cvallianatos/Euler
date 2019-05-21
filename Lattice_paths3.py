'''

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?

'''

def nextNodeEast(myString, dimension):
        tempString = myString[-4:]
        myEdge = int(tempString[-2:]) + 1
        if myEdge > dimension:
                return myString
        else:
                myString = myString + " " + tempString[:2] + ("0000" + str(myEdge))[-2:]
                return myString

def nextNodeSouth(myString, dimension):
        tempString = myString[-4:]
        myEdge = int(tempString[:2]) + 1
        if myEdge > dimension:
                return myString
        else:
                myString = myString + " " + ("0000" + str(myEdge))[-2:] + tempString[-2:]
                return myString

def longestPath(anyList):
    maxLength = 1
    for i in anyList:
        if maxLength < len(i):
            maxLength = len(i)
    return maxLength

def cleanPath(anyList):
    tempList = []
    x = longestPath(anyList)
    for i in anyList:
        if len(i) >= x:
            tempList.append(i)
    return tempList

def confirmComplete(anyList, dimension):
    flag = True
    myDimension = ('0000' + str(dimension))[-2:]
    myDimension = myDimension + myDimension
    for i in anyList:
        if i[-4:] != myDimension:
            flag = False
            break
    return flag

def findPaths(dimension):
    myPaths = []
    myPaths.append('0000')
    while (confirmComplete(myPaths,dimension) != True):
        k = len(myPaths)
        for i in range(k):
            myPaths.append(nextNodeEast(myPaths[i],dimension))
            myPaths.append(nextNodeSouth(myPaths[i],dimension))
        myPaths = cleanPath(myPaths)
    return myPaths

method = input("For a single dimension press 1 else press any other key:")

if method == "1":
    dimension = int(input("Enter Dimension: "))
else:
    dimension = int(input("Enter max dimension: "))

if method == "1":
    myPaths = findPaths(dimension)
    print("For ", dimension, " there are ", len(myPaths), " paths")
else:
    for j in range(2, dimension + 1):
        myPaths = findPaths(j)
        print("For ", j, " there are ", len(myPaths), " paths")

if method == "1":
    print ("----------------------------------------")

    for i in range(dimension + 1):
        for j in range(dimension + 1):
            print (("00" + str(i))[-2:] + ("00" + str(j))[-2:] + " ", end='')
        print()

    print ("----------------------------------------")

    j = 1
    for i in myPaths:
        print(j, " -> ",i)
        j = j + 1
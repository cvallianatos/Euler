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

myPaths = []

# iteration 0
myPaths.append('0000')
print(myPaths)
k = len(myPaths)
# iteration 1
for i in range(k):
    myPaths.append(nextNodeEast(myPaths[i],2))
    myPaths.append(nextNodeSouth(myPaths[i],2))

print(myPaths)
myPaths = cleanPath(myPaths)
print(confirmComplete(myPaths,2))

#iteration 2
k = len(myPaths)
for i in range(k):
    myPaths.append(nextNodeEast(myPaths[i],2))
    myPaths.append(nextNodeSouth(myPaths[i],2))

print(myPaths)
myPaths = cleanPath(myPaths)
print(confirmComplete(myPaths,2))

#iteration 3
k = len(myPaths)
for i in range(k):
    myPaths.append(nextNodeEast(myPaths[i],2))
    myPaths.append(nextNodeSouth(myPaths[i],2))

print(myPaths)
myPaths = cleanPath(myPaths)
print(confirmComplete(myPaths,2))

#iteration 4
k = len(myPaths)
for i in range(k):
    myPaths.append(nextNodeEast(myPaths[i],2))
    myPaths.append(nextNodeSouth(myPaths[i],2))

print(myPaths)
myPaths = cleanPath(myPaths)
print(myPaths)

print(confirmComplete(myPaths,2))
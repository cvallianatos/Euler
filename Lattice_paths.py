'''

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?

'''

def nextNodeEast(myString, dimension):
        tempString = myString[-4:]
        myEdge = int(myString[-2:]) + 1
        if myEdge > dimension:
                return myString
        else:
                myString = myString + " " + tempString[:2] + ("0000" + str(myEdge))[-2:]
                return myString

def nextNodeSouth(myString, dimension):
        tempString = myString[-4:]
        myEdge = int(myString[:2]) + 1
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

myPaths = []

myPaths.append('0000')

x = len(myPaths)

for i in range(x):
        myPaths.append(myPaths[i] + ' 0001')
        myPaths.append(myPaths[i] + ' 1000')

print(myPaths)
myPaths = cleanPath(myPaths)
print(myPaths)

print ('-------------')

x = len(myPaths)

for i in range(x):
        myPaths.append(myPaths[i] + ' 1010')
        myPaths.append(myPaths[i] + ' 0020')
print(myPaths)
myPaths = cleanPath(myPaths)
print(myPaths)

print(nextNodeEast('0000 0001 0101',2))
print(nextNodeSouth('0000 0001 0002',2))
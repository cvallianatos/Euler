'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 
is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant
 if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as
 the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater 
 than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced 
 any further by analysis even though it is known that the greatest number that cannot be expressed as the 
 sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

'''

def sumUpList(myList):
    sum = 0
    for i in myList:
        sum = sum + i
    return sum
    
def findDivisors(myNum):
    myList = []
    for i in range(1,myNum):
        if (myNum%i) == 0:
            myList.append(i)
    if myNum ==1:
        myList = [1]
    return myList

def isAbundant(myNum):
    if myNum < sumUpList(findDivisors(myNum)):
        return True
    else:
        return False

myInput = int(input("Enter target number: "))
sum = 0
for i in range(myInput):
    print(i)
    myFlag = False
    for j in range(1,1+int(i/2)):
        a = i - j
        if (isAbundant(a) and isAbundant(j)):
            myFlag = True
            break
    if myFlag == False:
        sum = sum + i
print(sum)
        
   

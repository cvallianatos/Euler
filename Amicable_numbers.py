
'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called 
amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

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

myInput = int(input("Enter target number: "))
amicableSum = 0
for n in range(1,myInput):
    myList1 = findDivisors(n)
    mySum1 = sumUpList(myList1)
    print(n, " -> ", myList1, " Sum = ", mySum1,end='')
    myList2 = findDivisors(mySum1)
    mySum2 = sumUpList(myList2)
    print(" -- ", myList2," Sum = ", mySum2,end='')
    if n == mySum2:
        if mySum1 != mySum2:
            print ("****************")
            amicableSum = amicableSum + n + mySum1
    print()
print ("----------------------")
print(amicableSum/2)
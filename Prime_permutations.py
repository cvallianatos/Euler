'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
(i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, 
but there is one other 4-digit increasing sequence.
What 12-digit number do you form by concatenating the three terms in this sequence?

Algorithm
=========
Get all primes from 1000 to 10000
For each prime, run permutations
Check if each permutation is prime
For each permutation find distance from original prime number
Do this for the next permutation and find out if distance is the same
If so, for ll permutations then this is the target number
Concatenate to a 12-digit number
'''

import itertools as iter

def isPrime(n):

    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True

myList = []
x = iter.permutations('1487',4)
for i in x:
    myNum = int(''.join(i))
    if isPrime(myNum):
        myList.append(myNum)
        print(myNum)
myList.sort()
print(myList)

myLength = len(myList)
myDict = {}

for j in range (1,myLength):
    for i in range(j,myLength):
        delta = myList[i]-myList[i-j]
        strDelta = str(myList[i]) +  " - " + str(myList[i-j])
        myDict[strDelta] = delta
        print(myList[i], " - ", myList[i-j], " = ", delta )
    print("-----------------------------")
print(myDict)
# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# 
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

import itertools as it

def isPrime(n) : 
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

def buildPrimeList(primeList, primeLimit):
    for i in range(1,primeLimit):
        if (isPrime(i)):
            primeList.append(i)
    return 

#
# Main program
#

myLimit = 30
myBoundary = 100
myList =[]
buildPrimeList(myList,myLimit)
print(myList)
myLength = len(myList)
print("-------")
print(myLength)
print("-------")

largestSum = 0
sum = 0
for j in range(myLength+1,2,-1):
    x = it.combinations(myList, j)
    for y in x:
        print(y, end='')
        sum = 0
        for k in range(j):
            sum = sum + y[k]
        if (sum >= myBoundary):
            print (" = ", sum, " ** MORE THAN BOUNDARY **")
            break
        if (isPrime(sum)):
            print (" = ",sum, " <- PRIME ->")
        else:
            print (" = ",sum)

#            if sum < myLimit:
#                print(y)
#                print(" SUM = ", sum)
#                print ("****************")
#                if sum > largestSum:
#                    largestSum = sum

        
#print("Largest sum is: ", largestSum)
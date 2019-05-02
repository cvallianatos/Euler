# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# 
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

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

def calcLargestSum(primeList, myBoundary):

    myList = []
    longestList = []
    longestSum = 0
    longestLength = 0
    sum = 0
    
    for i in primeList:
        myList.append(i)
        sum = sum + i
        if (sum < myBoundary):
            if (isPrime(sum)):
                longestSum = sum
                myLength = len(myList)
                if (myLength > longestLength):
                    longestLength = myLength
                    longestList = myList
        else:
            break
    return longestList, longestSum, longestLength

# Main program

myLimit = 4000
boundary = 1000000
myPrimes = []
buildPrimeList(myPrimes,myLimit)
numberOfPrimes = len(myPrimes)
largestSum = 0
largestList = []
longestLength = 0
for j in range(numberOfPrimes):
    result = calcLargestSum(myPrimes[j:],boundary)
    if result[2] > longestLength:
        longestLength = result[2]
        largestList = result[0]
        largestSum = result[1]
print (largestList)
print ("SUM= ", largestSum)
print("LENGTH= ", longestLength)
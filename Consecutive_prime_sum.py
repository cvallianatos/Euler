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

#
# Main program
#

myLimit = 30
myList =[]
longestSum = 0
sum = 0
for i in range(1,myLimit):
    if (isPrime(i)):
        print("i = ", i)
        myList.append(i)
        print(myList)
        sum = sum + i
        print("sum = ",sum)
        print("-------")
        if (sum < myLimit):
            if (isPrime(sum)):
                longestSum = sum
                print("**************")
                print("longest sum = ",longestSum)
                print("**************")
        else:
            break
print(longestSum)
print(myList)
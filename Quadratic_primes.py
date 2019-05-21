'''
Euler published the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. 
However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41
 is clearly divisible by 41.

Using computers, the incredible formula  n² – 79n + 1601 was discovered, which produces 80 primes for the consecutive 
values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000
where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number
 of primes for consecutive values of n, starting with n = 0.
'''

#time module for execution time
import time
import sys
sys.path.append(r'/Users/chris/Dropbox/Projects/cnv')

import cnv

def quadratic(a,b):
    primeCount = 0
    flag = True
    n = 0
    while flag:
        f = abs((n**2) + (n*a) + b)
        if (cnv.isPrime(f)==True):
            primeCount = primeCount + 1
            n = n + 1
        else:
            flag = False  
    return f, primeCount


#time at the start of program
start = time.time()

maxCount = 0
for a in range(-999,1000):
    for b in range(-999,1001):
        x,y = quadratic(a,b)
        if y > maxCount:
            maxCount = y
            myA = a
            myB = b
        print (a, " ", b, "maxCount = ", maxCount)
print("****************************")
print(myA," ** ", myB, " ** ", myA * myB, " *** ", maxCount)

#time at the end of execution
end = time.time()

#printing the total time for execution
print (end-start)
'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

'''

from decimal import Decimal
from fractions import Fraction

def allDigitsSame(myStr):
    if myStr.count(myStr[0]) == len(myStr):
        return True
    return False

def getRecSubStr(myStr):
    maxCycle = 1
    maxStr = ""
    for i in range(0,len(myStr)):
        for j in range(i+1,len(myStr)+1):
            mySub = myStr[i:j]
            if myStr.count(mySub) > 1:
                if maxCycle < j - i:
                    maxCycle = j -i
                    maxStr = mySub
    return maxStr

longestLength = 1
longestCycle = ""
for i in range(1,2001):
    myStr = str(Decimal.from_float(1/i))[2:]
    cycle = getRecSubStr(myStr)
    cycleLength = len(cycle)
    print (i," --- ",myStr, " --- ", cycle, " --- ", cycleLength, end='')
    if (longestLength < cycleLength) and (allDigitsSame(cycle) == False):
        print(" ********* ")
        longestLength = cycleLength
        longestCycle = cycle
        d = i
    print()
print(d, " -- ", longestCycle, " -- ", longestLength)
'''
a =  getRecSubStr("23142754804914299467653456348114275")
print (a)
'''
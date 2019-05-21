'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and 
product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''
sum = 0
myList = []
for i in range(1,10000):
    for j in range(1,10000):
        k = i * j
        myStr = str(i) + str(j) + str(k)
        if len(myStr) > 9:
            break
        flag = False
        for x in range(1,10):
            myCount = myStr.count(str(x))
            if myCount != 1:
                flag = False
                break
            else:
                flag = True
        if flag and myStr.count("0") == 0:
            myList.append(k)

no_dupes = [x for n, x in enumerate(myList) if x not in myList[:n]]
for a in no_dupes:
    sum = sum + a
print(no_dupes)
print("********************")
print("SUM is ", sum)
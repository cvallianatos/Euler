'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''
sum = 1
for n in range(3,1002,2):
    topLeft = (n**2) - (n-1)
    topRight = topLeft + (n-1)
    bottomLeft = topLeft - (n-1)
    bottomRight = bottomLeft - (n-1)
    sum = sum + topLeft + topRight + bottomLeft + bottomRight
    print (n)
    print(topLeft, " ", topRight)
    print(bottomLeft, " ", bottomRight)
    print(sum)
    print("***************")
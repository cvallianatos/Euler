# Highly divisible triangular number
# Problem 12 
# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th 
# triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

# 1: 1
# 3: 1,3
# 6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?

# Open output file
myFile = File.open("euler12-output.txt", "w")

target = 500
a = Array.new
i = 1
flag = true
numberOfDivisors = 0
while flag
	a[i] = 0
	for j in 1..i
		a[i] = a[i] + j
	end
	
	myFile.print a[i], " "
	count = 1
	for j in 1..a[i]
		if a[i] % j == 0
			count = count + 1
			myFile.print j, " "
		end
	end
	
	myFile.print " count is : ", count - 1, "\n"
	print a[i], " --> ", count, "\n"
	if count - 1 > target
		flag = false
	end
	
	i = i + 1
end

myFile.close  

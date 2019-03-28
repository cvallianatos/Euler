# Longest Collatz sequence
# Problem 14 
# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 
# terms. Although it has not been proved yet (Collatz Problem), it is thought that all 
# starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

def collatz (arg)
	if arg % 2 == 0
		arg = arg /2
	else
		arg = (3 * arg) + 1 
	end
end

# Open output file
myFile = File.open("euler14-output.txt", "w")

mostFactors = 0
mostNumber = 0
target = 1000
for k in (target).downto(13)
	i = k
	numberOfFactors = 1
	while true
		print i, " -> "
		myFile.print i, " -> "
		j = collatz(i)
		i = j
		numberOfFactors = numberOfFactors + 1
		if i == 1
			print i
			myFile.print i
			break
		end
	end
	if mostFactors < numberOfFactors
		mostFactors = numberOfFactors
		mostNumber = k
	end
	
	print " == Number of factors: ", numberOfFactors, "\n"
	myFile.print " == Number of factors: ", numberOfFactors, "\n"
end

	print "**************************************", "\n"
	print mostNumber, " produced most Collatz factors ", mostFactors, "\n"
	print "**************************************", "\n"
	
	myFile.print "**************************************", "\n"
	myFile.print mostNumber, " produced most Collatz factors ", mostFactors, "\n"
	myFile.print "**************************************", "\n"

myFile.close  
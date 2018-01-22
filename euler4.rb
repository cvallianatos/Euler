# Largest palindrome product
# Euler Problem 4 
# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
result = 0
temp = 0

for i in 999.downto(1)
	for j in 999.downto(1)
		x = i * j
				
		leftToRight = x.to_s
		rightToLeft = leftToRight.reverse
		
		if leftToRight == rightToLeft
			temp = x
			if result < temp
				result = temp
				print i, "-", j, " ----->",  x, "======", leftToRight, " == ", rightToLeft,"\n"
			end
		end
	end
end

puts "The largest palindrome is: "
puts result

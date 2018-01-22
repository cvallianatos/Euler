# Summation of primes
# Problem 10 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

require 'prime'

target = 2000000

i = 1
sum = 0
z = 1

while z < target do
	x = Prime.first i
	z = x.max
	if z < target 
		sum = sum + z
	end
	i = i + 1

	if i % 1000 == 0
		print i, ").", z, " ----- ", sum
		puts ""
	end
	
end
puts "=============================="
puts "SUM is"
puts sum

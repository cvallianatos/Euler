# Euler problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

require 'prime'

# puts Prime.first 20

x = Prime.prime_division(600851475143)
lengthOfX = x.length

for i in 0..lengthOfX-1
	puts x[i][0]

end

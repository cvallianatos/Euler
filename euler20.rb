# Factorial digit sum
# Problem 20 
# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

def factorial(n)
	if n < 0
		return nil
	end
	result = 1
	while n > 0
		result = result * n
		n -= 1
	end
 	return result
end

puts "Enter target factorial:"
input = gets
num = input.to_i
str = factorial(num).to_s
len = str.length

sum = 0
for i in 0..len - 1
	sum = sum + str[i].to_i
end

puts str
puts sum



# Euler problem 2
# Sum of all even fibonacci numbers below an upper limit
# Each new term in the Fibonacci sequence is generated by adding the 
# previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not 
# exceed four million, find the sum of the even-valued terms.



puts "Enter upper limit number: "
num = gets.to_i

x =1
y = 1
z = 0
sum = 0

while z <= num do
	puts z	
	z = x + y
	if (z % 2 == 0)
		sum = sum + z
	end
	x = y
	y = z

end
puts "The sum of even fibonacci numbers are"
puts sum

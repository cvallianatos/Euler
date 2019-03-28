# Power digit sum
# Problem 16 
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 21000?

x = 1
for i in 1..1000
	x = x * 2
end

puts x
y = x.to_s
resultLength =  y.length - 1

puts resultLength

sum = 0	
for j in 0..resultLength
	sum = sum + y[j].to_i
end

puts sum
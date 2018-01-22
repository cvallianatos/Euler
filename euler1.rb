# This is the Euler 1 challenge.
# Looking for the sum of all integers that are divisible by 3 or 5

puts "Starting Euler 1 challenge..."
puts "Enter the upper limit number: "
num = gets.to_i
sum = 0
puts sum
for i in 1..num-1
   if (i % 3 == 0) or (i % 5 == 0)
	puts i
      	sum = sum + i
   end
end

puts "The sum is ", sum
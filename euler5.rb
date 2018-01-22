# Smallest multiple
# Problem 5 
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without 
# any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 
# to 20?

flag = true 
i = 1

while flag
	s = 0
	for j in 2..20
		s = s + (i % j)
	end
	
	if s == 0
		flag = false
	else
		i = i + 1
	end
	if i % 100000 == 0
		print i, " - ", s, "\n"
	end
	
end
puts "================"
puts i

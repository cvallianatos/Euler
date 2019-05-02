# Special Pythagorean triplet
# Problem 9 
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

puts "Enter target"
input = gets
target = input.to_i
solution = false

for a in 1..target
	for b in 2..target
		for c in 3..target
			if a + b + c == target
				if (a * a ) + (b * b) == (c * c) 
					result = a * b * c
					print "Found solution for target ", target, "\n"
					puts "==============================="
					print "a =  ", a, " b = ", b, " c = ", c, "\n"
					print "a * b * c = ", result, "\n"
					solution = true
				end
			end
			if solution
				break
			end
		end
		if solution
			break
		end
	end
	if solution
		break
	end
end

if solution == false
	print "there is no solution for target ", target
end
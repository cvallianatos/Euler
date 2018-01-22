# Lattice paths
# Problem 15 
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

# Initialize array with 0's
# When an array node is visited the value changes to 1

size = 3
a = Array.new(size) {Array.new(size)} 

for i in 0..size - 1
	for j in 0..size - 1
		a[i][j] = 0
		print "a[", i, ",", j, "] = ", a[i][j], "\n"
	end
end

gets

i = 0
j = 0

while a[2][2] == 0
	# When in position a(i,j) we can go to a(i+1,j) or a(i,j+1)
	a[i][j] = 1
	print "a[", i, ",", j, "] = ", a[i][j], "\n"
	if i < size - 1
		i = i + 1
		a[i][j] = 1
	else
		if j < size - 1
			j = j + 1
			a[i][j] = 1
		end
	end
end
print "a[", i, ",", j, "] = ", a[i][j], "\n"

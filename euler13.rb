# Large sum
# Problem 13 
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

fname = "euler13.txt"
a = Array.new
i = 1
File.open(fname).each do |line|
	a[i] = line.to_i
	i = i + 1
end
sum = 0
for j in 1..100
	print a[j], "\n"
	sum = sum + a[j]
end

print "\n\n*****************************\n"
print sum
print "\n\n*****************************\n"

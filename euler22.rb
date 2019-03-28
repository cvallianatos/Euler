# Names scores
# Problem 22 
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

alfa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

file = File.open("names.txt", "r")
myFile = File.open("euler22-output.txt", "w")

contents = file.read
extract = contents.split(',')
arrayLength = extract.length - 1
extract.sort!
sum = 0
for i in 0..arrayLength
	extract[i] = extract[i].gsub(/["]/,'')
	tempStr = extract[i].split(//)
	tempStrLength = tempStr.length - 1
	strSum = 0
	print i+1, "). "
	myFile.print i+1, "). "
	for j in 0..tempStrLength
		loc = alfa.index(tempStr[j]) + 1
		strSum = strSum + loc
		print " ", loc
		myFile.print " ", loc
	end
	print " ", extract[i], "  ---> ", strSum * (i+1), "\n"
	myFile.print " ", extract[i], "  ---> ", strSum * (i+1), "\n"
	sum = sum + (strSum * (i+1))
end

print "============================\n"
print sum, "\n"
myFile.print "============================\n"
myFile.print sum, "\n"

myFile.close  


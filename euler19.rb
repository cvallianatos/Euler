# Counting Sundays
# Problem 19 
# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

startDate = Time.new(1901, 1, 1)
endDate = Time.new(2000, 12,31)
print startDate, " ----> ", startDate.wday, "\n"

# Add 1 day
newDate = startDate + 86400
sum = 0
while newDate <= endDate
	newDate = newDate + 86400
	if (newDate.day == 1 and newDate.wday == 0)
		print newDate, " ----> ", newDate.wday, "\n"
		sum = sum + 1
	end
end

print "*************************\n"
print "There are ", sum, " Sundays that fell on the first of the month in te 20th century\n"






# UA permutation is an ordered arrangement of objects. For example, 
# 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all 
# of the permutations are listed numerically or alphabetically, we call it lexicographic 
# order. The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

def Lexicographic(myString)

  origArray = myString.split(//)
  newArr = origArray.permutation.to_a
  counter = 1
  newArr.each do |x|
    if counter == 1000000
       print counter, "--> ", x.join, "\n"
       break
    else
      counter = counter + 1
    end
  end
end

# keep this function call here    
timer_start = Time.now
Lexicographic(STDIN.gets.chomp)
puts "Elapsed Time: #{(Time.now - timer_start)*1000} milliseconds"
#.any? { |obj| block } => true or false
#["ant", "bear", "cat"].any? { |word| word.length >= 3 }

#.each => calls block once for each element in ruby self, passing that element as a block parameter.
#["ant", "bear", "cat"].each { |word| print word, "--" }

#.collect { |obj| block } => returns a new array with the results of running block once for every element in enum
#print (1..4).collect { |i| i*i }
#print (1..4).collect { "cat" }

#.detect/.find => returns the first for which block is not false.
#(1..10).detect { |i| i %5 == 0 and i % 7 == 0 }
#print (1..100).detect { |i| i %5 == 0 and i % 7 == 0 }

#.find_all { |obj| block } or .select { |obj| block } => returns an array containing all elements of enum for which block is not false
#print (1..10).find_all { |i| i % 3 == 0 }

#.reject { |obj| block } => opposite of find_all
#print (1..10).reject { |i| i % 3 == 0 }

#.upto(limit) => iterates block up to the int number
#5.upto(10) { |i| print i, " " }


x = (1..5)
puts x.class
puts x.include?(3)
puts x.last
puts x.max
puts x.min
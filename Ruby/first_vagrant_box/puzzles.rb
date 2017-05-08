#1.
#x = [3,5,1,2,7,9,8,13,25,32]
#sum = 0
#arr = []
#x.each do |number| 
#    "Sum: #{sum += number}"
#end
#puts sum
#print x.find_all {|number| number > 10}

#2
#x = ["John", "KB", "Oliver", "Cory", "Matthew", "Christopher"]
#x.shuffle.each {|name| puts name if name.length > 5}

#3
#def shuf_alph
#alphabet = ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#alphabet_shuf = alphabet.shuffle
#print alphabet_shuf
#    if alphabet_shuf[0] == "a"
#        puts "Message"
#    elsif alphabet_shuf[0] == "e"
#        puts "Message"
#    elsif alphabet_shuf[0] == "i"
#        puts "Message"
#    elsif alphabet_shuf[0] == "o"
#        puts "Message"
#    elsif alphabet_shuf[0] == "u"
#        puts "Message"
#    end
#puts alphabet_shuf[0]
#puts alphabet_shuf[-1]

#end

#shuf_alph

#4
#print 10.times.map{ 55 + Random.rand(46) }

#5
#arr = 10.times.map{ 55 + Random.rand(46) }
#print arr.sort
#puts arr.max
#puts arr.min

#6
#puts 5.times.map{ (65+rand(26)).chr }.join

#7
#arr = []
#10.times do
#    arr << 5.times.map{ (65+rand(26)).chr }.join
#end
#print arr
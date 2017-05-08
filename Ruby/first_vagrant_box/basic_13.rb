#1. Print 1-255
#x = (1..255)
#x.each {|number| puts number}

#2. Print odd numbers between 1-255
#x = (1..255)
#x.each {|number| puts number if number.odd?}

#3. Print Sum
#x = (0..255)
#sum = 0

#for i in x
#    sum += i
#    puts "Number is #{i} Sum:#{sum}"
#end


#4. Iterating through an array

#x = [1, 3, 5, 7, 9, 13]

#x.each {|number| puts number}

#5. Find Max

#x = [1, 3, 5, 7, 9, 13, -5, 64]
#puts x.max

#6 Get Average
#x = [2, 10, 3, 7, 9 , 100]
#sum = 0
#x.each {|number| puts sum += number}
#avg = sum/x.length
#puts avg

#7 Array with Odd Numbers
#x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#x.each {|number| puts number if number.odd?}

#8 Greater Than Y
#x = [1, 3, 5, 7]
#y = 3
#count = 0

#for i in x
#    if i > y
#        count += 1
#    end
#end
#puts count



#9 Square the values
#x = [1, 5, 10, -2]
#puts x.collect {|number| number * number}

#10 Eliminate Negative Numbers
#x = [1, 5, 10, -2]
#for i in x
#    if i < 0
#        i = 0
#    end
#    puts i
#end

#11 Max, Min, and Average
#x = [1, 5, 10, -2]
#max = x.max
#min = x.min
#sum = 0
#x.each {|number| sum += number}
#avg = sum/x.length

#hash = {maximum: max, minimum: min, average: avg}
#puts hash

#12 Shifting the Values in the Array
#x = [1, 5, 10, 7, -2]
#x.each {|number| 
#    x.shift
#    print x 
#    x.insert(-1, number)
#    print x
#}
#print x
#x.shift
#x.insert(-1, 1)
#print x

#13 Number to String
#x = [-1, -3, 2]

#x.map! {|number|
#    if(number < 0)
#        "Dojo"
#    else
#        number
#    end
#}
#print x
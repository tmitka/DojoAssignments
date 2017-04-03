#find and replace
str = "It's thanksgiving day. It's my birthday, too"
print str.find("day")
str = str.replace("day", "month")
print str

#max and min
x = [2, 54, -2, 7, 12, 98]
print max(x)
print min(x)

#f and l
y = ["hello",2,54,-2,7,12,98,"world"]
print y[0], y[len(y) - 1]

#new sorted list cut in the middle
z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
print z
first_l = z[0:len(z)/2]
second_l = z[len(z)/2:len(z)]
print first_l
print second_l
second_l.insert(0,first_l)
print second_l

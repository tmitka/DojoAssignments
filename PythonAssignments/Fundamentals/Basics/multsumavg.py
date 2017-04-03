#print odd numbers
for count in range(1, 1000):
    if (count % 2 != 0):
        print count

#print multiples of 5
for fives in range(5, 1000001):
    if (fives % 5 == 0):
        print fives

#sum list
list = [1, 2, 5, 10, 255, 3]
sumlist = sum(list)
print sumlist

#avg list
avglist = sum(list) / len(list)
print avglist
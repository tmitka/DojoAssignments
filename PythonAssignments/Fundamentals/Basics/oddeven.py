#odd/even function
def oddeven(num1, num2):
    rangenums = range(num1, num2)
    for count in (rangenums):
        if num1 % 2 == 0:
            print "Number is",  num1, "This is an even number"
        if num1 % 2 != 0:
            print "Number is", num1, "This is an odd number"
        num1 += 1

#oddeven(1, 2001)

#multiply function
def multiply(list, value):
    multlist = []
    for number in list:
        multlist.append(number * value)
    return multlist

#multiply([2, 4, 10, 16], 5)

#hacker challenge

def layered_multiples(arr):
    ones_array = []
    for value in arr:
        i = 1
        while i <= value:
            ones_array.append(1)
            i += 1
    print ones_array
#layered_multiples(multiply([2,4,5],3))
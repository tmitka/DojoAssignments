i = 0
sum = 0
tlist = "haha   "
newl = []
l = ["magical unicorns", 19, "hello", 98.98, "world"]
while i < len(l):
    if type(l[i]) is str:
        newl.append(l[i])
    if type(l[i]) is int:
           sum = sum + (l[i])
    if type(l[i]) is float:
        sum = sum + (l[i])
    i = i + 1
#cant figure out the check type of the l
#if str and int in(l):
#    print "ok"
#if str in(l):
#    tlist = "The array is of string type"
#if int in(l):
#    tlist = "The array is of integer type"  
print tlist
print "String:", " ".join(newl)
print "Sum:", sum
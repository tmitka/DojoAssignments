i = 0
l = ['hello','world','my','name','is','Anna']
char = 'o'
n = []
while i < len(l):
    if char in l[i]:
        n.append(l[i])
    i = i + 1

print n
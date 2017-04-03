def findchars(arr, char):
    i = 0
    n = []
    while i < len(arr):
        if char in arr[i]:
            n.append(arr[i])
        i = i + 1
    print n

findchars(['hello','world','my','name','is','Anna'], "o")
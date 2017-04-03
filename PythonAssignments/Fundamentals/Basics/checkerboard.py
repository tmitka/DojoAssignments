evenlines = "* * * * "
oddlines = " * * * *"
i = 0

while i < 9:
    if (i % 2 == 0):
        print evenlines
    if (i % 2 != 0):
        print oddlines
    i = i + 1
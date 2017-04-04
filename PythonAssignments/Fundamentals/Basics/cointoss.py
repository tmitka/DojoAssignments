import random

def cointoss(number):
    headcount = 0
    tailcount = 0
    for num in range(1, number):
        toss = (random.randint(0, 1))

        if toss == 0:
            headcount = headcount + 1
            print "Attempt #", num, "Throwing a coin... It's a head! ... Got", headcount, "head(s) so far and", tailcount, "tail(s) so far"             
        else:
            tailcount = tailcount + 1
            print "Attempt #", num, "Throwing a coin... It's a head! ... Got", headcount, "head(s) so far and", tailcount, "tail(s) so far"
            
cointoss(5001)

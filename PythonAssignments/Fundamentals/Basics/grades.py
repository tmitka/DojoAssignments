import random
def grade(number):
    for num in range(number):
        grade = (random.randint(60, 100))
        if grade > 89:
            print "Score is", grade, "Your grade is A"
        elif grade > 79:
            print "Score is", grade, "Your grade is B"
        elif grade > 69:
            print "Score is", grade, "Your grade is C"
        else:
            print "Score is", grade, "Your grade is D"    
grade(10)
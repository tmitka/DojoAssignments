class MathDojo(object):
    def __init__(self):
        self.sum = 0

    def add(self, *addnumber):
        if type(addnumber) is tuple:
            numberlist = list(addnumber)
            for number in numberlist:
                sumlist = []
                sumlist.append(number)
                print sumlist
                #self.sum = self.sum + number
            return self
            #for number in addnumber:
            #    numberlist = []
            #    numberlist.append(number)  
            #    self.sum = self.sum + number
            #return self

        if type(addnumber) is int:
            for number in addnumber:
                numberlist = []
                numberlist.append(number)
                self.sum = self.sum + number
            return self

    def subtract(self, *subnumber):
        if type(subnumber) is int:
            for number in subnumber:
                numberlist = []
                numberlist.append(number)
                self.sum = self.sum - number
            return self

    def result(self):
        print self.sum

MathDojo().add([5, 2, 3])
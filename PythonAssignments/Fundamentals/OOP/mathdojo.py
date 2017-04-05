class MathDojo(object):
    def __init__(self):
        self.sum = 0

    def add(self, *addnumber):
            for number in addnumber:
                if type(number) is int:
                    self.sum = self.sum + number
                else: 
                    self.sum = self.sum + sum(number)
            return self

    def subtract(self, *subnumber):
            for number in subnumber:
                if type(number) is int:
                    self.sum = self.sum - number
                else:
                    self.sum = self.sum - sum(number)
            return self

    def result(self):
        print self.sum

MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result()
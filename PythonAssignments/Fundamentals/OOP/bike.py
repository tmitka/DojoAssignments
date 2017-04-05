class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def bikeinfo(self):
        print self.price
        print self.max_speed
        print self.miles
    
    def ride(self):
        self.miles += 10
        print "You have riden {} miles".format(self.miles)
    
    def reverse(self):
        if self.miles > 0:
            self.miles -= 5
            print "Reversing {}".format(self.miles)
        else:
            print "You can't reverse below 0 miles"

    
bike1 = Bike(200, 20)
print "This is the first bike"
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.bikeinfo()

bike2 = Bike(150, 15)
print "This is the second bike"
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.bikeinfo()

bike3 = Bike(300, 30)
print "This is the third bike"
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.bikeinfo()
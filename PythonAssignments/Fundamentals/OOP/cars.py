class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = .12
        if self.price > 10000:
            self.tax = .15
        


       

    def display_all(self):
        print "Price: {}".format(self.price)
        print "Speed: {}".format(self.speed)
        print "Fuel: {}".format(self.fuel)
        print "Mileage: {}".format(self.mileage)
        print "Tax: {}".format(self.tax)
        print ""

car1 = Car(2000, "35mpg", "Full", "15mpg")
print "Car1 info"
car1.display_all()

car2 = Car(2000, "5mph", "Not full", "105mpg")
print "Car2 info"
car2.display_all()

car3 = Car(2000, "15mph", "Kind of full", "95mpg")
print "Car3 info"
car3.display_all()

car4 = Car(2000, "25mph", "Full", "25mpg")
print "Car4 info"
car4.display_all()

car5 = Car(2000, "45mph", "Empty", "25mpg")
print "Car5 info"
car5.display_all()

car6 = Car(20000000, "5mph", "Empty", "15mpg")
print "Car6 info"
car6.display_all()
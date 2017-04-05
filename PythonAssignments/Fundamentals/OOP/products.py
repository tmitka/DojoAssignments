class Products(object):
    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax_percentage):
        self.price = self.price + self.price * tax_percentage

    def discount(self):
        self.price = self.price - self.price * .2

    def return_item(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
            return self
        elif reason == "used box":
            self.status = "used"
            self.discount()
            return self

        elif reason == "box_new":
            self.status = "for sale"
            return self
        else:
            print "Status change error please say 'defective', 'used box', or 'box_new'"

    def display_info(self):
        print self.price
        print self.item_name
        print self.weight
        print self.brand
        print self.status

product1 = Products(300, "Xbox One", "5 lbs", "Microsoft", 400)
product1.display_info()
product1.return_item("used box")

product1.display_info()
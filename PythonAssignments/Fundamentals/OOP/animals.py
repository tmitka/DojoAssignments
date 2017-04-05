class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = 100

    def walk(self):
        self.health = self.health - 1
        return self

    def run(self):
        self.health = self.health - 5
        return self
    
    def displayHealth(self):
        print "{} has {} health".format(self.name, self.health)

cat = Animal("cat", 50)
cat.walk()
cat.walk()
cat.walk()
cat.run()
cat.displayHealth()

class Dog(Animal):
    def __init__(self, name, health):
        self.name = name
        self.health = 150

    def pet(self):
        self.health += 5

dog = Dog("sam", 900)
dog.walk().walk()
dog.walk()
dog.walk()
dog.run()
dog.run()
dog.pet()
dog.displayHealth()

class Dragon(Animal):
    def __init__(self, name, health):
        self.name = name
        self.health = 170

    def fly(self):
        self.health -= 10

    def displayHealth(self):
        print "This is a dragon,", 
        super(Dragon, self).displayHealth()


dragon = Dragon("Smaug", 300)
dragon.walk()
dragon.walk()
dragon.run()
dragon.run()
dragon.fly()
dragon.fly()
dragon.displayHealth()
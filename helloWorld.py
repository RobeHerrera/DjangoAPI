print("Hello Robert")

class Sample():

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def __str__(self):
        return self.breed + " " + self.name

x = Sample(breed = "Lab", name = "Juanito")
print(x)


#inheritance

class Animal():

    def __init__(self):
        print("Animal created")

    def whoIam(self):
        print("aNIMAL")
    
    def eat(self):
        print("Eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def bark(self):
        print("Woof")

    def eat(self):
        print("dog eating")

print(15*"-")
mydog = Dog()
mydog.whoIam()
mydog.bark()
mydog.eat()

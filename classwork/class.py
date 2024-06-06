class Animal:
    def __init__(self, name, specie):
        self.name = name #attribute
        self.specie = specie #attribute
    def speak(self): #method
        pass

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog") #call the parent calss constructor
        self.breed = breed  #ad 1 attrbt for og class
    
    def speak(self): #polymorphism, method overriding
        return f"{self.name} says woof!"


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Dog") #call the parent calss constructor
        self.color = color  #ad 1 attrbt for cat class
    
    def speak(self): #polymorphism, method overriding
        return f"{self.name} says meow!"


# created the instances of Dog and Cat

dog = Dog("Bingo", "Local Dog")
cat = Cat("Musu", "Tabbycat")

print(dog.speak())
print(cat.speak())

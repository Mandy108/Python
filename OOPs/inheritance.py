class Animal:  # Parent class (superclass)
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Generic animal sound")

class Dog(Animal):  # Dog inherits from Animal (Dog is a subclass of Animal)
    def speak(self):  # We *override* the speak method (more on this later)
        print("Woof!")

class Cat(Animal):  # Cat also inherits from Animal
    def speak(self):
        print("Meow!")

# Create objects:
my_dog = Dog("Rover")
my_cat = Cat("Fluffy")

# They both have a 'name' attribute (inherited from Animal):
print(my_dog.name)  # Output: Rover
print(my_cat.name)  # Output: Fluffy

# They both have a 'speak' method, but it behaves differently:
my_dog.speak()  # Output: Woof!
my_cat.speak()  # Output: Meow!


# Calling Parent Constructor with super()
class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)  # Call Animal's __init__ to set the name
        self.wingspan = wingspan # Add a Bird-specific attribute

my_bird = Bird("Tweety", 10)
print(my_bird.name)      # Output: Tweety (set by Animal's constructor)
print(my_bird.wingspan)  # Output: 10   (set by Bird's constructor)
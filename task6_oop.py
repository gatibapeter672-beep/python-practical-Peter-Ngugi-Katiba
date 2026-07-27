"""
Task 6: Object-Oriented Python

This program demonstrates:
- Classes and objects
- Class variables
- Methods
- Inheritance
- Encapsulation
"""

# a. Define class Animal
class Animal:
    species = "General Animal"   # class variable
    counter = 0                 # class variable to count instances

    def __init__(self, name, sound, age):
        self.name = name
        self.sound = sound
        self.__age = age   # private attribute (encapsulation)

        Animal.counter += 1  # increment counter when object is created

    # b. Method speak()
    def speak(self):
        print(f"{self.name} says {self.sound}")

    # f. Getter method
    def get_age(self):
        return self.__age

    # f. Setter method
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")


# c. Create objects
animal1 = Animal("Dog", "Bark", 5)
animal2 = Animal("Cat", "Meow", 3)

animal1.speak()
animal2.speak()

# d. Display number of instances
print("\nTotal Animals Created:", Animal.counter)


# e. Inheritance
class Dog(Animal):
    def speak(self):
        print(f"{self.name} (Dog) barks loudly!")


# Create object of subclass
dog1 = Dog("Buddy", "Bark", 4)
dog1.speak()


# f. Encapsulation demonstration
print("\nDog Age (using getter):", dog1.get_age())

dog1.set_age(6)
print("Updated Dog Age:", dog1.get_age())
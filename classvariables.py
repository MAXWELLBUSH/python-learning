# class variables are shared by all objects of the class,the belong to the class itself not to one specific 
#defined outside of the constructor

class Dog:
    # 🟢 Class variable
    species = "Canine"

    def __init__(self, name, age):
        # 🔵 Instance variables
        self.name = name
        self.age = age

# Create two dogs
dog1 = Dog("Buddy", 3)
dog2 = Dog("Bella", 5)

# Access class variable
print(dog1.species)  # Output: Canine
print(dog2.species)  # Output: Canine

# Access instance variables
print(dog1.name)     # Output: Buddy
print(dog2.name)      # Output: Buddy 
print(dog2.age)     #output: 5
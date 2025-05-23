class Animal:
     def __init__(self,name):
          self.name = name
          self.is_alive = True

     def eat(self):
          print(f"{self.name} is eating")
          
     def sleep(self):
          print(f"{self.name} is sleeping")


class Dog(Animal):
  def speak(self): 
    print("!WOOf")
class Cat(Animal):
   pass    
class Mouse(Animal):
    pass  

dog = Dog("Bushbaby")
cat = Cat("mahez")
mouse = Mouse("maxwell")

print(dog.name)
print(dog.is_alive)
cat.eat()
mouse.sleep()
dog.speak()

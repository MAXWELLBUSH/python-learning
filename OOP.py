# the class car we can put it in a another python file called car then we import the file

from car import Car

car1 = Car("mustang",2024,"purple",False)
car2 = Car("Prado",2027,"pink",True)

"""
print(car2.model)
print(car2.year)
print(car2.for_sale)
print(car2.color)
"""
car2.drive()
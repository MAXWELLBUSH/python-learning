#List comprehension is a cleaner way to create a new listfrom an existing list


doubles = [x*2 for x in range(1,11)]
square = [x*x for x in range(1,11)]
#print(square)

#strings
fruits = ['apple','orange','banana','coconut',]
fruits =[ fruit.upper() for fruit in fruits]
fruit_chars = [ fruit[0] for fruit in fruits]
#print (fruit_chars)

"""
numbers = [1,-2,-3,-4,-5.-6, 8]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num <= 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]
print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)
"""

grades = [85,42,79,90,56,61,30]
passing_grades = [ grade for grade in grades if grade >= 60]
print(passing_grades)
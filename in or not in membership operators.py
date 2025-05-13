"""
#Sets
students = {
    "bush","patrick","sandy"
}
student = input(' Enter the name of a student')

if student in students:
    print(f"{student} is a student")
else:
     print(f"{student} is not a student")
"""

"""
#dictionaries
grades = {
    "Sandy" :"A",
    "Mahez" :"B",
    "Bush" :"C",
    "Maxwell" :"D",
}
student = input("Enter the name of a student")
if student in grades:
     print(f"{student}'s grade is {grades[student]}")
else:
     print(f"{student} was not found")
"""

email = "mahezmax@gmail.com"
if "@" in email and "." in email:
    print("valid email")
else:
    print("invalid email")
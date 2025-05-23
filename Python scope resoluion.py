x = 5
print(x)  # ✅ You can use x here


def say_hello():
    x = 10
    print(x)

say_hello()
print(x)  # ❌ This will cause an error!


#  Python's Rule for Finding Variables: LEGB
# Local - 	Inside the current function
# Enclosing-	Inside any outer (wrapping) function
# Global - At the top of the file (main code)
# Built-in - 	Python’s own keywords (like len)

x = "global"  # Global scope

def outer():
    x = "enclosing"  # Enclosing scope

    def inner():
        x = "local"  # Local scope
        print(x)     # Python will use the LOCAL one

    inner()

outer()

#It will print: local — because Python always looks from inside → out.

name = "Global Name"

def greet():
    name = "Local Name"
    print("Hello", name)

greet()
print("Outside function:", name)

#OUTPUT
#Hello Local Name
#Outside function: Global Name
#See? The same variable name name can exist in two places — inside the function and outside. They are not the same!

#Exception handling lets you handle errors in your code without crashing the program
# When something goes wrong (like dividing by zero or opening a missing file), Python raises an exception. You can catch and handle it using try...except.
# types of errors (ZeroDivisionError,TypeError,ValueError)
#A TypeError happens when you try to do something with the wrong type of value, such as adding a number and a string, or calling something that isn’t callable.
try:
 number = int(input("enter a number"))
 print(1/number)
except ZeroDivisionError:
  print("you cant divide by zero")
except ValueError:
  print("enter only numbers dumb ass")
except Exception:
  print("something went wrong")
finally:
  print("Do so cleanup")


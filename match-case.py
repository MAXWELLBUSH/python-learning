# An alternative of using many elif statements,execute some code if a value matches a 'case 

def day_of_week(day):
    match day:
        case 1:
            return "its a Sunday"
        case 2:
            return "its a Monday"
        case 3:
            return "its a Wednesday"
        case 4:
            return "its a Thursday"
        case 5:
            return "its a Friday"
        case 6:
            return "its a saturday"
        case 4:
            return "its a sunday"
        case _:
             return "Not a valid day"
#print(day_of_week(17))

def is_weekend(day):
    match day:
        case "Sunday":
            return True
        case "Monday":
            return False
        case "Tuesday":
            return False
        case "Wednesday":
            return False
        case "Thursday":
            return False
        case "Friday":
            return False
        case "Saturday":
            return True
        case _:
             return "Not a valid day"
#print(is_weekend("Monday"))

def is_weekend(day):
    match day:
        case "Sunday" | "Saturday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
       
        case _:
             return "Not a valid day"
print(is_weekend("Monday"))
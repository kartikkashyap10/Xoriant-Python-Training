def validate(func):
    def validator(*args, **kwargs):
        if len(args) >= 1:
            if args[1] == 0:
                print("Invalid Input!")
                return None
            else:
                power = func(args[0], args[1])
                return power
        else:
            print("Invalid arguments!")
    return validator

# Decorator
import math
@validate
def mypower(x, y):
    return math.pow(x, y)

mypower(10, 2)
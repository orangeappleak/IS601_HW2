def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a, b):
    if b == 0:
        #This raises a division by zero error if the denominator i.e. b is passed as 0.
        raise ZeroDivisionError("Division by zero is not possible")
    return a / b
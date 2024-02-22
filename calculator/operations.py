'''All the operations listed here'''

def add(arg_a,arg_b):
    '''Returns the addition result'''
    return arg_a + arg_b

def subtract(arg_a,arg_b):
    '''returns the subtraction result'''
    return arg_a - arg_b

def multiply(arg_a,arg_b):
    '''returns the multiplication result'''
    return arg_a * arg_b

def divide(arg_a,arg_b):
    '''return the division result with zero division error'''
    if arg_b == 0:
        #This raises a division by zero error if the denominator i.e. b is passed as 0.
        raise ValueError("Division by zero is not possible")
    return arg_a / arg_b

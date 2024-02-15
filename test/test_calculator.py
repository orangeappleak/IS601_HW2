'''My Calculator Test'''
import pytest
from calculator import Calculator

def test_addition():
    '''Test that addition function works '''    
    assert Calculator.add(2,2) == 4

def test_subtraction():
    '''Test that addition function works '''    
    assert Calculator.subtract(2,2) == 0

def test_multiply():
    '''Test that addition function works '''    
    assert Calculator.multiply(2,2) == 4

def test_divide():
    '''Test that addition function works '''    
    assert Calculator.divide(2,2) == 1

def test_zero_divide():
    '''Test that divide by zero throws a ZeroDivisionError'''
    with pytest.raises(ZeroDivisionError):  # Import pytest and use context manager
        Calculator.divide(2, 0)
        
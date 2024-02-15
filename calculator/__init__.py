from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def add(a,b):
        return Calculation.create(a,b,add).get_result()
    @staticmethod
    def subtract(a,b):
        return Calculation.create(a,b,subtract).get_result()
    @staticmethod
    def multiply (a,b):
        return Calculation.create(a,b,multiply).get_result()
    @staticmethod
    def divide(a,b):
       return Calculation.create(a,b,divide).get_result()
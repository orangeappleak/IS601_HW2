'''Calculator Class'''

from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide


class Calculator:
    '''Calculator Class with static methods'''
    @staticmethod
    def add(arg_a, arg_b):
        '''adds the given arguments'''
        return Calculation.create(arg_a, arg_b, add).get_result()

    @staticmethod
    def subtract(arg_a, arg_b):
        '''subtracts the given arguments'''
        return Calculation.create(arg_a, arg_b, subtract).get_result()

    @staticmethod
    def multiply(arg_a, arg_b):
        '''multiplies the given arguments'''
        return Calculation.create(arg_a, arg_b, multiply).get_result()

    @staticmethod
    def divide(arg_a, arg_b):
        '''divides the given arguments'''
        return Calculation.create(arg_a, arg_b, divide).get_result()

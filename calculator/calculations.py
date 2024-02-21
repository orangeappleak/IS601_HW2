'''Calculations class'''

from typing import List

from calculator.calculation import Calculation

class Calculations:

    '''History functions for the calculator'''

    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """adds whatever calcualtion has been made to history"""
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """lists all the calculations from history"""
        return cls.history
    @classmethod
    def clear_history(cls):
        """Clear the history of calculations."""
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        """Get the latest calculation. Returns None if there's no history."""
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        """Find and return a list of calculations by operation name."""
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]

'''Calculation Class'''


class Calculation:
    '''calculation class with the class method'''

    def __init__(self, arg_a, arg_b):
        self.arg_a = arg_a
        self.arg_b = arg_b
        self.operation = None  # Initialize operation attribute

    @classmethod
    def create(cls, arg_a, arg_b, operation):
        """
        Creates a Calculation instance with the specified operation.
        """
        instance = cls(arg_a, arg_b)
        instance.operation = operation
        return instance
    def perform(self):
        """Perform the stored calculation and return the result."""
        return self.operation(self.arg_a, self.arg_b)

    def get_result(self):
        """
        Calculates the result using the stored operation function.
        """
        if self.operation is None:
            raise ValueError("Operation is not defined")
        return self.operation(self.arg_a, self.arg_b)

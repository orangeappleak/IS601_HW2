class Calculation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @classmethod
    def create(cls, a, b, operation):
        """
        Creates a Calculation instance with the specified operation.
        """
        instance = cls(a, b)
        instance.operation = operation
        return instance

    def get_result(self):
        """
        Calculates the result using the stored operation function.
        """
        return self.operation(self.a, self.b)

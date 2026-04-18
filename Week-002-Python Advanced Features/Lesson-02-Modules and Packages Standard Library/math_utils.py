class TaylorCalculationError(Exception):
    def __init__(self, value, reason):
        self.value = value
        self.reason = reason
        message = f"Calculation Error for value [{value}]: {reason}"
        super().__init__(message)

def calculate_taylor_step(x, n):
    if n == 0:
        raise ZeroDivisionError
    
    if x <= -1 or x >= 1:
        raise TaylorCalculationError(x, "Value is outside the convergence interval (-1, 1)")
    
    return (x**n) / n

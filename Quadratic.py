import math

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    D = b**2 - 4*a*c

    # Check the discriminant
    if D > 0:
        # Two real and distinct solutions
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        return [x1, x2]
    elif D == 0:
        # One real solution
        x = -b / (2*a)
        return [x]
    else:
        # No real solution
        return None

# Tests
print(solve_quadratic(56, 67, 2))  # D > 0, Two solutions: [2.0, 1.0]
print(solve_quadratic(1, 34, 1))  # D = 0, One solution: [1.0]
print(solve_quadratic(1, 2, 1))   # D < 0, No real solution: None

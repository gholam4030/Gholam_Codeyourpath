from math import sqrt

def solve_quadratic(a: float, b: float, c: float):

    #این ها فقط تشریحات است برای کسی که کود شما را میخوانند
    """
    Calculate the roots of a quadratic equation.

    Parameters:
    - a (float): Coefficient of x^2.
    - b (float): Coefficient of x.
    - c (float): Constant term.

    Returns:
    List: A list containing the roots or None if D < 0.
    """
    # اخر تشریحات
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check the discriminant and calculate solutions accordingly
    if discriminant > 0:
        # Two real roots
        root1 = (-b + sqrt(discriminant)) / (2*a)
        root2 = (-b - sqrt(discriminant)) / (2*a)
        return [root1, root2]
    elif discriminant == 0:
        # One real root
        root = -b / (2*a)
        return [root]
    else:
        # No real roots
        return None



# Test cases
test_cases = [
    # Two real roots
    ((1, -3, 2), [2.0, 1.0]),

    # One real root
    ((1, -2, 1), [1.0]),

    # No real roots (discriminant < 0)
    ((1, 2, 5), None),
]

# Validate the results for each test case
for i, (coefficients, expected_result) in enumerate(test_cases, start=1):
    result = solve_quadratic(*coefficients)

    print(f"\nTest Case {i}:")
    print(f"Coefficients: {coefficients}")
    print("Expected Result:", expected_result)
    print("Actual Result:", result)

    assert result == expected_result

# If all assertions pass, print success message
print("\nAll test cases passed successfully!")

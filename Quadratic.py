from math import sqrt


def solve_quadratic(a, b, c):
    """
    Calculates x values for specified quadratic equation coefficients
    :param a: first coefficient of quadratic equation
    :type a: float
    :param b: second coefficient of quadratic equation
    :type b: float
    :param c: third coefficient of quadratic equation
    :type c: float
    :return: Calculated x values as list or None if there are no solutions
    :rtype: list or None
    """
    # Calculate the discriminant
    discriminant = b**2 - 4 * a * c

    # Check the discriminant
    if discriminant > 0:
        # Two real and distinct solutions
        x1 = (-b + sqrt(discriminant)) / (2 * a)
        x2 = (-b - sqrt(discriminant)) / (2 * a)
        return [x1, x2]
    elif discriminant == 0:
        # One real solution
        x = -b / (2 * a)
        return [x]
    else:
        # No real roots
        return None


# Tests
assert solve_quadratic(56, 67, 2) == [2.0, 1.0]  # D > 0, Two solutions: [2.0, 1.0]
assert solve_quadratic(1, 34, 1) == [1.0]  # D = 0, One solution: [1.0]
assert solve_quadratic(1, 2, 1) is None  # D < 0, No real solution: None


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

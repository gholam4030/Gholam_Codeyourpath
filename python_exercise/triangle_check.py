def classify_triangle(x: int, y: int, z: int) -> str:
    # If input is valid, then the code goes further to check other conditions
    if not is_input_valid(x, y, z):  # if NOT valid, return string
        return "Invalid input"  # When return no other code is executed, exit function
    if x == y == z:
        return "This is an equilateral triangle"  # When return no other code is executed, exit function
    if x == y or x == z or y == z:
        return "This is an isosceles triangle"  # When return no other code is executed, exit function
    return "This is a scalene triangle"  # Equivalent to else as there are no other options left


def is_input_valid(x: int, y: int, z: int) -> bool:
    if x <= 0 or y <= 0 or z <= 0:
        return False
    # Check the Triangle Inequality Theorem, returns bool (True or False)
    return x + y > z and x + z > y and y + z > x  # This will be True or False


if __name__ == "__main__":
    a = int(input("Type first edge: "))
    b = int(input("Type second edge: "))
    c = int(input("Type third edge: "))
    return_string = classify_triangle(a, b, c)
    print(return_string)

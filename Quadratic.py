from math import sqrt
import click


@click.command()
@click.option(
    "--a",
    type=float,
    required=True,
    show_default=True,
    help="The first coefficient in quadratic eq",
)
@click.option(
    "--b",
    type=float,
    required=True,
    show_default=True,
    help="The second coefficient in quadratic eq",
)
@click.option(
    "--c",
    type=float,
    required=True,
    show_default=True,
    help="The third coefficient in quadratic eq",
)
def main(a, b, c):
    print("Start of the script quadratic")
    print(f"a={a}, b={b}, c={c}")
    print(f"Result = {solve_quadratic(a, b, c)}")
    print("End of the script quadratic")


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
        # No real solution
        return None


if __name__ == "__main__":
    main()

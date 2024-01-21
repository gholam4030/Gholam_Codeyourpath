import click


def calculate_interest(principal, rate, time):
    """
    Calculate compound interest.

    Args:
        principal (float): Initial amount of money.
        rate (float): Annual interest rate (in %).
        time (float): Amount of years.

    Returns:
        tuple: A tuple containing the interest earned and the total amount after interest.
    """
    if any(var <= 0 for var in (principal, rate, time)):
        raise ValueError("Every variable should be a positive number")
    # Formula for compound interest
    amount = principal * (1 + rate / 100) ** time
    interest = amount - principal
    return interest, amount


@click.command()
@click.option("-p", "--principal", type=float, help="Initial amount of money")
@click.option("-r", "--rate", type=float, help="Annual interest rate (in %)")
@click.option("-t", "--time", type=float, help="Amount of years")
def main(principal, rate, time):
    """
    Calculate compound interest.

    This script takes command line arguments for principal, rate, and time
    and calculates compound interest.
    """
    if not all([principal, rate, time]):
        click.echo("Please provide values for principal, rate, and time.")
        return

    try:
        interest, amount = calculate_interest(principal, rate, time)
        click.echo(f"Principal: ${principal}")
        click.echo(f"Annual Interest Rate: {rate}%")
        click.echo(f"Time (years): {time}")
        click.echo(f"Interest Earned: ${interest:.2f}")
        click.echo(f"Total Amount: ${amount:.2f}")
    except ValueError as e:
        click.echo(str(e))  # Display the specific error message raised in calculate_interest


if __name__ == "__main__":
    main()

import argparse

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
    # Formula for compound interest
    amount = principal * (1 + rate / 100) ** time
    interest = amount - principal
    return interest, amount

def main():
    """
    Main function to handle command line arguments and display results.
    """
    parser = argparse.ArgumentParser(description='Calculate compound interest.')
    parser.add_argument('--principal', type=float, help='Initial amount of money')
    parser.add_argument('--rate', type=float, help='Annual interest rate (in %)')
    parser.add_argument('--time', type=float, help='Amount of years')

    args = parser.parse_args()

    if not all([args.principal, args.rate, args.time]):
        parser.error("Please provide values for principal, rate, and time.")

    interest, amount = calculate_interest(args.principal, args.rate, args.time)

    print(f"Principal: ${args.principal}")
    print(f"Annual Interest Rate: {args.rate}%")
    print(f"Time (years): {args.time}")
    print(f"Interest Earned: ${interest:.2f}")
    print(f"Total Amount: ${amount:.2f}")

if __name__ == "__main__":
    main()

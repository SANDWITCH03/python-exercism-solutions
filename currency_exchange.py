# -------------------- Currency Exchange Program --------------------


def exchange_money(budget: float, exchange_rate: float) -> float:
    """
    Calculate estimated value after exchange.
    """

    return budget / exchange_rate


def get_change(budget: float, exchanging_value: float) -> float:
    """
    Calculate remaining money after exchange.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination: float, number_of_bills: int) -> float:
    """
    Calculate total value of bills.
    """

    return denomination * number_of_bills


def get_number_of_bills(amount: float, denomination: float) -> int:
    """
    Calculate number of bills possible.
    """

    return int(amount // denomination)


def get_leftover_of_bills(amount: float, denomination: float) -> float:
    """
    Calculate leftover amount after exchanging into bills.
    """

    return amount % denomination


def exchangeable_value(
    budget: float,
    exchange_rate: float,
    spread: float,
    denomination: float
) -> int:
    """
    Calculate maximum exchangeable currency value.
    """

    # Convert spread percentage into decimal
    spread_decimal = spread / 100

    # Calculate actual exchange rate including spread
    actual_exchange_rate = (
        exchange_rate +
        (exchange_rate * spread_decimal)
    )

    # Calculate exchanged money
    exchanged_money = budget / actual_exchange_rate

    # Calculate number of bills possible
    number_of_bills = exchanged_money // denomination

    # Return maximum exchangeable value
    return int(number_of_bills * denomination)


# -------------------- User Input Section --------------------


# Ask user for total budget
budget = float(input("Enter your total budget: "))

# Ask user for exchange rate
exchange_rate = float(input("Enter the current exchange rate: "))

# Calculate exchanged money
exchanged_money = exchange_money(
    budget,
    exchange_rate
)

# Display exchanged money
print(f"\nExchanged money = {exchanged_money:.2f}")


# Ask user how much money they exchanged
exchanging_value = float(input("\nEnter the amount exchanged: "))

# Calculate remaining balance
remaining_money = get_change(
    budget,
    exchanging_value
)

# Display remaining balance
print(f"Amount left = {remaining_money:.2f}")


# Ask user for denomination value
denomination = float(input("\nEnter the value of one bill: "))

# Ask user for number of bills
number_of_bills = int(input("Enter the number of bills: "))

# Calculate total bill value
total_bill_value = get_value_of_bills(
    denomination,
    number_of_bills
)

# Display total bill value
print(f"Total value of bills = {total_bill_value:.2f}")


# Reuse budget as amount
amount = budget

# Calculate total bills possible
total_bills = get_number_of_bills(
    amount,
    denomination
)

# Display total bills
print(f"Number of bills possible = {total_bills}")


# Calculate leftover amount
leftover_amount = get_leftover_of_bills(
    amount,
    denomination
)

# Display leftover amount
print(f"Leftover amount = {leftover_amount:.2f}")


# Ask user for spread percentage
spread = float(input("\nEnter the exchange spread percentage: "))

# Calculate exchangeable value
maximum_exchange_value = exchangeable_value(
    budget,
    exchange_rate,
    spread,
    denomination
)

# Display maximum exchangeable value
print(
    f"Maximum exchangeable value = "
    f"{maximum_exchange_value}"
)
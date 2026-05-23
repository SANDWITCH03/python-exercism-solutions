"""
Check whether a number is an Armstrong number.

An Armstrong number is a number that is equal to
the sum of its digits each raised to the power
of the total number of digits.
"""

def is_armstrong_number(number):
    """
    Store the original number in a temporary variable.
    Count the total number of digits in the number.
    Extract each digit using modulus (%) and raise it
    to the power of the digit count.
    Add all powered digits together and compare the
    result with the original number to determine
    whether it is an Armstrong number.
    """

    temp = number
    order = len(str(number))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** order
        temp = temp // 10

    return total == number


# User input
try:
    user_number = int(input("Enter a number: "))

    if is_armstrong_number(user_number):
        print(f"{user_number} is an Armstrong number.")
    else:
        print(f"{user_number} is not an Armstrong number.")

except ValueError:
    print("Error: Please enter a valid integer.")
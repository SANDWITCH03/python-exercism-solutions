def collatz_process(number):
    """Prints the Collatz sequence and returns number of steps."""

    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    count = 0

    print("Collatz sequence:")

    while number != 1:
        print(number, end=" → ")

        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1

        count += 1

    print(1)  # final value
    return count


# user input
try:
    user_number = int(input("Enter a positive integer: "))
    steps = collatz_process(user_number)
    print("Total steps:", steps)

except ValueError as e:
    print("Error:", e)
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
#user input 
try:
    user_year = int(input("Enter a year: "))
    if leap_year(user_year):
        print(f"{user_year} is a leap year.")
    else:
        print(f"{user_year} is not a leap year.")
except ValueError:
    print("Error: Please enter a valid integer for the year.")

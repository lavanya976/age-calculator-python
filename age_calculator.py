from datetime import date

# Take input from user
day = int(input("Enter birth day: "))
month = int(input("Enter birth month: "))
year = int(input("Enter birth year: "))

# Get today's date
today = date.today()

# Create birth date object
birth_date = date(year, month, day)

# Calculate age
age = today.year - birth_date.year

# Adjust age if birthday hasn't occurred this year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

print("Your age is:", age)

from dictionary import month_value, day_value, days_in_line, days_in_months

# This code prompts the user to input a month and year
month = input("Month: ")
year = int(input("Year: "))
month_int = month_value[month]

# These lines calculate the number of spaces needed to center the month and year in the calendar
blank_month = int((20 - len(month)) / 2)
blank_year = int((20 - len(str(year))) / 2)

# If the month is January or February, we need to subtract 1 from the year because the calendar starts in March
if month == "January" or month == "February":
    year = year - 1

# These lines calculate the year within the current century and the zero-based century
year_of_century = year % 100
zero_based_century = int(year / 100)

# This formula calculates the day of the week for the first day of the month
formula = (1 + int(13 * (month_int + 1) / 5) + year_of_century + int(year_of_century / 4) + int(
    zero_based_century / 4) - 2 * zero_based_century) % 7

# If the result of the formula is 0, we need to set it to 7 because 0 is not a valid day of the week
if formula == 0: formula = 7

# This line calculates the number of days in the month, including the first day
number_of_days = days_in_months[month] + 1

# If the month is January or February, we need to add 1 to the year because the calendar starts in March
if month == "January" or month == "February":
    year = year + 1

# These lines handle leap years for February
if year % 4 == 0 and year % 100 != 0 and month == "February":
    number_of_days += 1

if year % 100 == 0 and year % 400 == 0 and month == "February":
    number_of_days += 1

# These lines print the calendar
print(" " * blank_year + f"{year}")
print(" " * blank_month + f"{month}")
print("Mo Tu We Th Fr Sa Su")

# This line calculates the day of the week for the first day of the month
day_of_week = -1 + days_in_line[day_value[formula]]

# This loop prints the appropriate number of blank spaces before the first day of the month
for i in range(day_of_week):
    print("   ", end="")

# This loop prints the days of the month
for i in range(1, number_of_days):
    print("%2d " % i, end="")
    day_of_week = (day_of_week + 1) % 7
    if day_of_week == 0:
        print()
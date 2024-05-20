#Activity 4 
#Magic date checker
#user input day month and last two digit of the year
day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year_last_two_digits = int(input("Enter the last two digits of the year: "))

# determine if its magic date or not
if day * month == year_last_two_digits:
    print(f'provided date {day}-{month}-{year_last_two_digits} is a magic date!')
else:
    print(f'provided date {day}-{month}-{year_last_two_digits} is not a magic date!')

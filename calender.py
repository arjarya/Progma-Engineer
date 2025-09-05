import os
os.system("cls")
import calendar
year = 2025
while True:
 year = int(input("Enter year: "))
 month = int(input("Enter month[1-12]: "))
 if 1<= month <=12:
    print(calendar.month(year, month))
    break
 else:
    print("Invalid month")
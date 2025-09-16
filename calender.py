import os
os.system("cls")
import calendar
year = int(input("Enter year(e.g, 2025): "))

while True:
   month = int(input("Enter month[1-12]: "))
   if 1<= month <=12:
     print(calendar.month(year, month))
   else:
     print("Invalid month")
     continue # only skip back if month is invalid
   choice = input("Do you want see another month: (y/n)").lower().strip()
   if choice != "y":
      print("goodbye")
      break
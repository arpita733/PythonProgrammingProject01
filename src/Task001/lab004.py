year = input("Enter the year\n")
if year%4==0:
    print("The year is a leap year")
elif year%100==0:
    print("The year is a leap year")
elif year%400==0:
    print("The year is a leap year")
else:
    print("The year is not a leap year")
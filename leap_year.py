year=int(input("Enter the year\t"))
if year>0:
    if year%4==0:
        print(year,"is a leap year")
    else:
        print(year,"is not a leap year")
else:
    print("Not a valid year")
#Write a program that uses nested if statements to determine if a year is a leap year.

year= int(input("enter year for cheaking its leap year or not "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year}is not leap year")
    else:
        print(f"{year}is  leap year")
else:
    print(f"{year}is not leap year")
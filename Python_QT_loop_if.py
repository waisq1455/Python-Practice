#Question: Write a program that uses nested if statements to determine if a person can drive based on age and whether they have a license

name = input("what is  your name ?")
age= int(input("Enter your age "))

if age >=18:
    print("you are authorized for driving")

else:
    print("you are not authorized for driving ")


#Question: Write a program that uses nested if statements to determine the price of a ticket based on age and membership status.

age = int(input("enter age"))
status= input("menber/not-member")
if age>=18:
    if status == "member":
        print("your ticket price is 500")
    
    else:
        print("your ticket price is 700")
else:
     print("wrong entry")
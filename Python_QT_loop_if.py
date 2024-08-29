#Question: Write a program that uses nested if statements to determine if a person is eligible to apply for a job based on age and work experince

age = int(input("enter age "))
work_experince= int(input("enter experince "))

if age>=18:
    if work_experince >=2:
        print("you are eligible for this job")

    else:
        print("this job requird min 2 years of experince")

else:
    print("you under 18")
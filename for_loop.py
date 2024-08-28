#Question: Write a for loop to print all numbers from 1 to 10.

for i in range(1,11):
    print(i)


#Question: Write a for loop to calculate the sum of numbers from 1 to 5.'''
total=0
for x in range(1,6):
    total=total+x
print(total) 


#Question: Write a for loop to print each element of the following list: [10, 20, 30, 40,50].
l=[10,20,30,40,50]

for x in l:
    print(x)

#Question: Write a for loop to print the square of each number from 1 to 5

for x in range(1,6):
    i=x*x
    print(i)


#Question: Write a for loop to create a list of even numbers between 1 and 10

for x in range(1,11):
    if (x % 2) == 1:
        print(x)


#Question: Write a for loop to count down from 10 to 1 and print each number.

for x in reversed(range(1,11)):
    print(x)


#Question: Write a for loop to print all multiples of 3 between 1 and 15.

for x in range(1,16):
    if (x % 3)==0:
        print(x)


Question: Write a for loop to print the following pattern:
*
**
***
****
*****

for x in range(6):
    print("*"*x)



#Question: Write a for loop to print each character of the string "hello".

string= "Hello"

for x in string:
    print(x)


#Question: Write a for loop to calculate the factorial of the number 8
    
fac=1
num=8

while num>0:
    fac=fac*num
    num=num-1

print(fac)


#Question: Write a for loop to print the multiplication table for the number 7, from 1 to 10

num=7

for i in range(1,11):
    print(f"{num}*{i} = {num*i}")
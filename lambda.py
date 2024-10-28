#Question: Count the odd numbe rgiven list using lambda expression
list1 = [10, 21, 4, 45, 66, 93, 11]
odd_number = list(filter(lambda x: x%2==0,list1))
print(odd_number)


#Question: Python program to print odd Numbers in a List using Using List Comprehension
list1 = [10, 21, 4, 45, 66, 93, 11]

odd_number=list(filter(lambda x : x%2==0,list1))
print(odd_number)


#Question: string1 = "Hello World" split this string1 using lambda function
string1 = "Hello World"
s=(lambda x:x.split())(string1)
print(s)

#Question: Calculate the total multiplication of all elements in a list use lambda function
from functools import reduce
my_list = [1, 2, 3, 4, 5]
multiple= reduce(lambda x,y:x*y,my_list)
print(multiple)


#Question: Calculate the total addition of all elements in a list use lambda function
from functools import reduce
my_list = [1, 2, 3, 4, 5]
additons=reduce(lambda x,y:x+y,my_list)
print(additons)


#Question: my_string = "Hello World" remove space inside a string using a lambda function

my_string = "Hello World"
space_remove= lambda x:x.replace(" ", "")
result=space_remove(my_string)
print(result)


#Question: Write a lambda function that takes a number and returns its square.
a=int(input("enter a number"))
square= lambda x:x**2
result=square(a)
print(result)



#Question: Use filter with a lambda function to get all even numbers from a list.

list1=[1,2,3,4,5,6,7,8,9]

even= list(filter(lambda x:x%2==0,(list1)))
print(even)


#Question: Use a lambda function inside a list comprehension to square each number in a list.
list1=[1,2,3,4,5,6,7,8,9]
square=[(lambda x:x**2)(x) for x in list1]
print(square)




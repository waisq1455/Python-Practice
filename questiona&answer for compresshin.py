#Qt 1] How can you find all the even numbers in a given list of integers using Python?
a=[1,2,3,4,5,6,7,8,9,10]
a=[i for i in a if i%2!=0]
print(a)


#Qt 2] How can you find all the odd numbers in a given list of integers using Python?
#compression
z=[x for x in range(1,20) if x%2!=0]
print(z)


#Qt 4] How can you output a string in Python with the first letter capitalized?
a="wasiq"
print(a.capitalize())

#Qt 5] How can you create a list using list comprehension with a nested for loop in Python?
a=[(i,j) for i in range(3) for j in range(2)]
print(a)
    
    

#Qt 7] list1 = [1, -12, 34, -4, 25, -16, 19], write a Python program to create a new list list2 that contains the string " +ve " for each positive number and " -ve " for each negative number using list comprehension with if-else conditionals. Print the resulting list2.

list1 = [1, -12, 34, -4, 25, -16, 19]
list2=[i for i in list1 if i<0]
list3=[i for i in list1 if i>0]
print(list2)
print(list3)




#Qt 8] string = 'AbcDeFG', write a Python program to create a new list list1 that contains each character of the string converted to uppercase using list comprehension. Print the resulting list1.

string = 'AbcDeFG'
list1=[i.upper() for i in string ]
print(list1)




#QT 9] Create a dictionary using dictionary comprehension Convert the numbers squares to cubes by using dict comprehension
cube={num: num**3 for num in range(1,5)}
print(cube)


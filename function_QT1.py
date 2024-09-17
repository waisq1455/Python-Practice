#Question 1: Write a function that takes a list of numbers and returns a new list with each number squared.

def square():
    l=[2,3,4,5,6,7]
    m=[]
    for i in l:
        m.append(i**2)
    print(m)
square()

#Question 2: Write a function that takes a string and splits it into a list of words. Assume words are separated by spaces.

def f1():
    a="Hello this is Python class"
    print(a.split(" "))
f1()

#Question 3: Write a function that takes a list of numbers and returns a new list where each number is multiplied by 5.

def f2():
    a=[1,2,3,4,5,6,7]
    b=[]
    for i in a:
        b.append(i*5)
    print(b)
f2()

#Question 4: Write a function that takes a string and returns the count of each vowel (a, e, i, o, u) in the string.

def vowel():
    a="Hello this is python class"
   

#Question 5: Write a function that takes a string and returns the string reversed.

def string():
    a="Hello this is Python class"
    print(a[::-1])
string()

#Question 6: Write a function that takes a list of numbers and returns a new list with only the even numbers.
def even():
    a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    for i in a:
     if i%2==0:
        print(i)
even()
#Question 8: Write a function that checks if a given string is a palindrome

def ispalindrome(s):
    return s==s[::-1]
s="malayalam"
ans=ispalindrome(s)
if ans:
    print("yes")
else:
    print("No")
ispalindrome(s)

##Question 1: Write a function that takes a list of numbers and returns a new list with each number squared.

def square():
    l=[2,3,4,5,6,7]
    m=[]
    for i in l:
        m.append(i**2)
    print(m)
square()

#Question 2: Write a function that takes a string and splits it into a list of words. Assume words are separated by spaces.

def f1():
    a="Hello this is Python class"
    print(a.split(" "))
f1()

#Question 3: Write a function that takes a list of numbers and returns a new list where each number is multiplied by 5.

def f2():
    a=[1,2,3,4,5,6,7]
    b=[]
    for i in a:
        b.append(i*5)
    print(b)
f2()

#Question 4: Write a function that takes a string and returns the count of each vowel (a, e, i, o, u) in the string.

def vowel():
    a="Hello this is python class"
   

#Question 5: Write a function that takes a string and returns the string reversed.

def string():
    a="Hello this is Python class"
    print(a[::-1])
string()

#Question 6: Write a function that takes a list of numbers and returns a new list with only the even numbers.
def even():
    a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    for i in a:
     if i%2==0:
        print(i)
even()
#Question 8: Write a function that checks if a given string is a palindrome

def ispalindrome(s):
    return s==s[::-1]
s="malayalam"
ans=ispalindrome(s)
if ans:
    print("yes")
else:
    print("No")
ispalindrome(s)

#Question 9: Write a function that calculates the sum of all elements in a list.

def sum():
    a=[2,3,4,5,6,7,8,9]
    total=0
    for x in a:
        total=total+x
    print(total)
sum()



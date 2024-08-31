#How do you append an element to a list in Python?
l=[1,2,3,4,]

l.append(5)
print(l)


#Write a Python program to find the sum of all elements in a list.
total=0
list=[1,2,3,4,5]
for x in list:
    total=total+x
print(total)



#How do you remove duplicates from a list in Python?
a=[1,2,3,4,5,3,4,5,1]
unique=list(set(a))
print(unique)


#Write a Python program to find the largest number in a list.
list=[25,10,40,60]
larget_number= max(list)
print(larget_number)

#How do you sort a list in Python?
a=[1,2,3,4,5,3,4,5,1]
sorted_number= sorted(a)
print(sorted_number)


#Write a Python program to find the index of an element in a list.
a=[1,2,3,4,5,6,7,8,9]
print(a[5])


#How do you insert an element at a specific position in a list in Python?
a=["wasiq","quazi","rizwan","sajid"]

print(a.insert(2,"feroz"))
print(a)


#Write a Python program to reverse a list.
a=[1,2,3,4,5,6,7,8]
print(a.reverse())
print(a)

#How do you concatenate two lists in Python?
a=[1,2,3,4]
b=[5,6,7,8,9]
concatenate=a+b
print(concatenate)


#How do you merge two dictionaries in Python?
a={"a":10,"b":20}
b={"c":30,"d":40}

c=b.update(a)
print(c)

c=a | b
print(c)


#Write a Python program to find the maximum value in a dictionary.
dic1={"wasiq":10,"sajid":20,"rizwan":30,"feroz":40}
max_vlaue=max(dic1.values())
print(max_vlaue)


#5. How do you use the get() method to access a dictionary value?

dic1={"wasiq":10,"sajid":20,"rizwan":30,"feroz":40}

print(dic1.get("sajid"))
print(dic1.get("rizwan"))


#How do you create a named tuple in Python?

name =()
print(type(name))


#Write a Python program to find the index of an element in a tuple.
name=(1,2,3,4,5,6,7)
print(name[6])


#How do you use tuple unpacking to assign values to variables?

tuple1=(22,10,3,7)
print(tuple1)
print(type(tuple1))



#Write a Python program to create a tuple from a list.

a=[1,2,3,4,5,6,7,8,9]
b=tuple(a)
print(b)
print(type(b))



#5. How do you compare two tuples in Python?
a=(1,2,3,4)
b=(1,2,3,4)
if a==b:
    print("tuple equal")
else:
    print("tuple not equal")


#Write a Python expression to check if a number is even.
number=int(input("enter value"))

if number % 2 == 0:
    print("its is odd number")

else:
    print("even number")



#Use the in operator to check if a string contains a specific substring.
a="hello world my name is wasiq"

if "my name" in a:
    print("string value available")

else:
    print("string value not available")







#Question: Count the odd numbe rgiven list using lambda expression
list1 = [10, 21, 4, 45, 66, 93, 11]
odd_number= list(filter(lambda x:x%2==0,list1))
print(odd_number)


#Question: Python program to print odd Numbers in a List using Using List Comprehension
list1 = [10, 21, 4, 45, 66, 93, 11]
odd_number_using_Comprehension= [list(filter(lambda x:x%2==0,list1))]
print(odd_number_using_Comprehension)



#Question: string1 = "Hello World" split this string1 using lambda function

string1 = "Hello World"
split_text = (lambda x: x.split())(string1)
print(split_text)



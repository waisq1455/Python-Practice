Question: Write a for loop to create a list of even numbers between 1 and 10
---Logic right hai but o/p list me chahiye ---

lst=[]
for x in range(1,11):
    if (x % 2) == 1:
        lst.append(x)
print(lst)
        


'''Question: Write a for loop to count down from 10 to 1 and print each number.
---Inbuilt function reversed use Kiya hai aise nhi Krna hai---'''

a=[]
for x in range(1,11):
    a.append(x)
print(a[::-1])


#Question: Write a for loop to create a list of even numbers between 1 and 10
ev=[]
for x in range(1,11):
    if (x % 2) == 1:
        ev.append(x)
print(ev)
        
#Qt 2] How can you find all the odd numbers in a given list of integers using Python?

a=[]
for x in range(1,20):
    if x%2==0:
        a.append(x)

print(a)




"""
*       * 
  *   *   
    *     
  *   *   
*       * 
"""
#range(1,5)==(1,2,3,4)
#range(5)==(0,1,2,3,4)

for i in range(5):#(0,1,2,3,4)
    for j in range(5):#(0,1,2,3,4)
        if i==j or i+j==4: # 0==0-*,1==1 *,2==2--*,
            print('*',end='')
        else:
            print(' ',end='')
    print()
#0(0,1,2,3,4) 1(0,1,2,3,4) 2(0,1,2,3,4) 3(0,1,2,3,4) 4(0,1,2,3,4)




#compression
z=[x for x in range(1,20) if x%2!=0]
print(z)

#Qt 5] How can you create a list using list comprehension with a nested for loop in Python?
a=[(i,j) for i in range(3) for j in range(2)]
print(a)

#Question: Write a program that uses nested if statements to classify a student's grade based on their marks.

# Input: marks obtained by the student
marks =50

# Check if marks are within the valid range
if marks >= 0 and marks <= 100:
    # Nested if statements to classify the grade
    if marks >= 90:
        grade = 'A'
    elif marks >= 80:
        grade = 'B'
    elif marks >= 70:
        grade = 'C'
    elif marks >= 60:
        grade = 'D'
    else:
        grade = 'F'
else:
    grade = 'Invalid marks'

# Output the result
print(f"The student's grade is: {grade}")




for i in range(1,5):
    print(str(i)*i)

for i in range(1,5):
    print('1'*i)

for i in range(1,5):
    for j in range(i):
        print(i,end='')
    print()

for i in range(5):
    for j in range(i):
        print(i,end='')
    print()

l=['A','B','C','D','E','F']
for i in range(1,4):
    for k in l:
        print(k*i,end='')
    print()

for k in l:
    for i in range(1,4):
        print(k*i,end=' ')
    print()

for i in range(1,5):
    print('A'*i)

l = ['A', 'B', 'C', 'D', 'E', 'F']
for i in range(1, 5):
    for k in l[:i]:
        print(k, end='')
    print()






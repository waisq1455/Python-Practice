'''
1. Print the following pattern:

1
2 2
3 3 3
4 4 4 4 
5 5 5 5 5'''

row =6
for i in range(row):
    for j in range(i):
        print(i,end=" ")
    print()



'''5. Print the following pattern:
A
B B
C C C
D D D D
E E E E E'''

row=5
ascii_value = 65
for x in range(row):
    for i in range(x+1):
        alphabet = chr(ascii_value)
        print(alphabet,end=" ")
    ascii_value +=1
    print() 



4. Print the following pattern:
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5

row=6
for i in reversed(range(1,row)):
    for j in range(1,i+1):
        print(row-i,end=" ")
    print()


'''3. Print the following pattern:
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
'''
row=5
for i in range(row):
    for x in range(i+1):
        print(row-x,end=" ")
    print()


'''1. Print the following pattern:
1
2 2
3 3 3
4 4 4 4 
5 5 5 5 5
'''
row=6
for i in range(row):
    for x in range(i):
        print(i,end=" ")
    print()



2. Print the following pattern:
1
0 1
0 1 2
0 1 2 3
0 1 2 3 4

4. Print the following pattern:
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5







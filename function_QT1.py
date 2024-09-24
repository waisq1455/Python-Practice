#Question 10: Write a function that generates the first n numbers of the Fibonacci sequence.

def fibonacci_for_loop(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
fibonacci_for_loop(15)





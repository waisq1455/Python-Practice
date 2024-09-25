1) create decorators that adds 1 to the result of a function 
def add_one(func):
    def one(a,b):
        result= func(a,b)
        return result + 1
    return one

@add_one
def example_fuction(a,b):
    return a+b
print(example_fuction(6,6))


#2)how to print hello 10 times by  using decorator?
string="hello"

def repeat(n):
    def decor(func):
        def inner():
            for i in range(n):
                func()
        return inner
    return decor

@repeat(10)

def f1():
    print("hello")
f1()


#implementation a decorators that checks if a function input is +ve

def outer(func):
    def inner(n):
        if n>0:
            return f"+ve{n}"
        else:
            return f"-ve{n}"
    return inner

@outer
def f1(n):
    return n

print(f1(6))

print(f1(-5))



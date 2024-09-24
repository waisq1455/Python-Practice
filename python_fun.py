#Function
def fun1():
    pass
fun1()

def fun1(a,b):
    print(a-b)
fun1(100,200)

#positional arguments
#keyword arguments
#default arguments
#Variable length argu

def fun1(a,b):
    print(a-b)
fun1(b=10,a=20)


def fun1(a,b,c):
    print(a)
    print(b)
    print(c)
fun1(10,20,30)

def fun1(a,b,c):
    print(a)
    print(b)
    print(c)
fun1(10,c=100,b=40)


def fun1(a,b,c):
    print(a)
    print(b)
    print(c)
#fun1(10,a=100,c=40)#invalid

fun1(b=10,a=100,c=40)

#fun1(10,c=100,40)#invalid
fun1(a=10,c=100,b=40)#invalid


#default arguments

def fun1(a=None):
    print(a)
fun1()
fun1(500)

def fun1(a,b=None):
    print(a)
    print(b)
#fun1(20)
fun1(200,300)

"""def fun1(a,b=None,c=None,d):
    print(a)
    print(b)
    print(c)
    print(d)
fun1(100,200,300,400)
"""
#Default args rules
#def fun1(a,b=None,c=None,d)# invalid
#def fun1(a=None,b=None,c=None,d=None)#valid
#def fun1(a,b=None,c,d)#invalid
#def fun1(a,b=None,c=None,d=None)#valid
#def fun1(a,b,c,d=None)#valid

# Keywords args
"""def fun1(a,b,c):
   pass
fun1(10,a=100,c=40)#invalid
fun1(b=10,a=100,c=40)#valid
#fun1(10,c=100,40)#invalid
fun1(a=10,c=100,b=40)#invalid
"""
#Variable length arg
#*args,**kwrgs

def f1(*a):
    print(a)
f1()
f1(10,20)
f1(10,20,30,40,5,60)

def f1(**a):
    print(a)
f1()
f1(name='abc',b=20)














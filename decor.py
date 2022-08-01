#DECORATORS
#PYHTONS ARE FIRST CLASS OBJECTS::==> CAN BE USED AS ARGUMENTS 
#PYHTONS CAN BE STORED IN VARIABLES
#CAN PASS FUNCTION TO ANOTHER FUNCTION
#DECORATORS==>> uSED TO MODIFY A FUNCTION
#in decorators=>func are taken as args into another func anf then called inside the wrapper func


def first(msg):
    print(msg)


first("Hello")

second = first
second("Hello")

def inc(x):
    return x+1

def dec(x):
    return x-1

def operate(func,x):
    result=func(x)
    return result

print(operate(inc,3))
print(operate(dec,3))



def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")
print(ordinary())

pretty=make_pretty(ordinary)
print(pretty())

#decorating functions with parameters

def divide(a,b):
    return a/b

print(divide(2,5))

def smart_divide(func):
    def inner(a,b):
        print("i am going to divide",a,"and",b)
        if b==0:
            print("oopsiee!! cannot divide")
            return
        return func(a,b)
    return inner


def divide(a,b):
    print(a/b)

new_divide=smart_divide(divide)
print(divide(5,0))


import os


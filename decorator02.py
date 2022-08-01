# def decorator_function(any_function):
#     def wrapper_function(*args,**kwargs):
#         '''This is a wrapper function'''
#         print('This is extra function')
#         return any_function(*args,**kwargs)
#     return wrapper_function

# def decorator_function2(any_function):
#     '''hello'''
#     def wrapper_function(*args,**kwargs):
#         print('This is extra function')
#         return any_function(*args,**kwargs)
#     return wrapper_function

# #extra line--> "This is extra function"
# def fun1():
#     print("function-->1")

# @decorator_function
# def func2(any_value):
#     print(f"function-->2 with {any_value}")


# @decorator_function2
# def add_two_num(num1,num2):
#     ''' This function takes two number and sums'''
#     return num1+num2




# # func2(5)
# print(add_two_num(3,5))
# # print(decorator_function(5))


# #importing module
from functools import wraps
# def decorator_function3(any_function):
#     @wraps(any_function)
#     def wrapper_function(*args,**kwargs):
#         '''This is wrapper function'''
#         print('This is extra function')
#         return any_function(*args,**kwargs)
#     return wrapper_function

# @decorator_function3
# def add(a,b):
#     '''this is add function'''
#     return a+b

# add(2,3)
# print(add(2,4))
# print(add.__name__)
# print(add.__doc__) #print the doc string of wrapper function (problem)


# def show_functions(any_function):
#     @wraps(any_function)
#     def wrapper_function(*args,**kwargs):
#         print("this is extra function")
#         return any_function(*args,**kwargs)
#     return wrapper_function

# @show_functions
# def sum(a,b):
#     '''this is an add function'''
#     return a+b

# sum(4,5)
# print(sum(2,4))

# print(sum.__doc__)



import time as t
t1=t.time()
print(t1)
for i in range(1,100,1):
    print (i)
t2=t.time()
print(t2)
total_required_time=t2-t1
print(f"total_required_time is {total_required_time}")



def only_int_allowed(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        stored_data_type=[]
        for arg in args:
            stored_data_type.append(type(arg)==int)
        if all(stored_data_type):
            return any_function(*args,**kwargs)
        else:
            print("Only int is allowed")
    return wrapper_function


def only_int_allowed(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        if all([type(arg)==int for arg in args]):
            return any_function(*args,**kwargs)
        else:
            print("Only int is allowed")
    return wrapper_function



@only_int_allowed
def add_func(*args):
    total=0
    for i in args:
        total += i
    return total
print(add_func(1,2,3,4))



##decorators with argument
def which_data_allow(data_type):
    def decorator_function(any_function):
        @wraps(any_function)
        def wrapper_function(*args,**kwargs):
            if all([type(arg)==data_type for arg in args]):
                return any_function(*args,**kwargs)
            else:
                print("Only string is allowed")
        return wrapper_function
    return decorator_function

@which_data_allow(str)
def string_join(*args):
	joined_string = ""
	for i in args:
		joined_string += i
	return joined_string

print(string_join("Kritika"," Deo")) 






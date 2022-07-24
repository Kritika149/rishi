# import numbers


# def sum(a,b):
#     return a+b

# print(sum(3,4))

# def another_sum(*args):   #*-->to give as many argumensts
#     print(args)
#     print(type(args))

# print(another_sum(2,3,4))
# print(sum(3,4))


# def calculator(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     return sum
# print(calculator(0,1,5,8))






# user_numbers=str(input("enter the numbers you eant to sum(comma separated)").split(","))
# print(user_numbers)
# print(type(user_numbers))



# user_numbers=str(input("enter the numbers you want to sum"))
# print(type(user_numbers))
# int_num=int(user_numbers)
# print(type(int_num))
# def calculator_sum(*args):
#     sum2=0
#     #*list=====> unpacking of listtt

# def calculator(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     return sum
# print(calculator(0,1,5,8))



# l1=[3,4,5,6]
# num=int(input("enter a number"))
# def power(pow_num,*args):
#     l2=[]
#     for i in args:
#         l2.append(i**pow_num)
#     return l2
# print(power(num,*l1))
    


# def to_power(power_no,*args):
#     if args:
#         return[i**power_no for i in args]
#     else:
#         return"you did not pass any args"
# print(to_power(num,*l1))    

# list_to_num=input("enter a number to form list:").split(",")
# print(*list_to_num)


#kwargs takes value in dictionary

def sum_all_num(**kwargs):
    print(type(kwargs))

    for key,value in kwargs.items():
        print(f"{key}:{value}")

print(sum_all_num(first_name="Arayama",last_name="sharma"))





dict={"a":1,"b":2,"c":3}

def sum_func(**kwargs):
    sum=0
    for val in kwargs.values():
        sum+=val
    return sum
print(sum_func(**dict))



##PADK (parameter,args,default,kwargs)

def user_info(name,*args,address="unknown",**kwargs):
    print(name)
    print(args)
    print(address)
    print(kwargs)

user_info("maharshi",1,2,4,address="ktm",p=12,q=13)

is_reverse=False


list_of_names=["aryama","kriitka","rushav","samay","maharshi"]


def capital(names_list,**kwargs):
    ''' to reverse you must give {is_reverse=true} either or true'''
    if kwargs.get("is_reverse"):
        return[name[-1::-1].title() for name in names_list]

    else:
        return[name.title() for name in names_list]


print(capital(list_of_names))
print(capital.__doc__)







    
    
        



# def odd_function(num):
#     dict={}
#     for items in range(0,num+1):
#         if items%2==0:
#             dict[items]="even"   
#         else:
#             dict[items]="odd"
#     return dict

# print(odd_function(10))    

def square_func(number):
    # return {k**2:("even" if (k**2)%2==0 else "odd") for k in range(number+1)}
    return {k**2: ("even" if k**2%2 else "odd") for k in range(number+1)}
print(square_func(5))


def char_count(name):
    return {char:name.lower().count(char.lower()) for char in name.lower()}
print(char_count("kritika"))




def sq_num(number1):
    return{n**2 for n in range(0,number1+1)}

print(sq_num(10))


def tuple_of_sets(num):
    return{(i,2*i)for i in range(0,num+1)}

print(tuple_of_sets(5))


name1,name2,name3,name4,name5=input("input 5 names").split(",")
all_name=[name1+name2+name3+name4+name5]



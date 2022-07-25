




# list_of_names=["aryama","kritika","rushav","samay","maharshi"]

# # # position=0
# # # for i in list_of_names:
# # #     print(f"the name {i} is in {position} position")
# #     position+=1


# # for location,name in enumerate(list_of_names):
# #     print(f"the name {name} is in {location} position")

# user_name=input("enter a name  ")
# def find_index(name_list,target_name):
#     for position,name in enumerate(name_list):
#         if name.lower()==target_name.lower():
#             return(position)
#         else:
#             print("name not found")
# print(find_index(list_of_names,user_name))


#lambda with filter

# l1=[9,8,4,7,5,6,3,4,1,5,2,8]
# l2=list(filter(lambda x: (x%2!=0),l1))
# l3=list(map(lambda x:x*2,l1))
# print(l2)
# print(l3)


# list_of_numbers=[1,8,6,4,5,3,9,7,5,1,6,4,22,58]
# def even_filter(num):
#     if num%2==0:
#         return True
#     else:
#         return False
    
# even_list=list(filter(even_filter,list_of_numbers))
# print(even_list)


# #map finctions==> iterator
# list_of_numbers=[1,8,6,4,5,3,9,7,5,1,6,4,22,58]
# def square_func(num):
#     new_list=[]
#     for i in num:
#         new_list.append(i*i)
#     return new_list
# print(square_func(list_of_numbers))





# def square(a):
#     return a*a


# list_of_numbers=[1,8,6,4,5,3,9,7,5,1,6,4,22,58]

# k_ho=list(map(lambda a:a**2,list_of_numbers))
# print(k_ho)

# for i in k_ho:
#     print(f"k_ho ==>{i}")



# #iterable vs iterator

# #iter function --> convert into iterator

# num_list=[1,2,3,4]  #iterator

# iterator_converted=iter(num_list)
# print(next(iterator_converted))
# print(next(iterator_converted))
# print(next(iterator_converted))
# print(next(iterator_converted))


# for i in num_list:
#     print(i)

#filter_function

# numbers=[5,8,4,9,66,5,7,1,4,5,3]




# def even_func(num):
#     return[x for x in num if x%2==0]
# print(even_func(numbers))

# numbers=[5,8,4,9,66,5,7,1,4,5,3]


# def even_func(list):
#     even_list=[]
#     odd_list=[]
#     for i in list:
#         if i%2==0:
#             even_list.append(i)
#         else:
#             odd_list.append(i)
    
#         return even_list,odd_list


# def filter_even2(list):
#     for i in list:
#         return i%2==0 

# def filter_even3(list):
#     return[i for i in list if i%2==0]

# def even_func(i):
#     return i%2==0
       
# print(filter(even_func(numbers)))
# even_list=tuple(filter(even_func,numbers))
# even_list2=list(filter(lambda a:a%2==0,numbers))
# print (even_list)
# print (even_list2)



#zip function

# char_list=["a","b","c","d"]
# num_list=[1,2,3,4,5,6,7,8]
# char_num_list=["A","B","C","D"]

# print(list(zip(char_list,num_list)))
# print(dict(zip(num_list,char_list)))
# print(list(zip(num_list,char_list,char_num_list)))


# #unzip function
# l=list(zip(char_list,char_num_list))
# print(l)

# l1,l2=zip(*l)
# print(l1)
# print(l2)

# # def check_even(num):
# #     if num%2==0:
# #         return True
# #     else:
# #         return False
# # even_list=list(filter(check_even,numbers))
# # print(even_list)


# user_input_num=int(input("enter a number"))
# l1=list(range(0,user_input_num+1))
# def odd_even_func(list):
#     even_list=[]
#     odd_list=[]
#     for i in list:
#         if i%2==0:
#             even_list.append(i)
#         else:
#             odd_list.append(i)
#     return [max(pair) for pair in zip(odd_list,even_list)]

# print(odd_even_func(l1))




avg_calc=lambda *args:[(sum(pair)/len(pair)) for pair in zip (*args)]
print(avg_calc([1,2,3],[4,5,6],[7,8,9]))

num_list1=[2,4,6,8,10]
num_list2=[1,3,5,7,9]

# even_list=[True,True,True]
# print(any(even_list))
# print(all(even_list))
# odd_list=[True,False,False]
# print(any(odd_list))
# print(all(odd_list))

def check_even(list):
    even_list1=[]
    for i in list:
        even_list1.append(i%2==0)
    return even_list1

print(check_even(num_list1))

print(all([num%2==0 for num in num_list1]))

def sum(*args):
    if all([(type(arg)== int or type(arg)==float) for arg in args]):
        total=0
        for num in args:
            total +=num
        return total
    else:
        return"Int or float are allowed only"

print(sum(1,3.9,1))

















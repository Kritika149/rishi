# num=int(input("enter any number"))
# list1=list(range(0,num+1))

# def give_square(given_list):
#     square_list=[]
#     for items in given_list:
#         square_list.append(items**2)
    
#     return square_list
# abc=give_square(list1)
# print(abc)

# def same_square(n):
#     return [i**2 for i in range(1,n+1)]

# print(same_square(num))

# list=["abc","def","efg"]

# def return_first(mero_list):
#     new_list=[]
#     for each in mero_list:
#         new_list.append(each[0])
#     return new_list
# print(return_first(["abc","def","efg"]))

# def return_again(mero_list):
#     return [each[0] for each in mero_list]

# def filter_even(num):
#     return[i for i in range(num+1)if (i%2==0)]
# print(filter_even(10))

def new_list(number):
    return[ (2*i) if (i%2==0) else (i*-1) for i in range(number+1)]
print(new_list(10))

#nested list
def nested_loop(num):
    return[ [k for k in range(1,num+1)] for m in range(1,num+1)]

print(nested_loop(3))

list2=["abc","def","ghi"]
def rev_list(given_list):
    rev_bhayeko_list=[]
    for items in given_list:
        rev_bhayeko_list.append(items[::-1])
    return rev_bhayeko_list
returned_val=rev_list(list2)
print(returned_val)

def rev_of_list(abc):
    return[items[::-1] for items in abc]
print(rev_of_list(["abc","def","ghi"]))
# #1) abs function ==> returns absolute value
# a=3.14
# b=-69
# c=14
# d=3+4j
# print(abs(a))
# print(abs(b))
# print(abs(c))
# print(abs(d))

# #2) all(x)  returns true if all variables in iterable are true(i.e non zero and not NONE)
# tup1=(0,True,False)
# set={1,6,9}
# dict={}
# dict2={"apple":0,"banana":1}
# dict3={0:"apple"}
# x=all(tup1)
# y=all(set)
# z=all(dict)
# v=all(dict2)
# w=all(dict3)
# print(x,y,z,v,w)

#3) any(x) ===> returns false only if all are false
# tup1=(0,True,False)
# set={1,6,9}
# dict={}
# dict2={"apple":0,"banana":1}
# dict3={0:"apple"}
# x=any(tup1)
# y=any(set)
# z=any(dict)
# v=any(dict2)
# w=any(dict3)
# print(x,y,z,v,w)

# 4) bin() ==>returns binary value of a num
# print(bin(5))


#5)round() ==> rounds off a given num
# print(round(3.3))
# print(round(3.9))
# print(round(-3.9))


#6) bool() ==>returns boolean value
# print(bool(0))
# print(bool(-5))
# print(bool(-5.6))
# print(bool(True))
# print(bool(False))
# print(bool(None))

#7)list((itersble))==> converts into list
# string1="kritika"
# tuple1=(1,2,"a")
# print(list(string1))
# print(list(tuple1))

#8) len(())==> no of characters
# print(len(string1))

#9) max(),min()
# l1=[5,8,6,7,99,11,2,1]
# print(max(l1))
# print(min(l1))

#10) map()==>returns the iterable after persorming operation
   #syntax:: map(func,(iterable))
# multiply_by_two=list(map(lambda x: x*2,l1))
# print(multiply_by_two)

#11) pow()==>value of power of 1 no to another
# print(pow(2,5))

#12) oct() ==> to find octal representation of a num
# print(oct(32))

#13)  sorted() ==> sorts nombers and alphabets
# s1=(1,2,3,4,5,8,6,9,44)
# print(sorted(s1))
# print(sorted(s1,reverse=True))
# dict={"a":"sss","g":"wq","t":2}
# print(sorted(dict))
# print(sorted(dict,key=len))


#14)  sum() ==> sum of all iterable obj
# l1=[2,7,9,2,4.5,5.5,-5]
# sum1=sum(l1)
# print(sum1)

#15)  callable()==>returns true if obj passed is callable

# def abc():
#     return 5
# res=abc
# print(callable(res))
# num1=15*5
# print(callable(num1))

#16) reversed()==>returns in reversed order

# t1=(8,9,6,7,5,3)
# for i in reversed(t1):
#     print(i,end=' ')


#17) ascii()
# print(ascii("A"))

#18) chr()==>
# print(chr(65))

#19) Class method
# class fruit:
#     def sayhi(self):
#         print("Hi, I'm a fruit") 
       
# fruit.sayhi=classmethod(fruit.sayhi)
# fruit.sayhi()

#20)  enumerate() ==> returns position 
# l1=["kritika","aryama","maharshi","rushav","samay"]

# for names in enumerate(l1):
    # print(names)

#21) filter()
# l1=[1,8,9,6,7,5]
# l2=list(filter(lambda x: x%2!=0,l1))
# print (sorted(l2))

#22) format
# a,b=2,3
# print("a={0} and b={1}".format(a,b))



numbers=[5,8,4,9,66,5,7,1,4,5,3]


def check_even(num):
    if num%2==0:
        return True
    else:
        return False
even_list=list(filter(check_even,numbers))
print(even_list)

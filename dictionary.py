#in keyword -used in condiotional and looping

any_dict = {
        "f_name" : "Maharshi",
        "age" : 23,
        "fav_song" : ["s1","s2",11,False],
        "others":{
            "fav_game":"Football",
            "fav_programming":"Python"
        }
}

print(any_dict)


if "f_names" in any_dict:
    print("present")
else:
    print("not present")

# different methods hunchha ----> keys(),value(),copy(),clear(),clear()

if "f_name" in any_dict:
    print("present")
else:
    print("not present")

if "Maharshi" in any_dict.values():
    print("present")
else:
    print("not present")



for i in any_dict:
    print(i)

for i in any_dict.values():
    print(i)

for i in any_dict.items():
    print(i)

for i,k in any_dict.items():
    print(f"the key is: {i} and the value is: {k}")

any_dict2=any_dict.copy()
print(any_dict2)
any_dict2.clear()
print(any_dict2)


dic1={"day1":"Sunday","day2":"Monday"}
dic2={"day3":"Tuesday","day4":"Wednesday"}
dic3=dic1.copy()


# add value to dic3
dic3["day5"]=["Nice day","Rainy Day"]
dic3["all_days"]=["day1","day2","day3"]
print(dic3)

print(dic1)
dic1.update(dic2)
print(dic1)


dic1.pop("day1")
print(dic1)


popped_items=dic1.pop("day2")
print(dic1)
print(popped_items)


days=dict.fromkeys(["day1","day2","day3"],"unknown")
print(days)

days2=(["day1","day2","day3"],["unknown","a","b"])
print(days2)

#print(days["day5"]) ---> gives error
print(days.get("day5")) #---->does not exist but doesnt give error
print(days.get("day3"))

if any_dict.get("address"):
    print("Present")
else:
    print("not present")


print(days.get("day5" , "Sorry! your not found your value"))    

user_info={"fname":"Aaryama","lname":"Sharma","age":19,"age":20}
print(user_info.get("age"))


num=int(input("enter a number"))

def cube(abc):
    dic_new={}
    for i in range(abc+1):
        dic_new[i]=i**3
    return dic_new

print(cube(num))

def countchar(name):
    new_dict={}
    for char in name:
        new_dict[char]=name.lower().count(char)
    return new_dict

print(countchar("kritika"))











        








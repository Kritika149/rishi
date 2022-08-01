import os 

print(os.getcwd())
path=r"C:\Users\N\OneDrive\Desktop\python training 2"


# os.mkdir("any")
# os.mkdir("any2")
# os.rmdir("any2")

# print(os.path.exists("any2"))

# if os.path.exists("any2"):
#     print("already exists")
# else:
#     os.mkdir("any3") 

#open or make new file
open("file.png","a").close()# a--> append mode

print(os.listdir())
list_dir_path=r"C:\Users\N\OneDrive\Desktop\python training 2\any3"

# print(os.listdir(list_dir_path))


#change directory
change_dir_path=r"C:\Users\N\OneDrive\Desktop\python training 2\any3"
# os.chdir(change_dir_path)
print(os.getcwd())
os.chdir(path)
print(os.getcwd())

#to find th epath of files:
for item in os.listdir():
    file_path=os.path.join(os.getcwd(),item)
    print(f"The path of this item file {item} is: --> {file_path}")

#to walk in the path of files:
print(os.walk(path))   #walk is an iterator
file_walk=os.walk(path)
print(file_walk)
for current_path,folder_names,file_name in file_walk:
    print(f"The current_path is: --> {current_path}")
    print(f"The folder name is: --> {folder_names}")
    print(f"The file name is: --> {file_name}")

import shutil
print(os.getcwd())

# shutil.rmtree("any3") #permanently delete

# any3_path=path+r"\any3"
# copy_garne_path=path+r"\any3\any2"
# shutil.copytree(path +r"\any3",copy_garne_path)


# file_path=path+r"\file.txt"
# file_ko_copy_garne_path=path+r"\any\file.txt"
# shutil.copy(file_path,file_ko_copy_garne_path)


# file_path=path+r"\file.txt"
# file_ko_move_garne_path=path+r"\any\file.png"
# shutil.move(file_path,file_ko_move_garne_path)




# list all directories and files in directory
import os

path = "../"
dir_list = os.listdir(path)
print("Files and directories in '", path,"' : ")
print(dir_list)
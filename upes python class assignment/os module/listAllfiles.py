# program to list all files in a directory and the address is taken from user

import os

directoryPath = input("Enter the address of the directory:")

# check if path exists or not
if os.path.exists(directoryPath):
    print(os.listdir(directoryPath))
   
# if path does not exists or path is incorrect     
else:
    print("entered path is incorrect")    
    
 
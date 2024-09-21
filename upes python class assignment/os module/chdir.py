# change the current working directory
import os

print("current working directory before:")
print(os.getcwd())
print()
print("current working directory after:")
os.chdir('../')
print(os.getcwd())
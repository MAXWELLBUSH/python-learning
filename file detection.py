"""
import os

file_path = "stuff/text.txt"

if os.path.exists(file_path):
    print(f"the location '{file_path}' exists'")
else:
     print(f"the location '{file_path}' doesnt  exists'")
     """

# Absolute
# create a new file in  your desktop text document,check properties and paste location

import os

file_path = "C:/Users/BUSH/Desktop/text.txt"

if os.path.exists(file_path):
    print(f"the location '{file_path}' exists'")

    if os.path.isfile(file_path):
         print("this is a file")
    elif os.path.isdir(file_path):
        print("this is a directory")
    
else:
     print(f"the location '{file_path}' doesnt  exists'")
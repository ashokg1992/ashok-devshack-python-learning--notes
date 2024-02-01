
#------------------------  FOLDER CREATED ------------------
# import os    # OS MODULE HANDLE ALL THESE TAKSS, SO WE IMPORT THIS OS MODULE
# os.mkdir('ashokfolder1') 
# output=os.listdir('.')
# print(output)

#-------------------- to check certain foler/file  is existed or not ----------------------

# import os
# import os.path
# a=os.path.exists('ashok.txt')
# b=os.path.exists('ashok1.txt')
# print('this file ashok.txt is exist:',a)
# print('this file ashok1.txt is exist:',b)


#-------------------- to remove  certain foler/file    ----------------------


# import os
# os.rmdir('ashokfolder1') # to remove direcoty
# os.remove('ashok.txt') # to delte file
# a=os.listdir('.')
# print(a)


#-------------------- to delete folder along with files in it    ----------------------

# # for this we import  shutil module
# import os
# import os.path
# import shutil
# shutil.rmtree('a')  # we are telling in this "a" folder and  the files in it are delted


#--------------------  summery of file handelinig  ----------------------



# Opening and Closing Files:
# --------------------------------

# file = open('myfile.txt', 'r')   # Opening a file in read mode
# file = open('myfile.txt', 'w')  # Opening a file in write mode
# file = open('myfile.txt', 'a')  # Opening a file in append mode
# file.close()		# Always close the file after you're done with it

# Reading from Files:
# ----------------------
# content = file.read()	# Reading the entire file
# line = file.readline()	# Reading one line at a time
# lines = file.readlines()	# Reading all lines into a list

# Writing to Files
# -----------------------
# file.write("Hello, World!\n")

# Appending to Files:
# --------------------
# Opening a file in append mode allows you to add content to the end of the file.

# file = open('myfile.txt', 'a')
# file.write("New content\n")



# Creating Directories:
# -----------------------
# You can use the os module to create directories.
# import os
# os.mkdir('mydir')  # Create a directory

# 2. Listing Files and Directories:
# -----------------------------------
# import os
# contents = os.listdir('.')  # List all files and directories in the current directory

# Checking if a File or Directory Exists:
# ------------------------------------------
# You can use the os.path module to check if a file or directory exists.
# import os.path
# os.path.exists('myfile.txt')  # Check if a file exists
# os.path.exists('mydir')	# Check if a directory exists


#  Deleting Files and Directories
# ----------------------------------
# To delete files, you can use os.remove() and to delete directories, you can use os.rmdir().
# import os
# os.remove('myfile.txt') # Delete a file
# os.rmdir('mydir')	# Delete an empty directory

#  Recursive Directory Deletion
# -----------------------------------
# To delete a directory and its contents recursively, you can use the shutil.rmtree() function.
# import shutil
# shutil.rmtree('mydir') # Recursively delete a directory

# ==================================
# Remember to always handle files carefully, and make sure to close them after you're done to free up system resources.

#  Additionally, when working with directories, be cautious about deleting files, as it's a permanent action.

# ==================================


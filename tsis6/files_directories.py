import os
import shutil

#1 Write a Python program to list only directories, files and all directories, files in a specified path.

#path = "../.."

# print("ONLY Directories:")

# for name in os.listdir(path):
# 	if os.path.isdir(os.path.join(path, name)):
# 		print(name)

# print("ONLY files")

# for name in os.listdir(path):
# 	if not os.path.isdir(os.path.join(path, name)):
# 		print(name)

# print("BOTH")
# for name in os.listdir(path):
# 	print(name)

#2 Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path

# path = os.path.join(os.getcwd(), "files_directories.py")


# print('Exist:', os.access(path, os.F_OK))
# print('Readable:', os.access(path, os.R_OK))
# print('Writable:', os.access(path, os.W_OK))
# print('Executable:', os.access(path, os.X_OK))

#3 Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.

# path = os.path.join(os.getcwd(), "files_directories.py")

# if os.path.exists(path):
# 	print("exists!")
# 	print(os.path.basename(path))
# 	print(os.path.dirname(path))
# else:
# 	print("Doesn't exist!")

#4 Write a Python program to count the number of lines in a text file.

# with open("SAMPLETXT.txt", "r", encoding="Utf8") as f:
# 	print(len(f.readlines()))

#5 Write a Python program to write a list to a file.

# l = ["sdkf", "sdjfljsdlkf", '3933', "sdfkkf33"]

# with open("SAMPLETXT2.txt", "w", encoding="Utf8") as f:
# 	for x in l:
# 		f.write(f"{x}\n")

#6 Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
# import string


# if not os.path.exists("filesAZ"):
#    os.makedirs("filesAZ")


# for letter in string.ascii_uppercase:
#    with open(os.getcwd() + '/filesAZ/' + letter + ".txt", "w") as f:
#        f.writelines(letter)

#7 Write a Python program to copy the contents of a file to another file


# shutil.copy(os.path.join(os.getcwd(), "SAMPLETXT.txt"), "/Users/nurstanduisengaliyev/Documents/Python/SAMPLE")


#8 Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.


# path = "./SAMPLETXT2.txt"

# if not os.path.exists(path):

# 	print("DOESN't EXISTS!")

# else:
# 	if os.access(path, mode = os.F_OK):
# 		os.remove(path)
# 		print("DELETED!")

# 	else:
# 		print("DOESN't EXISTS!")





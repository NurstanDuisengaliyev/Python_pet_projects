import re

def read_file(fpath: str):
    with open(fpath, mode='r', encoding='utf8') as f:
        return f.read()



file = read_file("row.txt")


#1 Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

# pattern = "а*б"
# if re.search(pattern, file) != None:
# 	print("Found a match!")
# else:
# 	print("Not Matched!")

#2 Write a Python program that matches a string that has an 'a' followed by two to three 'b'.


# pattern = "аб{2,3}"
# if re.search(pattern, file) != None:
# 	print("Found a match!")
# else:
# 	print("Not Matched!")

#3 Write a Python program to find sequences of lowercase letters joined with a underscore.

# pattern = "[a-z]+_[a-z]+"
# print(re.findall(pattern, file))


#4 Write a Python program to find the sequences of one upper case letter followed by lower case letters.

# pattern = "[A-Z][a-z]+"
# print(re.findall(pattern, file))

#5 Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'

# pattern = 'a.*b$'
# if re.search(pattern, file) != None:
#     print("Found a match")
# else:
#     print("Not Matched!") 

#6 Write a Python program to replace all occurrences of space, comma, or dot with a colon.

# txt = re.sub(" ", ":", file)
# txt = re.sub(",", ":", txt)
# # txt = re.sub(".", ":", txt)
# txt = re.sub(r"\.", ":", txt)
# print(txt)

#7 Write a python program to convert snake case string to camel case string.

# def camelCase(a: str):
#     # snake_case
#     while re.search("_.", a):
#         t = re.search("_.", a)
#         a = a[0:t.span()[0]] + a[t.span()[1] - 1].upper() + a[t.span()[1]:]
#     return a

# # a = input()# snake_case
# a = "snake_case"
# print(camelCase(a))

#8 Write a Python program to split a string at uppercase letters.

# text = "NurstanDuisengaliyevDastanulyYesIam"
# pattern = "[A-Z][^A-Z]*"
# print(re.findall(pattern, text))

#9 Write a Python program to insert spaces between words starting with capital letters.

# text = "NurstanDuisengaliyevDastanulyYesIam"
# text = re.sub(r"(\w)([A-Z])", r"\1 \2", text)
# print(text)

#10 Write a Python program to convert a given camel case string to snake case.

# def snake_case(a: str):
#     #camelCase
#     while re.search("[A-Z]", a):
#         t = re.search("[A-Z]", a)
#         a = a[0:t.span()[0]] + a[t.span()[0]].lower() + "_" + a[t.span()[1]:]
#     return a

# # a = input()
# a = "camelCaseFakdDkf"
# print(snake_case(a))

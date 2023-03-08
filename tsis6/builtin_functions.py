

#1 Write a Python program with builtin function to multiply all the numbers in a list

# list1 = [1, 2, 3, 2, -2, -4, 31]
# ans = 1
# for x in list1:
# 	ans = ans * x

# print(ans)

#2 Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

# s = input()
# ans1, ans2 = 0, 0
# for x in s:
# 	if x.isupper():
# 		ans1 += 1
# 	else:
# 		ans2 += 1
# print("Upper case: ", ans1)
# print("Lower case: ", ans2)

#3 Write a Python program with builtin function that checks whether a passed string is palindrome or not.

# word = "abba"
# word2 = word[::-1]
# if word == word2:
# 	print("Palindrome!")
# else:
# 	print("Not Palindrome")

#4 Write a Python program that invoke square root function after specific milliseconds.

# from time import sleep
# from math import sqrt

# x = int(input())
# t = int(input())

# sleep(t / 1000)

# print(f"Square root of {x} after {t} miliseconds is {sqrt(x)}")

#5 Write a Python program with builtin function that returns True if all elements of the tuple are true.

# tuple1 = (True, True, True)
# print(all(tuple1))

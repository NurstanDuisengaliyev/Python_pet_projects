def grams_to_ounces(grams):
	return 28.3495231 * grams
#1
def fahren_to_cent(F):
	return (5 / 9) * (F - 32)

#2
def solve(numheads, numlegs):
	# -2x - 2y   = -2 * numheads
	# 2x + 4y = numlegs
	# 2y = numlegs - 2 * numheads
	rabbits = (numlegs - 2 * numheads) / 2
	chickens = numheads - rabbits
	return list((chickens, rabbits))


#print(solve(35, 94))
#3
def filter_prime(numbers):
	ans = []
	for x in numbers:
		if x == 1:
			continue
		check = True
		for i in range(2, x):
			if x % i == 0:
				check = False
				break
		if check == True:
			ans.append(x)
	return ans # returning only prime numbers

#print(filter_prime([2, 2, 4, 5, 13, 1, 15]))

#4
from itertools import permutations
def all_permutations(s1):
	string_permutations = list(permutations(s1))
	string_permutations = [''.join(permutation) for permutation in string_permutations]
	print(string_permutations)



#all_permutations("abcd")
#5


def string_reversed(string):
	words = string.split()
	words.reverse()
	for word in words:
		word.strip()
		print(word, end=' ')


#string_reversed("abcde sdlkfjsldf sdlkfjsdlf sdlkd dd djdj")
#6


def has_33(nums):
	previous = None
	for x in nums:
		if x == previous:
			return True
		previous = x
	return False

#print(has_33([1, 3, 3]))
#7 

def spy_game(nums):
	cnt = 0
	for x in nums:
		if x == 0:
			cnt+= 1
		if x == 7:
			if cnt >= 2:
				return True
	return False

#print(spy_game([1,2,4,0,0,7,5])) 
print(spy_game([1,7,2,0,4,5,0]))
#8

from math import pi
def Volume(r):
	return 4/3 * pi * r**3

#9

def unique_val(arr):
	arr.sort()
	ans = []
	for i in range(1, len(arr)):
		if arr[i] != arr[i - 1]:
			ans.append(arr[i - 1])
	ans.append(arr[-1])
	return ans

#print(unique_val([0, 0, 1, -1, 5, 5, 9, 0]))
#10


def is_palindrome(a):
	if a == a[::-1]:
		return True
	else: 
		return False

#print(is_palindrome("abba"))

#11

def histogram(nums):
	for x in nums:
		print("*" * x)

#histogram([4, 9, 7])

#12

def Game():
	print("Hello! What is your name?")
	name = input()
	print(f"Well, {name}, I am thinking of a number between 1 and 20.")
	import random
	guessed_number = random.randint(1, 21)
	cnt = 0
	while True:
		print("Take a guess.")
		n = int(input())
		if n == guessed_number:
			print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
			break
		else:
			cnt += 1

#Game()
#13 





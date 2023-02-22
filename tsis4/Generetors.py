#Create a generator that generates the squares of numbers up to some number N.
def square_numbers(n):
	for i in range(1, n + 1):
		yield i**2

for value in square_numbers(5):
	print(value)

#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

n = int(input())

def even_numbers(n):
	for i in range(0, n + 1, 2):
		yield i

for value in even_numbers(n):
	if value + 2 <= n:
		print(value, end=', ')
	else:
		print(value)

#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

def divisible34(n):
	for i in range(0, n + 1, 12):
		yield i

for value in divisible34(100):
	print(value)

#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

def squares(a, b):
	for i in range(a, b + 1):
		yield i**2

for value in squares(a = 13, b = 17):
	print(value, end=' ')

#Implement a generator that returns all numbers from (n) down to 0.

def func(n):
	for i in range(n, -1, -1):
		yield i
print()
for value in func(10):
	print(value, end=' ')


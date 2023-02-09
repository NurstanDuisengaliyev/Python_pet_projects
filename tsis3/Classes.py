class C1():
	"""docstring for C1"""
	def getString(self):
		self.string = input()

	def printString(self):
		print(self.string.upper())

# s = C1()
# s.getString()
# s.printString()
#1 _________________________________

class Shape():
	"""docstring for Shape"""
	def __init__(self, length):
		self.length = length

	def area(self):
		print(0)
		
class Square(Shape):
	def __init__(self, length):
		super().__init__(length)

	def area(self):
		print(self.length ** 2)


# shape1 = Shape(2)
# square1 = Square(5)
# shape1.area()
# square1.area()

#2 _________________________________

class Rectangle(Shape):
	"""docstring for Rectangle"""
	def __init__(self, length, width):
		self.width = width
		super().__init__(length)

	def area(self):
		print(self.width * self.length)

# rectangle1 = Rectangle(10, 3)
# rectangle1.area()

#3 ______________________________________

from math import sqrt

class Point:
	def __init__(self, x, y):
		self.x, self.y = x, y

	def show(self):
		print(self.x, self.y)

	def move(self, new_x, new_y):
		self.x = new_x
		self.y = new_y

	def dist(self, x, y):
		distance = sqrt((self.x - x)**2 + (self.y - y)**2)
		print(distance)

# point1 = Point(5, 5)
# point1.show()
# point1.move(1, 1)
# point1.dist(1, 10)

#4______________________________________________

class Account:
	def __init__(self, owner, balance):
		self.owner = owner
		self.balance = balance
	
	def deposit(self, amount):
		self.balance += amount
		print("Your current balance = {}".format(self.balance))

	def withdraw(self, amount):
		if self.balance >= amount:
			self.balance -= amount
			print("Your current balance = {}".format(self.balance))
		else:
			print("Invalid Withdrawal! The amount shouldn't exceed your balance!")
			print("Try it again.")


# acc = Account("Adil", 103)
# acc.deposit(3)
# acc.withdraw(102)
# acc.deposit(2)
# acc.withdraw(45)
# acc.withdraw(1)

#5______________________________________________

list1 = [2, 3, 2, 5, 6, 6, 6, 1, 7, 4, 10, 11]
isprime = lambda x: all(x % i != 0 for i in range(2, x))

primes = list(filter(isprime, list1))

# print(primes)

#6______________________________________________



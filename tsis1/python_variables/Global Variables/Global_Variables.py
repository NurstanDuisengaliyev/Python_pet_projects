x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#-----------------
x = "awesome"

def myfunc2():
  x = "fantastic"
  print("Python is " + x)

myfunc2()

print("Python is " + x)

#--------------------

def myfunc3():
  global y
  y = "fantastic"

myfunc3()

print("Python is " + y)
#--------------------

z = "awesome"

def myfunc4():
  global z
  z = "fantastic"

myfunc4()

print("Python is " + z)

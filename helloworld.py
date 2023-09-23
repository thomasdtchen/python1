print("Hello, World!")

if 5 > 2:
    print("5 > 2")
    print("also 2 < 5")

# variable
x = 5
y = "Hello, World!"
print(x)
print(y)

"""
This is a comment
written in
more than just one line
"""

x = str(3)
y = int(3)
z = float(3)

print(type(x))
print(type(y))
print(type(z))

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


x = 5
y = 10
print(x + y)

x = 5
y = "John"
#print(x + y)

x = 5
y = "John"
print(x, y)

x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()
print("Python is " + x)

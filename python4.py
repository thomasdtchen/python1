thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))  #3
print(range(len(thislist))) #range(0, 3)
for i in range(len(thislist)):
    print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

print("------------")
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

print("------------")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

print("------------")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

print("---------------------------------")
print(range(10))
newlist = [x for x in range(10)]
print("----")
print(newlist)
newlist = [x for x in range(10) if x < 5]
print("----")
print(newlist)
newlist = [x.upper() for x in fruits]
print("----")
print(newlist)
newlist = ['hello' for x in fruits]
print("----")
print(newlist)
newlist = [x if x != "banana" else "orange" for x in fruits]
print("----")
print(newlist)
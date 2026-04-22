print("Helllo, AI Playground!")
#Declaring variables
name = "Alice"
age = 30
height = 5.5
is_student = True
print(name, age, height, is_student)
#List in Python
list = [1, 2, 3, 4, 5]
print(list)
for i in list:
    print(i)
 #lists in Python are mutable
list.insert(0, 10)
print(list)
list.reverse()
print(list)
#Dictionaries in Python
dict = {"name": "Alice", "age": 30, "city": "New York"}
dict["country"] = "USA"
dict.setdefault("email", "test@gmail.com")
dict.update({"phone": "123-456-7890"})
dict.popitem()
print(dict)
dict.clear()
print(dict)
#Functions in Python
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))
#if-else statement and loops in Python
if 5 > 3:
    print("5 is greater than 3")
else:    print("5 is not greater than 3")
for i in range(5):
    print(i)
i=0
while i < 5:
    print(i)
    i += 1
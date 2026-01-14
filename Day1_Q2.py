#Question – List, Dictionary & Set Comprehensions

#Given a list:
data = [1, 2, 3, 4, 5, 6, 2, 4]
#Write a program to:

#1. Create a list comprehension to store squares of all numbers
squares = list(map(lambda x:x**2, data))
print(squares)

#2. Create a set comprehension to store only unique even numbers
unique_even_num = set(filter(lambda x:x%2==0,data))
print(unique_even_num)

#3. Create a dictionary comprehension where the key is the number and the value is its cube
cubes = {x: x**3 for x in data}
print(cubes)
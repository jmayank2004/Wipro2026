class Student:
    name="Rohan"
    age=23
s1=Student()
print(s1.name)
print(s1.age)

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

name=input("Enter your name:")
age=int(input("Enter your age:"))

s1=Student(name,age)
s1.display()
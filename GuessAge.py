"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that
they will turn 100 years old.
"""
name = input("Please input your name: ")
age = int(input("Please input your age: "))

year = 2018+(100-age)
print(name, "will be 100 in", year)

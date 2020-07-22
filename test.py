class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

tom = Person("Tom", 15)
print(dir(tom))
print(tom.name)
print(tom.age)

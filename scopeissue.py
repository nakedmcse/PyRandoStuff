# Inheritance issue = __ means private and cannot be overridden in a subclass
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __incAge(self):
        self.age = self.age

    def getAge(self):
        self.__incAge()
        print(self.age)

class Whore(Person):
    def __incAge(self):
        self.age += 1

aPythonWhore = Whore("Walker",50);

aPythonWhore.getAge()
aPythonWhore.getAge()
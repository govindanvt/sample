
class Person:
    def __init__(self,f,l):
        self.fName=f
        self.lName=l
    def __str__(self):
        return self.fName+" "+self.lName
class Employee(Person):
    def __init__(self,first,last,staffnum):
        super(). __init__(self,first,last)
        self.staffnumber=staffnum
    def __str__(self):
        return self.fName+" "+self.lName+" "+self.staffnumber
x=Person("Hari","Abhi")
y=Employee("Govind","Abhi","1007")
print(x)
print(y)
#syntax of inheritance
#class DerivedClass

class Person:
    def __init__(self,f,l):
        self.fName=f
        self.lName=l
    def Name(self):
        return self.fName+" "+self.lName
class Employee(Person):
    def __init__(self,first,last,staffnum):
        Person. __init__(self,first,last)
        self.staffnumber=staffnum
    def GetEmp(self):
        return self.Name()+","+self.staffnumber
x=Person("Hari","Abhi")
y=Employee("Govind","Abhi","1007")
print(x.Name())
print(y.GetEmp())
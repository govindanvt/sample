class Person:
    def __init__(self,f,l,a):
        self.fName=f
        self.lName=l
        self.age=a

    def __str__(self):
        return self.fName+" "+self.lName+","+str(self.age)

class Employee(Person):
    def __init__(self,first,last,age,staffnum):
        super(). __init__(first,last,age)
        self.staffnumber=staffnum

    def __str__(self): 
        return super(). __str()+","+self.staffnumber

x=Person("Hari","Abhi","27")
y=Employee("Govind","Abhi",25,"1007")
print(x)
print(y)
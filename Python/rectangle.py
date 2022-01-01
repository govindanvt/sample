class rectangle:
    def __init__(self,b,l):
        self.b=b
        self.h=l
    def area(self):
        return self.b*self.h
a=int(input("Enter the Breadth:"))
b=int(input("Enter the Breadth:"))
obj=rectangle(a,b)
print("Area of rectangle :",obj.area())
print()

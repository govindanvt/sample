import math
class Circle:
    def __init__(self,r): #Consturctr
        self.r=r
    def setRadius(self,r):
        self.r=r
    def getRadius(self):
        return self.r
    def area(self):
        return math.pi*self.r**2
    def __add__(self,another_cir):
        return Circle(self.r+another_cir.r)
c1=Circle(4)
print(c1.getRadius())
c2=Circle(5)
print(c2.getRadius())
c3=c1+c2 
print(c3.getRadius())
print("c1 area is: ",c1.area())
print("c2 area is: ",c2.area())
print("c3 area is: ",c3.area())
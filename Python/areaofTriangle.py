import math
x=int(input("Enter the value of 1st side of Triangle: "))
y=int(input("Enter the value of 2nd side of Triangle: "))
z=int(input("Enter the value of 3rd side of Triangle: "))
s=(x+y+z)/2
area=math.sqrt(s*(s-x)*(s-y)*(s-z))
print("Area of the triangle is: ",round(area,2))
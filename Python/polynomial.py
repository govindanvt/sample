import math
print("Enter the coefficent of the form ax^3 + bx^2 + cx + d")
a=[]
for i in range(0,4):
    co=int(input("Enter the Coefficient: "))
    a.append(co)
x=int(input("Enter the value of x: "))
sum=0
j=3
for i in range(0,3):
    while j>0:
        sum=sum+(a[i]*math.pow(i,j))
        break
    j=j-1
sum=sum+a[3]
print("The value of polynomial is: ",sum)
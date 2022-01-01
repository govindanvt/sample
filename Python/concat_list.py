a=[]
b=[]
n=int(input("Enter no.of Elements in list 1: "))
for i in range(1,n+1):
    a1=int(input("Enter the elements: "))
    a.append(a1)
m=int(input("Enter no.of Elements in list 2: "))
for i in range(1,m+1):
    b1=int(input("Enter the elements: "))
    b.append(b1)
c=a+b
c.sort()
print("The new Sorted list is: ",c)
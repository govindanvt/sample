a=[]
n=int(input("Enter the number of elements in list: "))
for x in range(0,n):
    b=int(input("Enter Elements "+ str(x+1)+":"))
    a.append(b)
temp=a[0]
a[0]=a[n-1]
a[n-1]=temp
print("New list is: ")
print(a)
a=[]
n=int(input("Enter the number of Elements: "))
for i in range(1,n+1):
    b=int(input("Enter the numbers: "))
    a.append(b)
for i in range(0,len(a)):
    for j in range(0,len(a)-i-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print("The second largest number is: ",a[n-2])
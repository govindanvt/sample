a=[]
n=int(input("Enter no.of elements: "))
for i in range(1,n+1):
    b=int(input("Enter the numbers in the list: "))
    a.append(b)
a.sort()
print("The Largest element is: ",a[n-1])
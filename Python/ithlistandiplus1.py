a=[]
n = int(input("Enter no.of Elements in list: "))
for i in range(0,n):
    b=int(input("Enter Elements " + str(i+1) + ":"))
    a.append(b)
alist=[sum(a[0:i+1]) for i in range(0,len(a))]
print("The orginal list is: ",a)
print("The new list is: ",alist)

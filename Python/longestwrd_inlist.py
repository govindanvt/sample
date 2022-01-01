a=[]
n=int(input("Enter no.of elements in list: "))
for i in range(0,n):
    b=input("Enter Word " + str(i+1) + ":")
    a.append(b)
max=len(a[0])
temp=a[0]
for i in a:
    if len(i)>max:
        max=len(i)
        temp=i
print("The word the longest length is: ")
print(temp)
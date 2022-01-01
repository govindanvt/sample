a=[]
n=int(input("Enter the no.of elements in list: "))
for i in range(1,n+1):
    b=int(input("Enter the elements: "))
    a.append(b)
odd=[]
even=[]
for j in a:
    if j%2==0:
        even.append(j)
    else:
        odd.append(j)
print("The even list: ",even)
print("The Odd list: ",odd)
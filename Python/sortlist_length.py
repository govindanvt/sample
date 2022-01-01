a=[]
n=int(input("Enter the number of Elements: "))
for i in range(1,n+1):
    b=input("Enter the Elements(Words): ")
    a.append(b)
a.sort(key=len)
print(a)
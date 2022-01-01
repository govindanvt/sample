a=[]
n=int(input("Enter the no.of Elements in List 1: "))
for i in range(1,n+1):
    a1=int(input("Enter the Elements: "))
    a.append(a1)
b=[]
m=int(input("Enter the no.of Elements in List 2: "))
for i in range(1,n+1):
    b1=int(input("Enter the Elements: "))
    b.append(b1)
union=list(set().union(a,b))
print("The Union of two list is: ",union)
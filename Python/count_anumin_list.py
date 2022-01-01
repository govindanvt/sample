a=[]
n=int(input("Enter no.of elements in the list: "))
for i in range(1,n+1):
    b=int(input("Enter the Elements: "))
    a.append(b)
m=0
num=int(input("Enter the number to be counted: "))
for j in a:
    if j==num:
        m+=1
print("Number of times ",num," appear is ",m)

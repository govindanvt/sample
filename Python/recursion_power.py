def powernum(n,m):
    if m==1:
        return n
    if m!=1:
        return n*powernum(n,m-1)
n=int(input("Enter the number: "))
m=int(input("Enter the power: "))
print("The result is: ",powernum(n,m))
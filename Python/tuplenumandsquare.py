lr=int(input("Enter the Lower range: "))
ur=int(input("Enter the Unpper range: "))
a=[(x,x**2) for x in range(lr,ur+1)]
print(a)
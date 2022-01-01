l=int(input("Enter the Upper Limit: "))
u=int(input("Enter the Lower Limit: "))
a=[]
a=[x for x in range(1,u+1) if (int(x**0.5))**2==x and sum(list(map(int,str(x))))<10]
print(a)
n=int(input("Provide a value to n: "))
for i in range(1,n+1):
    a=[]
    for j in range(1,i+1):
        print(j,sep=" ",end=" ")
        if j<i:
            print("+",sep=" ",end=" ")
        a.append(i)
    print()

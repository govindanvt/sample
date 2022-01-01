n=int(input("Enter the Upper Limit: "))
s=set(range(2,n+1))
while s:
    p=min(s)
    print(p,end="\t")
    s-=set(range(p,n+1,p))
print()
    
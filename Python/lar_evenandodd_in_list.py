n=int(input("Enter howmuch value add in the list: "))
b=[]
for i in range(0,n):
    a=int(input("Elements: "))
    b.append(a)
c=[]
d=[]
for i in b:
    if i%2==0:
        c.append(i)
    else:
        d.append(i)
c.sort()
d.sort()
c1=0
c2=0
for k in c:
    c1=c1+1
for j in d:
    c2=c2+1
print("Largest even number: ",c[c1-1],"\nLargest odd number: ",d[c2-1])
print()
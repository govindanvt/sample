print("Enter the limit:  ")
l=int(input())
c=0
m=2
while c<l:
    for i in range(1,m+1):
        a=m*m-i*i
        b=2*m*i
        c=m*m+i*i
        if c>l:
            break
        if a==0 or b==0 or c==0:
            break
        print(a,b,c)
    m=m+1
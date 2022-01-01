f=0
x=int(input("Enter a value: "))
if x<=1:
    print("1 is not prime")
else:
    for i in range(2 ,x//2):
        if (x%i)!=0: f=1
        i=i+1
    if f==0:
        print("prime number")
    else:
        print("not prime")
 

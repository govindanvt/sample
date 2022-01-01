x=int(input("Enter an Integer value: "))
a=[]
for i in range(2,x+1):
    if x%i==0:
        a.append(i)
if x==a[0]:
    print("The number is Prime number")
a.sort()
print("The smallest divisible of the Integer is: ",a[0])       
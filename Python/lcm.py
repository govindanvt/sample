m=int(input("Enter the 1st number: "))
n=int(input("Enter the 2nd number: "))
if m>n:
    a=n
else:
    a=m
while 1:
    if a%m==0 and a%n==0:
        print("LCM is: ",a)
        break
    a+=1
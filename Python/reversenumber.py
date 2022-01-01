x=int(input("Enter the Number: "))
r=0
while x>0:
    d=x%10
    r=r*10+d
    x=x//10
print("The reverse of the number: ",r)
    
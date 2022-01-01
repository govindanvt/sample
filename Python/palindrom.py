x=int(input("Enter a number to check Palindrom: "))
temp=x
r=0
b=0
while x>0:
    b=x%10
    r=r*10+b
    x=x//10
if temp==r:
    print("The number ",temp,"is palindrom")
else:
    print("The number ",temp,"is not palindrom")

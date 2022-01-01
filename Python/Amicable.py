a=int(input("Enter the 1st Number: "))
b=int(input("Enter the 2nd Number: "))
sum1=0
sum2=0
for i in range(1,a):
    if a%i==0:
        sum1+=i
for j in range(1,b):
    if b%j==0:
        sum2+=j
if sum1==b and sum2==a:
    print("Number is Amicable...")
else:
    print("Number is not Amicable...")

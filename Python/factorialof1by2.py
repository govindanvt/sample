import math
n=int(input("Enter the number of terms: "))
sum=1
for i in range(2,n+1):
    sum=sum+(1/math.factorial(i))
print("The sum of the series is: ",round(sum,2))
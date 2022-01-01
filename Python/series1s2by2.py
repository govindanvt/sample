n=int(input("Enter the number of terms: "))
x=int(input("Enter the value of x: "))
sum=1
for i in range(2,n+1):
    sum=sum+((x**i)/i)
print("The sum of the series is: ",round(sum,2))
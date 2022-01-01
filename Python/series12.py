print("The series is 1+1/2+1/3+.......+1/N")
n=int(input("Enter the value of n: "))
sum=1
for i in range(1,n+1):
    sum=sum+(1/i)
print("The sum of series ",rsound(sum,2))
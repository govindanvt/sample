n=int(input("Enter a Integer: "))
print("The divisors of the number are: ")
for i in range(1,n+1):
    if n%i==0:
        print(i)
    
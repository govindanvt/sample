m=int(input("Enter the range: "))
print("\nThe range of prime numbers are: ")
for a in range(2,m+1):
    k=0
    for i in range(2,a//2+1):
        if a%i==0:
            k+=1
    if k<=0:
        print(a)




























































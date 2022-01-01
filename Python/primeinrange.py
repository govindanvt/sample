n=int(input("Enter the Number: "))
k=0
for i in range(2,n//2+1):
    if n%i==0:
        k+=1
if k==0:
    print("Number is Prime...")
else:
    print("Number is not Prime...")
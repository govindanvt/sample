x=int(input("Enter the number: "))
add=0
for i in range(0,x):
    m=x%10
    add=add+m
    x=x//10
print("The sum of each digit of the number is: ",add)
import random
a=[]
n=int(input("Enter no.of Elements: "))
for j in range(n):
    a.append(random.randint(1,20))
print("Randomised list is: ",a)
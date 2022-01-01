l=[]
def sumdigit(b):
    if b==0:
        return 1
    dig=b%10
    l.append(dig)
    sumdigit(b//10)
n=int(input("Enter a number: "))
sumdigit(n)
print(sum(l))
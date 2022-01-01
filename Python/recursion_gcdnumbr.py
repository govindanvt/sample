def gcdnum(a,b):
    if b==0:
        return a
    else: 
        return gcdnum(b,a%b)
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
GCD=gcdnum(a,b)
print("GCD= ",GCD)
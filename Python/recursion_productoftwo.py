def prodct(a,b):
    if a<b:
        return prodct(b,a)
    elif b!=0:
        return a+prodct(a,b-1)
    else:
        return 0
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
print("Product of two numbers: ",prodct(a,b))
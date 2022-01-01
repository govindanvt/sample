def count_setbits(n):
    c=0
    while n:
        n&=n-1
        c+=1
    return c

#main
n=int(input("Enter n: "))
print("Number of set bits:", count_setbits(n))
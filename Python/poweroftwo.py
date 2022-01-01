def is_poweroftwo(n):
    #return True if n is apower of two
    if n<=0:
        return False
    else: 
        return n & (n-1) ==0

#main
n=int(input("Enter a number: "))
if is_poweroftwo(n):
    print("{} is a power of two..", format(n))
else: 
    print("{} is not a power of two..", format(n))
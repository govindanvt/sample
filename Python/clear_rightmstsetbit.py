def clear_rightmost_setbit(n):
    #clear rightmost set bit of n and return it.
    return n & (n-1)

#main
n=int(input("Enter a number: "))
ans=clear_rightmost_setbit(n)
print('n with its rightmost set bit cleared equals: ', ans)
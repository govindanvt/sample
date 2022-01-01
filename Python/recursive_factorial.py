def factor(n):
    if n<=1:
        return 1
    else:
        return(n*factor(n-1))
n=int(input("Enter number: "))
print("Factorial: ",factor(n))
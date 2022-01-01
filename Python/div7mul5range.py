Lrange=int(input("Enter the Lower Range: "))
Urange=int(input("Enter the Upper Range: "))
for i in range (Lrange,Urange+1):
    if i%7==0 and i%5==0:
        print(i)
print("THESE ARE THE NUMBERS DIVISIBLE BY 7 AND MULTIPLES OF 5 IN THE ",Lrange,"AND",Urange)
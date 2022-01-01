import math
def cosine(x,n):
    cosx=1
    sine=-1
    for i in range(2,n,2):
        pi=22/7
        y=x*(pi/180)
        cosx=cosx + (sine*(y**1))/math.factorial(i)
        sine = -sine
    return cosx
x=int(input("Enter the value of x in degrees: "))
n=int(input("Enter the number of terms: "))
print(round(cosine(x,n),2)) 
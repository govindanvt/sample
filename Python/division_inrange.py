r1=int(input("Enter the first limit: "))
r2=int(input("Enter the second limit: "))
div=int(input("Enter the divident: "))
for i in range(r1,r2):
    if i%div==0:
         print(i)
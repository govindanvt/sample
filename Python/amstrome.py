n=int(input("ENTER A NUMBER TO CHECK AMSTROME: "))
a=list(map(int,str(n)))
b=list(map(lambda x:x**3,a))
if(sum(b)==n):
    print("THE NUMBER IS AMSTROME...")
else:
    print("THE NUMBER IS NOT AMSTROME...")
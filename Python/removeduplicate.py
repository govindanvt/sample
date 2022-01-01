a=[]
n=int(input("Enter the number of elements in list: "))
for x in range(0,n):
    b=int(input("Enter Elements "+ str(x+1)+":"))
    a.append(b)
m=set()
uni=[]
for x in a:
    if x not in m:
        uni.append(x)
        m.add(x)
print("Non-duplicate items: ")
print(uni)
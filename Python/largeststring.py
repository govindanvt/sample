s=input("Enter 1st string: ")
t=input("Enter 2st string: ")
c=0
w=0
for i in s:
    w+=1
    if i==' ':
        w+=1
for i in t:
    c+=1
    if i==' ':
        c+=1
if w>c:
    print("The largest String is :",s)
else:
    print("The largest String is :",t)

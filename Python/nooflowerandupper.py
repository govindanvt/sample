s=input("Enter a string: ")
c=0
d=0
for i in s:
    if i.islower():
        c+=1
    elif i.isupper():
        d+=1
print("The number of Lowercase character: ",c)
print("The number of Uppercase character: ",d)    
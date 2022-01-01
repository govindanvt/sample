s=input("Enter a String(both words and digit): ")
c=0
d=0
for i in s:
    if i.isdigit():
        c+=1
    d+=1
print("The number of Digits are: ",c)
print("The number of Alphabets are: ",d)

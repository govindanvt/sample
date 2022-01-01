s=input("Enter a string: ")
c=0
for i in s:
    c+=1
new=s[0:3]+s[c-13:c-3]+s[c-3:c]
print("Newly formed string is: \n",new)   
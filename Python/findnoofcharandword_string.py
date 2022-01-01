s=input("Enter a string: ")
c=0
w=0
for i in s:
    c+=1
    if i==' ':
        w+=1
print("Number of words in the string: ",w)
print("Number of character in the string: ",c)
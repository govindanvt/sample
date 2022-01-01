def rever(s):
    if len(s)==0:
        return s
    else: 
        return rever(s[1:]) + s[0]
s=str(input("Enter the string to be reversed: "))
print(rever(s))
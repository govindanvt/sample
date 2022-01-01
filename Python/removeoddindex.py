def modify(s):
    f = " "
    for i in range(len(s)):
        if i%2!=0:
            f+=s[i]
    return f
s=input("Enter a string: ")
print("Modified String: ",modify(s))
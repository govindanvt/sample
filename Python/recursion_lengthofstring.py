def length(s):
    if not s:
        return 0
    return 1 + length(s[1::2]) + length(s[2::2])
a=[1,2,5]
print("Length of the string is: ",a)
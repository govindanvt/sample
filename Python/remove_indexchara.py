def remov(str, n):
    f = str[:n]
    l = str[n+1:]
    return f+l
str = input("Enter the string: ")
n=int(input("Enter the index of the character to remove: "))
print("Modified string: ")
print(remov(str, n))
s1=input("Enter 1st String: ")
s2=input("Enter 2nd String: ")
a=list(set(s1)^set(s2))
print("The letters are: ")
for i in a:
    print(i)
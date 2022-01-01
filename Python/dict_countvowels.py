s=input("Enter String: ")
c=0
vowels = set("aeiou")
for i in s:
    if i in vowels:
        c+=1
print("Count of the vowels is: ",c)
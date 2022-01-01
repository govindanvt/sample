s=input("Enter a Sentence: ")
w=input("Enter a Word to search: ")
a=[]
c=0
a=s.split(" ")
for i in range(0,len(a)):
    if w==a[i]:
        c+=1
print("Count of the word ",w,"is: ",c)

a=[]
n=int(input("Enter no.of Elements in the list: "))
for i in range(0,n):
    b=input("Enter Elements in words " + str(i+1) + ":")
    a.append(b)
print(a)
c=[]
count=0
r=input("Enter word to remove: ")
n=int(input("Enter the occurence to remove: "))
for i in a:
    if i==r:
        count+=1
        if count!=n:
            c.append(i)
    else: 
        c.append(i)
if count==0:
    print("Item not found...")
else:
    print("The no.of repetitions is: ",count)
    print("The Updated List is: ",c)
    print("The Distinct elements are: ",set(a))
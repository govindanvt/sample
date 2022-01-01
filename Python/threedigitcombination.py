x=int(input("Enter the 1st number: "))
y=int(input("Enter the 2nd number: "))
z=int(input("Enter the 3rd number: "))
d=[]
d.append(x)
d.append(y)
d.append(z)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if i!=j and j!=k and k!=i:
                print(d[i],d[j],d[k])
print("\n\nTotal Combination is: ",i+j+k)


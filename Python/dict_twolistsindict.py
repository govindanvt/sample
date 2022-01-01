k=[]
v=[]
n=int(input("Enter of elements for dictionary: "))
print("For keys: ")
for i in range(0,n):
    ele=input("Enter the Key elements "+str(i+1) + ":")
    k.append(ele)
print("For Values: ")
for i in range(0,n):
    ele=input("Enter the Value elements "+str(i+1) + ":")
    v.append(ele)
d=dict(zip(k,v))
print("The Dictionary \n D = ",d)
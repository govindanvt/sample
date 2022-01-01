t=0
avg=0
a=[]
print("Enter 5 numbers: ")
for i in range(5):
    x=int(input())
    a.append(x)
    t=t+x
print("Sum=", t)
avg=t/5
print("Avarage=", round(avg,2))

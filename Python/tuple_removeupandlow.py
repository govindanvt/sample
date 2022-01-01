y=[('A','12CS040'),('B','12CS450'),('C','12CS170'),('D','12CS055'),('E','12CS110')]
low=int(input("Enter Lower roll number (Starting with 12CS): "))
up=int(input("Enter Upper roll number (Starting with 12CS): "))
l='12CS0'+str(low)
u='12CS'+str(up)
p=[x for x in y if x[1]>l and x[1]<u]
print(p)
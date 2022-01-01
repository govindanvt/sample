x=str(input("Enter a file name with .txt extension: "))
f2=open(x,"r")
line=f2.readline()
while line!="":
    print(line)
    line=f2.readline()
f2.close()
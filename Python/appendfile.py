fo=open("append.txt","a")
for i in range(20):
    fo.write("This is line %d\r\n"%(i+1))
s="hello all this is append operation...!!!"
fo.write(s)
fo.close()
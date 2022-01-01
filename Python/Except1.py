try:
    fo=open("abc.txt","r")
except FileNotFoundError:
    s="No such file found"
else:
    s=fo.read()
finally:
    print(s)
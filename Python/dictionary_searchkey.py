d={'A':2,'B':12,'C':8,'D':74}
s=input("PLease enter the Key to search: ")
if s in d.keys():
    print("Key is present and the value of the key is: ",d[s])
else:
    print("Key is not prsent...!")
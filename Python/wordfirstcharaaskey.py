t_str=input("Enter a String: ")
len = t_str.split()
d={}
for i in len:
    if i[0] not in d.keys():
        d[i[0]]=[]
        d[i[0]].append(i)
    else:
        if i not in d[i[0]]:
            d[i[0]].append(i)
for k,v in d.items():
    print(k,":",v)
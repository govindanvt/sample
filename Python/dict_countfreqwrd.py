t_string=input("Enter string: ")
l=[]
l=t_string.split()
w_freq=[l.count(p) for p in l]
print(dict(zip(l,w_freq)))
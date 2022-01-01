def sum(a,b):
    return a+b
L1=[1,2,3]
L2=[4,5,6,8,9]
L=[x for x in map(sum,L1,L2)]
print(L)
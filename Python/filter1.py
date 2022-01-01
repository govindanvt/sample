def even(a):
    if a%2==0: return True
    else: return False
l1=[1,2,3,8,9,11,7]
L=[x for x in filter(even, l1)]
print(L)
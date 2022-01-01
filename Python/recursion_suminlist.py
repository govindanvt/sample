def sumflatlist(s):
    t=0
    for i in s:
        if type(i) == type([]):
            t=t+sumflatlist(i)
        else:
            t=t+i
    return t
print("Sum is: ",sumflatlist([[2,3],[5,8]]))
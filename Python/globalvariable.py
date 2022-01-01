a=1
def f():
    print("Inside f(): ",a)
def g():
    a=2
    print("Inside g(): ",a)
def h():
    a=3
    print("Inside h(): ",a)
print(" Global: ",a)
f()
print(" Global: ",a)
g()
print(" Global: ",a)
h()
print(" Global: ",a)
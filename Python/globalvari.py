def f():
    global s
    print(s)
    s="Look into myself"
    print(s)
s="I love myself"
f()
print(s)
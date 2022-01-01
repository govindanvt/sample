class Counter:
    c=0
    def __init__(self,name):
        self.name=name
        print(name,"created")
        Counter.c+=1
    def __del__(self):
        print(self.name,"deleted")
        Counter.c-=1
        if Counter.c==0:
            print("Last Counter object deleted:")
        else:
            print(Counter.c,"Counter OBJECT remaining")
x=Counter("First")
y=Counter("Second")
z=Counter("Third")
l=Counter("Naveen")
m=Counter("Megha")
n=Counter("Abhi")
del x
del y
del z
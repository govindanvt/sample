class Bird:
    def __init__(self,type):
        self.type=type
        def eat(self):
            return True
        def flylong(self):
            return True
        def petbirds(self):
            return True
class FlyBird(Bird):
    def eat(self):
        print("Bird eat veg and non-veg")
    def flylong(self):
        print("Some bird can Fly long distance")
    def petbirds(self):
        print("Some flying birds are good pet for human")
class NonflyingBird(Bird):
    def eat(self):
        print("Bird eat veg and non-veg and weak to collect food")
    def flylong(self):
        print("These birds are not long running")
    def petbirds(self):
        print("Non-flying birds are also good pet for human")
b=[FlyBird('Eagle'),NonflyingBird('Emu')]
for i in b:
    print(i.type)
    print(i.eat())
    print(i.flylong())
    print(i.petbirds())
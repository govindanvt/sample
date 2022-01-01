class Shark():
    def swim(self):
        print("The Shark is Swimming..!")
    def swim_backwards(self):
        print("Shark cannot swim backwards,but can sink backwards")
    def skeleton(self):
        print("The shark's skeleton is made of Cartilage")
class Clownfish():
    def swim(self):
        print("The clownfish is Swimming..!")
    def swim_backwards(self):
        print("Clownfish can swim backwards")
    def skeleton(self):
        print("The clownfish's skeleton is made of bone")
s=Shark()
s.skeleton()
c=Clownfish()
c.skeleton()
print("\n----------------------------------------------------------------------\n")
for f in (s,c):
    f.swim()
    f.swim_backwards()
    f.skeleton()
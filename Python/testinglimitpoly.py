# A simple python program to demonstrate
# working of iterates using an example type
# That iterates from 10 to given value
# an iterable user defined type
class Test:
    #constructor
    def __init__(self,limit):
        self.limit=limit
    #called when iteration is initiated
    def __iter__(self):
        self.x=10
        return self
    #To move to next element I python 3
    # We should replace next with __next__
    def __next__(self):
        #store current value of x
        x=self.x
        #stop iteration if limit is reached
        if x>self.limit:
            raise StopIteration
        #else Increment and return old value
        self.x=x+1
        return x
#prints numbers from 10 to 50
for i in Test(50):
    print(i)

#print nothing
for i in Test(5):
    print(i)
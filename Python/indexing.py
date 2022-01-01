from collections.abc import Sequence
class Mystructure(Sequence):
   def __init__(self):
       self.data=[]
   def __len__(self):
       return len(self.data)
   def append(self,item):
       self.data.append(item)
   def remove(self,item):
       self.data.remove(item)
   def __repr__(self):
       return str(self.data)
   def __getitem__(self,sliced):
       return self.data[sliced]
m=Mystructure()
m.append('First Element')
m.append('Second Element')
m.append('Third Element')
m.append('Forth Element')
m.append('Fifth Element')
m.append('Sixth Element')
print(m[0])
print(m[1:4])
print(m)

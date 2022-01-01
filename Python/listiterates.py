#define a list
my_list=[4,7,0,3]

#get an iterator using iter()
my_iter= iter(my_list)

## iterate trough it using next()

#point4

print(next(my_iter))

#point7
print(next(my_iter))

##next(obj)is same as obj. __next__()

#point 0
print(my_iter.__next__())

#point3
print(my_iter.__next__())

##This will raise error.no items left

print(next(my_iter))
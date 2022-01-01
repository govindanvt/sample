print("Please enter a hyphen seperated string: ")
a=[n for n in input().split('-')]
a.sort()
print("Sorted: ")
print('-'.join(a))
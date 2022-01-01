d={'a':5,'b':84,'c':13,'d':5}
print("\ninitial Dictionary \n D = ",d)
key=input("Enter the key to delete(a-d): ")
if key in d:
    del d[key]
else: 
    print("Key not found: ")
    exit(0)
print("Updated Dictionary \n D = ",d)
from string import ascii_lowercase as asc_lower
def check(s):
    return set(asc_lower) - set(s.lower()) == set([])
s=input("Enter a String: ")
if check(s) == True:
    print("The String is a Pangram..")
else:
    print("The string isn't Pangram..")

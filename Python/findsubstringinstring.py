s=input("Enter a Sentence: ")
sub=input("Enter a Word to search: ")
if s.find(sub)==-1:
    print("Substring is not found in string..")
else:
    print("Substring is present..")
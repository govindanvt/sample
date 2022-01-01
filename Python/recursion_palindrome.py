def pali(n):
    if len(n)<1:
        return True
    else:
        if n[0]==n[-1]:
            return pali(n[1:-1])
        else:
            return False
n=str(input("Enter a string: "))
if pali(n)==True:
    print("String is Palindrome..")
else:
    print("String is not Palindrome..")
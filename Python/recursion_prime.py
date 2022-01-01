def ch_prime(n, div = None):
    if div is None:
        div = n-1
    while div >=2:
        if n % div==0:
            print("Number is not Prime...!")
            return False
        else:
            return ch_prime(n, div-1)
    else:
        print("Number is Prime...!")
        return True
n=int(input("Enter a Number: "))
ch_prime(n)    
#Program to depict else clause try-except
#Function will return a/b
def AbyB(a,b):
    try:
        c=((a+b)/(a-b))
    except ZeroDivisionError:
        print("a/b result is infinity because of denominator 0")
    else:
        print("The result is :",c)
    finally:
        print("This is the final block...!")
AbyB(3.0,2.0)
AbyB(3.0,3.0)

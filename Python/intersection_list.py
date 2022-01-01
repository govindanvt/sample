def intersection(a, b):
    return list(set(a) & set(b))
def main():
    alist=[]
    blist=[]
    n=int(input("Enter no.of elements for list 1: "))
    m=int(input("Enter no.of elements for list 2: "))
    print("for List 1: ")
    for i in range(1,n+1):
        a1=int(input("Enter the Elements: "))
        alist.append(a1)
    print("For List 2: ")
    for i in range(1,m+1):
        b1=int(input("Enter the Elements: "))
        blist.append(b1)
    print("The intersection is: ")
    print(intersection(alist,blist))
main()
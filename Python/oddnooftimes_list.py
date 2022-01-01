def find_odd(alist):
    #return the elements that occurs odd numbers of times in alist    
    #alist is a list in which all elements except one element occurs an even numbers of times
    ans=0
    for ele in alist:
        ans ^= ele
    return ans
alist = input("Enter the list: ").split()
alist = [int(i) for i in alist]
ans = find_odd(alist)
print("The element that occurs odd number of times: ",ans)
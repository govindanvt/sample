def find_max_subarray(alist,start,end):
    #return (l,r,m) such that alist(l:r) is the maximum subarray in 
    #A[start:end] with sum m. Here A[start:end] means all A[x] for start <= x < end.
    
    #base case
    if start == end - 1:
        return start, end, alist[start]
    else:
        mid=(start+end)//2
        l_start,l_end,l_max= find_max_subarray(alist, start, mid)
        r_start,r_end,r_max= find_max_subarray(alist, start, end)
        c_start,c_end,c_max= find_max_subarray(alist, start, mid, end)
        if l_max > r_max and l_max > c_max:
            return l_start, l_end, l_max
        elif r_max > l_max and r_max > c_max:
            return r_start, r_end, r_max
        else: 
            return c_start, c_end, c_max
def find_max_crossing_subarray(alist, start, mid, end):
    #return (l,r,m) such that alist(l:r) is the maximum subarray within alist
    #with start <= l < mid <= r < end with sum m. The arguments start, mid,
    #end must satisfy start <= mid <= end.
    s_left=float('-inf')
    s_temp = 0
    c_start = mid
    for i in range(mid - 1, start - 1, -1):
        s_temp = s_temp + alist[i]
        if s_temp > s_left:
            s_left=s_temp
            c_start=i
    s_right = float('-inf')
    s_temp = 0
    c_end = mid + 1
    for i in range(mid,end):
        s_temp = s_temp + alist[i]
        if s_temp > s_right:
            s_right = s_temp
            c_end = i+1
    return c_start, c_end, s_left + s_right

alist = input("Enter the list of numbers: ")
alist = alist.split()
alist = [int(x) for x in alist]
start, end, maximum = find_max_subarray(alist, 0, len(alist))
print('The maximum subarray starts at index {}, ends at index {}'
      ' and has sum {}.'.format(start, end - 1, maximum))
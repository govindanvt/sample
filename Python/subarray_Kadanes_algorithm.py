def find_max_subarray(alist, start, end):
    #Return (l,r,m)such that alist[l:r] is the maximum subarray in 
    #A[start: end] with sum m. Here A[start:end] means all a[x] for start<=x<end.
    max_ending_at_i = max_seen_so_far = alist[start]
    max_left_at_i = max_left_so_far =start
    #max_right_at_i is always i+1
    max_right_so_far = start+1
    for i in range(start+1, end):
        if max_ending_at_i > 0:
            max_ending_at_i += alist[i]
        else:
            max_ending_at_i = alist[i]
            max_left_at_i = i
        if max_ending_at_i > max_seen_so_far:
            max_seen_so_far = max_ending_at_i
            max_left_so_far = max_left_at_i
            max_right_so_far = i+1
    return max_left_so_far, max_right_so_far, max_seen_so_far

#main
alist = input("Enter the list of numbers")
alist = alist.split()
alist = [int(x) for x in alist]
start, end, maxi = find_max_subarray(alist, 0, len(alist))
print('The maximum subarray start at index{}, ends at index {}'
      'and has sum {}.'.format(start, end - 1, maxi))
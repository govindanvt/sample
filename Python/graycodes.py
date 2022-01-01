def get_graycode(n):
    #return n-bit graycode in a list..
    if n==0:
        return ['']
    first_half = get_graycode(n-1)
    second_half = first_half.copy()
    
    first_half = ['0' + code for code in first_half]
    second_half = ['1' + code for code in reversed(second_half)]
    
    return first_half + second_half

#main
n=int(input("Enter the no.of bits: "))
codes = get_graycode(n)
print("All {}- bit Gray codes: ", format(n))
print(codes)
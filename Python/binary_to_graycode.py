def binryto_graycode(n):
    #Convert binary to gray codeword and return it.
    n=int(n,2) #convert to int
    n ^= (n>>1)
  
    #bin(n) returns n's binary representation with a '0b' prefixed
    # the slice operation is to remove the prefix
    return bin(n)[2:]

#main
g = input("Enter Binary number: ")
b = binryto_graycode(g)
print("Gray codeword: ",b)
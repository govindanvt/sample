def lcm_num(a,b):
    lcm_num.multiple=lcm_num.multiple+b
    if lcm_num.multiple % a==0 and lcm_num.multiple % b==0:
        return lcm_num.multiple
    else:
        lcm_num(a,b)
    return lcm_num.multiple
lcm_num.multiple=0
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if a>b: 
    LCM=lcm_num(b,a)
else:
    LCM=lcm_num(a,b)
print(LCM)

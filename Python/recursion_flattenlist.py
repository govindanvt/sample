def flat(s):
    if s==[]:
        return s
    if isinstance(s[0],list):
        return flat(s[0]) + flat(s[1:])
    return s[:1] + flat(s[1:])
s=[[1,2],[3,4]]
print("Flattened list is: ",flat(s))
    
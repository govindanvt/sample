def interchange(strr):
    return strr[-1:] +strr[1:-1] + strr[:1]
strr=input("Enter String: ")
print("Modified string: ")
print(interchange(strr))
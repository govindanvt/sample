print("Marksheet of a student....##")
s1=int(input("Enter the first mark: "))
s2=int(input("Enter the second mark: "))
s3=int(input("Enter the third mark: "))
s4=int(input("Enter the forth mark: "))
s5=int(input("Enter the fifth mark: "))
avg=(s1+s2+s3+s4+s5)/5
print("Average is: ",avg)
if avg>=90:
    print("Grade is: A")
elif avg>80 and avg<90: 
    print("Grade is: B")
elif avg>70 and avg<80 : 
    print("Grade is: C")
elif avg>=60 and avg<70: 
    print("Grade is: D")
elif avg>50 and avg<60: 
    print("Grade is: E")
elif avg>40 and avg<50: 
    print("Grade is: F")
else: 
    print("You are failed...sorry..!!")

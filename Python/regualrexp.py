import re
pattern=re.compile("A.....T")
matchObject=pattern.match("ACGTAAT")
if(matchObject):
    print(matchObject.group())
    print(matchObject.start(),matchObject.end())

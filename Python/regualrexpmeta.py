import re
regex = re.compile("\s\d\d\d\s")
m=regex.search("Hello 12 cats ran after 432 dogs")
if m:
    print(m.group())
    print(m.span())

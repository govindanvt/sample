import re
regex = re.compile("\s\w\w\w\s")
mList=regex.findall("All cat ran after 432 dogs")
for m in mList:
    print(m)
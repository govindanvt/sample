import re
regex=re.compile("(\d\d)-(\d\d)-(\d\d\d\d)")
match=regex.match("18-01-2020")
if match:
    print("Day",match.group(1))
    print("Month",match.group(2))
    print("Year",match.group(3))
    print("Date",match.group(0))
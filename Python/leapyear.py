year=int(input("Enter a year for check leap year or not: "))
if year%4==0 and year%100!=0 or year%400==0:
    print(year,"Is Leap Year....")
else:
    print(year,"Is Not Leap Year....")
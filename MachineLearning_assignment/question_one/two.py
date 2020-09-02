#


from datetime import date
year1 = int(input("year_one : "))
month1 = int(input("month_one : "))
day1 = int(input("day_one : "))

year2 = int(input("year_two : "))
month2 = int(input("month_two : "))
day2 = int(input("day_two : "))

d1 = date(year1, month1, day1)

d2= date(year2, month2, day2)

d = d2 - d1

print("Difference between",d1,"and",d2,"is: ",d.days)
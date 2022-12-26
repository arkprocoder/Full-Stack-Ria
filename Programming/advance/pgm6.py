# dates

import datetime
x = datetime.datetime.now()
print(x)
print(x.date())
print(x.time())
print(x.second)
print(x.year)
print(x.month)
print(x.microsecond)
print(x.minute)
print(x.day)
print(x.strftime("%B"))
print(x.strftime("%A"))


# setting the date
y = datetime.datetime(2020, 5, 17)
print(y)

# x = datetime.datetime(2018, 6, 1)
# print(x.strftime("%B"))
# print(x.strftime("%A"))
x=int("6")
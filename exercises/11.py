'''
98000
10000 = 0
10000= 10
78000 = 20

15600+1000=16600
'''

income=9999
tax=0
print("Given Income in ",income)

if(income<=10000):
    tax=0

elif(income<=20000):
    netamounttax=income-10000
    tax=netamounttax*10/100
else:
    # first 10,000
    tax=0
    # next 10,000 is 10%
    tax=10000*10/100
    # next remaining amount is 20%
    tax=tax+(income-20000)*20/100

print("final tax ",tax)




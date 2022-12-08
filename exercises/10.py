number=1234
print("given number is ",number)

while(number>0):
    lastdigit=number%10;
    number=number//10
    print(lastdigit,end=" ")
'''
1st
while(1234>0):
    lastdigit=1234%10
    lastdigit=4
    number=1234//10
    number=123
    print(4)
2nd
while(123>0):
    lastdigit=123%10
    lastdigit=3
    number=123//10
    number=12
    print(3)
3rs
while(12>0):
    lastdigit=12%10
    lastdigit=2
    number=12//10
    number=1
    print(2)
4th
while(1>0):
    lastdigit=1%10
    lastdigit=1
    number=1//10
    number=0
    print(1)
'''
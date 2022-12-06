'''
# problem 1
for i in range(1,100,2):
    print(i)
print("----------------------------------")
# problem 2
for i in range(0,101,2):
    print(i)
print("----------------------------------")
for i in range(20,101,20):
    print(i)
print("----------------------------------")

#problem 4a

i=1
while(i<=10):
    print(i)
    i=i+1
print("----------------------------------")
#problem 4b
i=0
while(i<100):
    i=i+2
    print(i)
print("----------------------------------")
#problem 4c
i=1
while(i<100):
    i=i+2
    print(i) 
    if(i==51):
        break

print("----------------------------------")
#problem 4d
i=0
while(i<100):
    i=i+1
    if(i==55):
        continue
    print(i) 
print("----------------------------------")  



# problem 5

num=int(input("enter the table number :\n"))
for i in range(1,11):
    print(f'{num} X {i}  = {num*i}')
'''
# problem 7

name=input("enter the student name :\n")
eng=int(input("Enter eng  marks \n"))

kan=int(input("Enter kan marks \n"))
hin=int(input("Enter hin marks \n"))
social=int(input("Enter social marks \n"))
science=int(input("Enter science marks \n"))
math=int(input("Enter math marks \n"))
avg=(eng+kan+hin+social+science+math)/6
if(eng>0 and eng<=100 and kan>0 and kan<=100 and hin>0 and hin<=100 and social>0 and social<=100 and science>0 and science<=100 and math>0 and math<=100):
    if avg<35:
        print(f'You have failed\nYou got {avg} %\nGrade is f ')
    
    elif(avg>=35 and avg<55):
        print(f'You have just pass \nYou got {avg} %\nGrade is d ')
    
    elif(avg>=55 and avg<60):
        print(f'You have passed \nYou got {avg} %\nGrade is c ')
    
    elif(avg>=60 and avg<75):
        print(f'You have average \nYou got {avg} %\nGrade is b ')
    
    elif(avg>=75 and avg<90):
        print(f'You have good \nYou got {avg} %\nGrade is a ')
    
    elif(avg>=90 and avg<=100):
        print(f'You have excellent \nYou got {avg} %\nGrade is a+ ')

    else:
        pass
      

else:
    print("Dont give negative numbers or greater than hundred")
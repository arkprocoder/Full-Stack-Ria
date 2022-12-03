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


'''
# problem 5

num=int(input("enter the table number :\n"))
for i in range(1,11):
    print(f'{num} X {i}  = {num*i}')
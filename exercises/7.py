num=int(input("enter the pattern number:\n"))
for i in range(1,num+1):
    for j in range(i):
        print(i,end=" ")
    print("\n")
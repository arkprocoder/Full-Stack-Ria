mylist=["mahonar","sriram","bhanu","mahesh","abhishek"]
# mylist=("mahonar","sriram","bhanu","mahesh","abhishek")
# for i in mylist:
#     print(i)

newList=enumerate(mylist,100)
newList=list(newList)
print(newList)
print(type(newList))
print(newList[4])

for i,j in enumerate(mylist,0):
    print(i,j)

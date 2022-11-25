# list

'''mylist=[2,3,4,1,5,6,7,"apple","banana","orange",15.236,True]
print(mylist)
print(type(mylist))
print(mylist[7])
print(mylist[11])
# print(mylist[12])
'''
mylist=[1,1,1,2,3,7,8,9,4,5,6]
mylist.sort()
mylist.append(10)
mylist.reverse()
# mylist.remove(17)
print(mylist.count(1))
newList=mylist.copy()
mylist.pop()
mylist.pop()
print("new list",newList)
print(mylist)

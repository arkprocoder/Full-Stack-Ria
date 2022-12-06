# lists
'''mylist=[1,2,3,4,5,"apple","orange","melon",34.456,23.34,True,[1,2,3]]
print(mylist)
# print(type(mylist))
print(mylist[6])
print(mylist[10])'''

mylist=[1,2,3,4,8,9,0,5,6,7,2,3,4,2,3,4]
mylist.sort()
print(mylist)
mylist.append(10)
print(mylist)
mylist.pop()
print(mylist)
# mylist.clear()
# print(mylist)
print(mylist)
newList=mylist.copy()
print("newlist",newList)
print(mylist.count(2))
mylist.reverse()
print(mylist)
print(len(mylist))


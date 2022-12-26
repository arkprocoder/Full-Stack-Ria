def mergeList(list1,list2):
    newList=[]

    for i in list1:
        if i%2 != 0:
            newList.append(i)
            
    for j in list2:
        if j%2 == 0:
            newList.append(j)

    return newList

list1=[7,12,45,78,96,45,98,32]
list2=[1,5,9,48,98,75,69,32,36,42]
res=mergeList(list1,list2)
print("new list ", res)
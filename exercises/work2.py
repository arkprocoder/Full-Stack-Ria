'''mylist=[23,4,5,6,7,8,1,2,3,9,0,122,10,2,3,4,3,3,2]
mystr= "Ria Institue of Technology"
1)write a python program to evaluate below list
a)Add the items in list 
b)Find the length of the list
c)sort the elements from the list
d)reverse the list
e)Count the duplicates elementsfrom the list (3,2)
g)print "Institue" using slicing
h)print "Institue" using Technology
i)print "Ria Institue of"
j)print "Rs"'''
mylist=[23,4,5,6,7,8,1,2,3,9,0,122,10,2,3,4,3,3,2]
mystr= "Ria Institue of Technology"
#total=0
#for i in mylist[23,4,5,6,7,8,1,2,3,9,0,122,10,2,3,4,3,3,2]:
   # print(total.append(i))
    #print(total)
#a
total=sum(mylist)
print('sum of the all elements in mylist :',total)
#b
print(len(mylist))
#c
mylist.sort()
print(mylist)
#d
mylist.reverse()
print(mylist)
#e
print(mylist.count(3)+mylist.count(2))
#g
print(mystr[4:12])
#i
print(mystr[:12])
#j
print(mystr[0:6])


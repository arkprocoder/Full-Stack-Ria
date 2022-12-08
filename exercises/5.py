def mylist(ilist):
    first_element=ilist[0]
    last_element=ilist[-1]
    if first_element==last_element:
        return True
    else:
        return False

res=mylist([10,2,4,5,6,7,8,10])
print(res)
res=mylist([10,2,4,5,6,7,9,5,6,8,20])
print(res)
res=mylist([10,2,4,5,6,7,8,30])
print(res)
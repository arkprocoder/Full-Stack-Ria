# a=[1,2,3,4,5,6]
# b=[2,5,0,7,3]
# c=list(filter(lambda x:x not in b,a))
# # c=list(filter(lambda x:x not in a,b))
# c=list(filter(lambda x:x  in a,b))
# print(c)
# val=[10,20,30,5,15,25,30,4]
'''def greater(number):
    # print("abc")
    return (number>10)*2

res=list(filter(greater,val))
print(res)'''  #defect


from functools import reduce

x=[1,2,3,4,5]

x=[2,3,4,5]
x=[6,4,5]
x=[24,5]
x=[120]

res=reduce((lambda x,y:x*y),x)
print(res)
print(type(res))

# map()
# 1
numbers=[1,2,3,4,5,6,7]
res=list(map((lambda x:x*2),numbers))
print(res)

# 2
def square(a):
    return a*a

def cube(a):
    return a*a*a

functions=[square,cube]
numbers=[2,4,6,8]

for i in numbers:
    res=list(map(lambda x:x(i),functions))
    print(res)

'''
1st iteration


for 2 in [2,4,6,8]:
    res=list(map(lambda x:x(i),functions))
    res=list(map(lambda x:x(2),[square,cube]))
    res=list(map(lambda x:x(2),[4,8]))
    print([4,8])

[4,8] 

2nd iteration


for 4 in [2,4,6,8]:
    res=list(map(lambda x:x(i),functions))
    res=list(map(lambda x:x(4),[square,cube]))
    res=list(map(lambda x:x(2),[16,64]))
    print([16,64])
   
[16,64]

3rd iteration


for 6 in [2,4,6,8]:
    res=list(map(lambda x:x(i),functions))
    res=list(map(lambda x:x(6),[square,cube]))
    res=list(map(lambda x:x(6),[36,216]))
    print([36,216])
   
[36,216]

# 4th iteration

for 8 in [2,4,6,8]:
    res=list(map(lambda x:x(i),functions))
    res=list(map(lambda x:x(8),[square,cube]))
    res=list(map(lambda x:x(8),[64,512]))
    print([64,512])
   
[64,512]

# stop iteration

output :
[4, 8]
[16, 64]
[36, 216]
[64, 512]

'''
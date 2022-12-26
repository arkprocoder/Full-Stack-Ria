# Comprehensions
# list
mylist=[]
for i in range(11):
    print(i)
    if i%2==0:
        mylist.append(i)
    if i==8:
        break
print(mylist)

# mylistCompress=[i for i in range(21) if i%2==0]
# print(mylistCompress)

# #set comprehension
# alphaaa=["a","b","c","d","e","c","a"]
# alphabets={i for i in alphaaa if i!="b"}
# print(alphabets)


#dictionary comprehensions


# normal_Dict={

#     0:"name 0",
#     1:"name 1",
#     2:"name 2",
#     3:"name 3",
#     4:"name 4",
#     5:"name 5",
# }
# print(normal_Dict)

# dictCompress={i:f'Name {i}' for i in range(1,101) if i%2!=0}
# # dictCompress={i:f'Name {i}' for i in range(1,101)}
# print(dictCompress)

# # yeild
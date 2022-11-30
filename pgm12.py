# f=open("ria.txt")
# print(f.read())
# f.close()

# f=open("ria.txt")
# print(f.readline())
# print(f.readline())
# f.close()

# f=open("ria.txt")
# myfiledata=f.readlines()
# print(myfiledata[1:3])
# f.close()

# f=open("ria.txt")
# data=f.read()
# for i in data:
#     print(i)
# f.close()

# f=open("newfile.txt","x")
# data=f.write("\nAnees")
# data=f.writelines("developer")
# data=f.writelines("programmer")
# f.close()

f=open("ria.txt","r+")
print(f.read())
f.write("ark")
f.close()

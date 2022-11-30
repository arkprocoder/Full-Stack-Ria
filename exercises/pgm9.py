# my=[1,2,3]
# my[1]=123
# mytup=(1,2,3,4)
# print(type(mytup))
# print(mytup[2])
# mytup[2]=34
# print(mytup)

# mydict={"key":"Values"}
# print(type(mydict))

mydict={"name":"Rohan",
"age":23,
"likes":["cricket","football"],
"role":"developer"}

print(mydict)
print(mydict["age"])
print(mydict["likes"])
# print(mydict["likes"])

print(mydict.items())
print(mydict.keys())
print(mydict.values())

mydict.update({"name":"mohan"})
# mydict.pop("role")
# print(mydict)
# mydict.clear()
newdict=mydict.copy()
print(mydict)
print(newdict)
print(mydict.get("age"))
print(mydict.get("aa"))

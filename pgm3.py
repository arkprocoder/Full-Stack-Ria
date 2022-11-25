# Strings....
name="ria INstitute"
# a=12
# b=13.233

print(name)
print(type(name))
# print(type(a))
# print(type(b))
print(name.capitalize())
print(name.upper())
print(name.lower())
print("the length of the string is ",len(name))
# print(name)


print(name.endswith('e'))
print(name.endswith('end'))
print(name.startswith('Ria'))
print(name.index("a"))
# print(name.index("z"))
print(name.find("INstitute"))
print(name.find(" "))
# print(name.find("z"))
print(name.count("t"))
print(name.count("i"))
# print(name.replace(name,"Ria Institute of technology"))
name=name.replace(name,"Ria Institute of technology")
print(name)
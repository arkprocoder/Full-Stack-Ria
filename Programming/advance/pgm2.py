# for else

# mylist=["a","b","c","d","e","f"]
# for i in mylist:
#     print(i)
# else:
#     print("i am else block of for loop")

items=["pizza","burger","friece"]
for i in items:
    if i=="chicken":
        print(i," is tasty")
        break
    print(i)
else:
    print("item not found")
    
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)
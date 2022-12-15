class Family:
    no_of_peoples=8 #public
    _siblings=4 #protected
    __sons=2 # private
class B(Family):
    pass

# obj1=Family()
# print(obj1.no_of_peoples)
# print(obj1._siblings)
# print(obj1._Family__sons)

obj2=B()
print(obj2._siblings)
print(obj2.no_of_peoples)
print(obj2._Family__sons)
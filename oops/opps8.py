# multiple inheritance
class Bestie:
    stars=10
    def __init__(self,bname,bage,blook,bheight,bhobby):
        self.name=bname
        self.age=bage # int type
        self.look=blook
        self.height=bheight
        self.hobby=bhobby #list type
        print("i have set the values for Bestie")

    def bestieDetails(self):
        print( f"MY bestie name is {self.name}\nAge is {self.age}\nLook is {self.look}\nHeight is {self.height}\nHobbies are {self.hobby}\nNo of stars {self.stars}") 
   

class Memories:
    place="Bangalore Karnataka"

    def __init__(self,placename,items,taste):
        self.placename=placename
        self.items=items
        self.taste=taste
        print("i have set the values for Memories")

    def printMemories(self):
        print( f"\nWe went to {self.place}\nResturant name is {self.placename}\nwe ate {self.items}\nthe taste as {self.taste}" )
    
    # @staticmethod
    def message(self,name):
        return f"hello {name}"

class Racing(Bestie,Memories):
# class Racing(Memories,Bestie):
    place="NS HIGHWAY"
    def Racing(self):
        return f"\n\nWhile Coming back we has a racing at {self.place}"

rohan=Bestie("Rohan",25,"awesome","tall",["sleeping","eating"])
rohan_memories=Memories("Corner House","Cake Fudge","Awesome")
# main class object below
rohan_race=Racing("Rohan",25,"awesome","tall",["sleeping,dancing"])
# rohan_race.bestieDetails()
# print(rohan_race.message("anees"))

# rohan_race1=Racing("Corner House","Desert Ice Cream","Awesome")
# print("_______________")
# print(rohan.bestieDetails())
# print("_______________")
# print(rohan_memories.printMemories())
# print("_______________")

# print("_______________")


# print("_______________")
print(rohan_race.Racing())
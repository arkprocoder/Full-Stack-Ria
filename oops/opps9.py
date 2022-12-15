class Animal:
    name="Animals"
    def __init__(self,animalname,animaltype):
        self.animalName=animalname
        self.animalType=animaltype

    def AnimalDetails(self):
        print(f"Animal name is {self.animalName}\nAnimal Type is {self.animalType}")

class Birds:
    bname="Birds"
    def __init__(self,birdname,birdtype,birdspan):
        self.birdname=birdname
        self.birdtype=birdtype
        self.birdspan=birdspan

    def BirdDetails(self):
        print(f"Bird name is {self.birdname}\nBird Type is {self.birdtype}\nBird Span is {self.birdspan}")

    def greet(self):
        print("Hello am a greet of class Birds")

class Nature(Animal,Birds):
    nname="Nature"
    

    def __init__(self, natureType, natureWeather,naturePlaceName,natureplacce):
        self.natureType=natureType
        self.natureWeather=natureWeather
        self.naturePlaceName=naturePlaceName
        self.natureplacce=natureplacce
  
    def natureDetails(self):
        print(f"This is a beautiful {self.name} {self.natureType} {self.natureWeather}")


class Nature1(Birds,Animal):
    name="Nature"

    def natureDetails1(self):
        print(f"This is a beautiful {self.name}")


obj1=Nature("Lion","wildanimal")
# obj2=Nature1("Parrot","herbivorous",10)

obj1.AnimalDetails()
print(obj1.bname)
print(obj1.name)
# obj1.BirdDetails()
obj1.greet()

obj=Nature("beautiful",21,"bangalore","karnataka")
obj.natureDetails()

obj3=Nature("sprarrow","birds",2)
obj3.BirdDetails()
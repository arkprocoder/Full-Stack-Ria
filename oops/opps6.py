# single level inheritance

class Parent:
    haircolor="Black"
    
    def __init__(self,name,height,bloodgroup,weight):
        self.name=name
        self.height=height
        self.bloodgroup=bloodgroup
        self.weight=weight

    def parentDetails(self):
        print(f"Name is {self.name}\nHeight is {self.height}\nBlood Group {self.bloodgroup}\nWeight is {self.weight}")

class Child(Parent):
    haircolor="White"
    def __init__(self,name,height,bloodgroup,weight,age):
        self.name=name
        self.height=height
        self.bloodgroup=bloodgroup
        self.weight=weight
        self.age=age

    def childDetails(self):
        print(f"Name is {self.name}\nHeight is {self.height}\nBlood Group {self.bloodgroup}\nWeight is {self.weight}\nAge is {self.age}")



child1=Child("Mohan",6.0,"B+",70,25)
# child1.childDetails()
# print(child1.haircolor)
# child1.parentDetails()

parent1=Parent("Rohan",5.5,"A+",80)
parent1.parentDetails()
print(parent1.haircolor)
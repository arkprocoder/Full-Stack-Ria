class Employee:   #Employee is a class Name it starts with Caps
    star=5         
    institute="RIA"
    location="marathalli"

    #Above star,intitute and location are the class varaibles can be accessed 
    # any objects by the same classs
     
    def institueDetails(self):
        print(f"Institue Name is {self.institute}\nIts located at {self.location}\ni will give {self.star} stars")
    
    #institueDetails is a method of the class Employee
    # it will be having self as a default positional Arguements using self
    # we can iterate the class varaibles  


    # def greeting():
    #     print("Good Morning")  ->this gives error becuz self argument is passed

akash=Employee()  #akash is a object
akash.institueDetails()
# akash.greeting()
# print(akash.location)
akash.location="Bangalore"  #here we are changing the instance Varaible and it applies
                            #only for akash object and this changee the class varaible
                            #that is location
akash.name="Akash"

# print(akash.location)
print("after changing the instance variable :location")
akash.institueDetails()
print("_________________________")

bhanu=Employee()
bhanu.institueDetails()
print("after changing the instance variable :stars")
bhanu.star=4
bhanu.institueDetails()
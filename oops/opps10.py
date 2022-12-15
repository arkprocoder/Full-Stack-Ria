# multilevel inheritance
class India:
    states=["karnataka","Ap","Up","kashmir","goa","tn"]
    def indiaDetails(self):
        print(f"India states are {self.states}")

class karnataka(India):
    district=["Chikabalapur","mangalore","Tumkur","Bangalore Urban"]
    def karnatakaDetails(self):
        print(f"karnataka district are {self.district}")

class Bangalore(karnataka):
    wards=["chamrajpet","hebbal","marathalli","devenhalli"]
    def BangaloreDetails(self):
        print(f"Bangalore wards are {self.wards}")


class Marathalli(Bangalore):
    instituteName=["Ria","governmentInstitue"]
    def instituteNameDetails(self):
        print(f"Marathalli institutes are {self.instituteName}")

obj1=Bangalore()
print(obj1.BangaloreDetails())
print(obj1.wards)
print(obj1.district)
print(obj1.karnatakaDetails())
print(obj1.states)
print(obj1.indiaDetails())
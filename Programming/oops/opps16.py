from abc import ABC,abstractmethod
 
class SmartPhone(ABC):  #this is abstract method
    mobileName="One +"

    @abstractmethod
    def camera(self):
        pass

    @abstractmethod
    def mediaplayer(self):
        pass

    @abstractmethod
    def whatsapp(self):
        pass

    def weatherapp(self):
        print("today the weather is cloudy")


class Phone(SmartPhone):

    def __init__(self,contacts,messages,notes):
        self.contact=contacts
        self.messages=messages
        self.note=notes

    def camera(self):
        print("On the Camera",self.note)

    def mediaplayer(self):
        print("Play Music")

    def whatsapp(self):
        print("Send Message")

    def weatherapp(self):
        return super().weatherapp()

obj1=Phone("ria","send message to ria","full stack")
obj1.camera()
obj1.mediaplayer()
obj1.whatsapp()
obj1.weatherapp()
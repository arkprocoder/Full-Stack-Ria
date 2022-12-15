from abc import ABC,abstractmethod

class Shape(ABC):

    @abstractmethod
    def mandatory(self):
        pass
    

    @abstractmethod
    def greet(self):
        print("good morning")
    
    def hello(self):
        print("hello")


class Circle( ):

    def mandatory(self):
        print('i am mandatory')
    

    def greet(self):
        return super().greet()

obj1=Circle()
obj1.greet()
obj1.mandatory()

obj2=Shape()
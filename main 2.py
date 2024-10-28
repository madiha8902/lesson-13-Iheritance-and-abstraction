from abc import ABC,abstractmethod

class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
      print("I can walk")

h=Human()
h.move()

class frog(Animal):
    def move(self):
     print("I acn jump")
f=frog()
f.move()
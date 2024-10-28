class person:

  def __init__(self,name,idno):
    self.name = name
    self.idno = idno
  def display(self):
        print("my name is" ,self.name)
        print("my id is" , self.idno)

class Child(person):
    def __init__(self,name,idno,salary,post):
     self.salary = salary
     self.post = post

     person.__init__(self,name,idno)

a=Child("madiha",520,10000,"manager")
a.display()
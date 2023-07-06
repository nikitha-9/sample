class info:
    def __init__ (self,id,name):
        self.id=id
        self.name=name
    def display(self):
        print(self.id,self.name)
ad=info(102,"nik")
ad.display()
#cant construct two constructors or two methods of same name within a class
#__init__ is keyword of constructor
class data:
    def __init__(self,v):
        self.v=v
    def display(self):
        print(self.v)
ad=data(99)#ad is a object created in this statement
ad.display()
#"encapsulation":      wrapping up all data into a single unit is called encapsulation
# write only classes
# write only classes,read only classes ,read and write both
#by default all data members of a class is of public type
# a concept namely access modifiers/specifiers:
   # shows the life and scope of members defined within class
#----->  public access
#private"  __ " (double underscore)

#protected "_"(single underscore)::  accesible within the class, outside  the class,from one class to another class by using inheritance





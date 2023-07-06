# object:real world entity and collection of attributes or fields
# id ,name,behaviour are objects properties
# class=logical entity collection of similar and dissimilar types of object,it is blue print of program
# "class classname" is syntax of class definiation, classname can b of any case either upper or lowr
# without object class is nothing
# a class contains(members):
# methods(functions using def)
# fields
# constructor
# destructor
# etc
# -------------6 features or properties of oops ---------
# object
# class 
# encapsulation
# polymorphism'
# inheritance
# abstraction
class hello:
    employee="nikita"
    def display(self):
        print("hai")#self is dummy and compulsory
    
obj=hello()
obj.display()
print(obj.employee)
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
# types of methods:
# static method,instance method,class method
#-----------------static method-----------------
class data:
    @staticmethod    #we can or cannnot use this decorater
    def calculate(n):
        print("static method",n**n)
data.calculate(2)
#---------------class method-----------
#here the decorater @classmethod is compulsory
class data:
    @classmethod    
    def calculate(u,n,n1):       #were first parameter is dummy should keep 1st parameter dummy
        print("class method",n**n1) #u can b self too
data.calculate(2,1)#i.e n=2 ,n1=1.u==dummy
#dynamic class method----------------
class data:
    
    def calculate(self,n,n1):
        print("static method",n*n1)
d1=data()
d1.calculate(2,9)
#w a p to append ,delete,display elements of list using class
lis=[22,77,89,74,90]
class mat:
    def display():
        print(lis)
        
        
        
        
    def delete(m):
        lis.remove(m)
        print(lis)
    def append(n):
        lis.append(n)
        print(lis)
mat.display()
mat.delete(90)
mat.append(66)
        


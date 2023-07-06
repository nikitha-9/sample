#private------> "__" use dble undscre
class A:
    def __hello(self):
        print("private data")
    def show(self):
        self.__hello()
        print("public method")
obj=A()
obj.show()
#-----------------------------------encapsulation------------------
#getter()::reads and write d data and returns data,,,,,,,,setter():reads data of the class
class Student:
    def setid(self,id):
        self.__id=id
    def getid(self):
        return self.__id
s1=Student()
s1.setid(6703)
print(s1.getid())
#------------------------inheritance-----------------
# a class is derieved within a class
#IS-A relationship concept we use in this(parent-child)
# parent class= super or base class   "here  for child class object is created which can also manipulAate super classs
# a prog on inhertance , unlike java we dsnt use "extends"   keyword
class A:
    def methodA(self):
        print("A method")
class B(A):# inheritance
    def methodB(self):
        print("method B")
ad=B()
ad.methodA()
ad.methodB()
ob=A()
ob.methodA()
                


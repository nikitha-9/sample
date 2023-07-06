#manipulation of data(public variables) from one class to another class
class A:
    def insert(self,id,salary):
        self.id=id#public variable
        self.salary=salary#public variable
    def display(self):
        print(self.id,self.salary)
class B:
    def data(self,obj):
        obj.salary+=100
        obj.display()
obj=A()
obj1=B()
obj.insert(101,7899)
obj.display()
obj1.data(obj)



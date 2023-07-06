#----------------constructor--------------
class student:
    def insert(self,id,name,marks):
        self.id=id
        self.name=name
        self.mk=marks
    def display(self):
        print("id={},name={}and marks={}"
              .format(self.id,self.name,self.mk))
    def calculate(self):
        if self.mk>=900:
            print("A")
        elif self.mk>=800:
            print("B")
        elif self.mk>=700:
            print("c")
        else:
            print("fail")
obj=student()
obj.insert(100,"nik",900)
obj.display()
obj.calculate()
#------------------ w a p to create a class which performs basic caluculater operations--------------
class calculate:
    def values(self,n,m):
        self.n=n
        self.m=m
    def add(self):
        print("sum :",self.n+self.m)
    def sub(self):
        print("diff is",self.n-self.m)
    def mul(self):
        print("multiplication is",self.n*self.m)
    def div(self):
        print("division",self.n/self.m)
x=int(input("enter x value"))
y=int(input("enter y value"))
op=input("enter operation")             
obj=calculate()
obj.values(x,y)
if op=="+":
    obj.add()
elif op=="-":
    obj.sub()
elif op=="*":
    obj.mul()
elif op=="/":
    obj.div()
else:
    print("invalid operation")
    


